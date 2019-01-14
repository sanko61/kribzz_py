JSON WEB API requests  to Python kribbz server
=================================================

1. create_address
--------------------
Create wallet  in system folder.
Input:
{"wallet":
   { "password":PWD,
     "wallet_name":W_NAME
   }
}
  where
  PWD  -  password,
  W_NAME  - wallet file name

Output:
{
    "msg": "Wallet existed or created successfully",
    "error": "0",
    "success": true,
    "address": "ckbzzBck5CACPEJGkt65ZLEvbho2FhcvY9X2H4gLhac2M6X9DqgjSpn5ct5YezHwvDhsWEcLaUhymZreAhtcQQ6mj3xpNq7hsxe"
}

Test:  curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet7"}}' "http://52.13.195.226:8804/create_address"


2. get_balance
 -----------------------
 Get balance of a wallet
Input: {"wallet": {"password":PWD,  "wallet_name":W_NAME} }

Output:
{
    "msg": "get_balance OK",
    "result": "{\"jsonrpc\": \"2.0\", \"id\": \"0\", \"result\": {\"locked_amount\": 0, \"available_balance\": 45000000, \"balance\": 45000000, \"unlocked_balance\": 45000000}}",
    "success": true,
    "error": "0"
}
Test:
curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet22"}}' "http://52.13.195.226:8804/get_balance"


3. get_transfers
--------------------------------
Get  wallet transfers
Input: {"wallet": {"password":PWD,  "wallet_name":W_NAME} }

Output:
{
u'msg': u'get_transfers OK',
u'result': u'{"jsonrpc": "2.0", "id": "0",
"result":
{"transfers": [
  {"fee": 140235756999999, "blockIndex": 25385, "time": 1546379440, "transactionHash": "cb936d2a3e347a9707b9d203e4a3f501c2899d95cade3cf9a04e6d60a79d488f",
   "amount": 1, "confirmations": 500, "unlockTime": 11, "address": "", "paymentId": "", "output": false,
   "kribbz_info": "{\\"transactionTotal\\":\\"9975000.00\\",\\"sellerName\\":\\"JohnClark\\",\\"cityName\\":\\"BeverlyHills\\",\\"zipCode\\":\\"90210\\",\\"longitude\\":\\"-118.413515\\",\\"buyerName\\":\\"EmilyStevens\\",\\"latitude\\":\\"34.079678\\",\\"streeAddress\\":\\"700RodeoDrive\\",\\"transactionId\\":\\"2019-01-0121:47:14\\",\\"transactionDateTime\\":\\"1523855778\\",\\"stateCode\\":\\"CA\\"}"}
]
}}',
u'success': True, u'error': u'0'}

Test:
curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet22"}}' "http://52.13.195.226:8804/get_transfers"


4. transfer_coin
-----------------------------
Transfer coin to address with KRIBBZ additional fieleds.
Input:{
 "kribbz": {
        "transactionId":transactionId, "streeAddress":"700 Rodeo Drive", "cityName":"Beverly Hills",
        "stateCode":"CA","zipCode":"90210","latitude":"34.079678","longitude":"-118.413515",
        "transactionDateTime":"1523855778",
        "transactionTotal":"9975000.00",
        "sellerName":"John Clark",
        "buyerName":"Emily Stevens",
        "agent_signature": signature1,
        "agent_pkey": agent_pkey,
        "investor_signature": signature2,
        "investor_pkey": investor_pkey,
        "owner_signature": signature3,
        "owner_pkey": owner_pkey,
        },
 "transfer": {
              "amount": amnt,
              "destination_address": dst,
   },
  "wallet": {
    "password":pwd,
    "wallet_name": wal_name,
   },
 }

Output:
{u'tx_hash': u'4c2b6c7fcd454b7c950f48771e83314728c502b5db52a05086132028ca62574e', u'msg': u'coin transfer successful', u'success': True, u'error': u'0'}

Test:
curl  -H "Content-Type: application/json" --request POST -d '
{
 "kribbz": {
        "transactionId":"643427363", "streeAddress":"700 Rodeo Drive", "cityName":"Beverly Hills",
        "stateCode":"CA","zipCode":"90210","latitude":"34.079678","longitude":"-118.413515",
        "transactionDateTime":"1523855778",
        "transactionTotal":"9975000.00",
        "sellerName":"John Clark",
        "buyerName":"Emily Stevens",
        "agent_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
        "agent_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
        "investor_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
        "investor_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
        "owner_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
        "owner_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
        },
 "transfer": {
              "amount": 3.3300000,
              "destination_address": "ckbzz9ntUJj4mx3j75nAss3CzvCGXASnYTejDexmfC7k6f4XLqsMJUKN7i84SEz6CTR9LM4ggBMRUgXBHhAtUAgtCvWzv8dGjPr",
              "fee": 100000,
   },
 "wallet":{ "password":"Password12345","wallet_name":"kribbz2"}}
}
' "http://52.13.195.226:8804/transfer_coin"




5. get_address
-------------------
 Get  wallet address
 Input: {"wallet": {"password":PWD,  "wallet_name":W_NAME} }
 Output:
 {
    "msg": "get_address OK",
    "result": "{\"jsonrpc\": \"2.0\", \"id\": \"0\", \"result\": {\"address\": \"ckbzzAkpo6cY3hRGrVhyYFNaH9uowjUDhVwN2APDo8TRjWsBewnM39i5MXxJmnDAJkbYFVA6rxMAuTSACbZbAMwT5FzK3sQnLro\"}}",
    "success": true,
    "error": "0"
 }
Test:
curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet7"}}' "http://52.13.195.226:8804/get_address"


6. get_height
----------------
Get  wallet height
 Input: {"wallet": {"password":PWD,  "wallet_name":W_NAME} }
 Output:
 {
    "msg": "get_height OK",
    "result": "{\"jsonrpc\": \"2.0\", \"id\": \"0\", \"result\": {\"height\": 26122}}",
    "success": true,
    "error": "0"
 }
 Test:
 curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet7"}}' "http://52.13.195.226:8804/get_height"


7. search_kribbz
---------------------
 Search incoming transaction by filter for all kribbz fields
 Input: {
  "wallet": {"password":PWD,  "wallet_name":W_NAME},
  "filter":{ "stateCode": state, "zipCode": zip, "transactionId":transactionId, "streeAddress": street, "cityName": city,
  "latitude":lat, "longitude": longitude, "transactionDateTime": v1, "transactionTotal":v2, "sellerName": v3, "buyerName": v4,
  }

 Output:
{
    "msg": "kribbz search successful",
    "transfers": [
        {
            "fee": 38900000,
            "transactionHash": "43dd8579d0bd87cc9de69b66e91cbd75c62002f0d994c95cb090f826e74ef576",
            "blockIndex": 4294967295,
            "amount": 55000000,
            "confirmations": -4294941156,
            "unlockTime": 38120448,
            "time": 0,
            "paymentId": "",
            "output": false,
            "kribbz_info": "{\"transactionTotal\":\"9975000.00\",\"sellerName\":\"JohnClark\",\"cityName\":\"BeverlyHills\",\"zipCode\":\"90210\",\"longitude\":\"-118.413515\",\"buyerName\":\"EmilyStevens\",\"latitude\":\"34.079678\",\"streeAddress\":\"700RodeoDrive\",\"transactionId\":\"643427363\",\"transactionDateTime\":\"1523855778\",\"stateCode\":\"CA\"}",
            "address": ""
        },
        ...........................
    ],
    "success": true,
    "error": "0"
}
Test:
 curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet24"},
 "filter":{"stateCode":"CA", "zipCode":"90210"}}' "http://52.13.195.226:8804/search_kribbz"

 curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet24"},
 "filter":{"streeAddress":"700RodeoDrive", "cityName":"BeverlyHills", "latitude":"34.079678", "longitude":"-118.413515", "transactionDateTime":"1523855778", "transactionTotal":"9975000.00", "sellerName":"JohnClark", "buyerName":"EmilyStevens"}}' "http://52.13.195.226:8804/search_kribbz"



8. get_transaction
-------------------
 Get transaction by hash.
 Input: {"transaction":{"txs_hash": tx_hash"}}
 Output:
 {
    "msg": "get_transaction OK",
    "result": {
        "status": "OK",
        "txs_as_hex": [
            "010b................."
        ],
        "missed_tx": []
    },
    "success": true,
    "error": "0"
 }
 Test:
 curl  -H "Content-Type: application/json" --request POST -d '{"transaction":{"txs_hash": "35b09d24dd11d4b5616951bfe7b0c460a1e2b759daee5ac02c76e1b53741e9d3"}}' "http://52.13.195.226:8804/get_transaction"


9. get_blockcount
------------------
 Get blockchain count.
 Input: {}
 Output:{
        "msg": "get_transaction OK",
        "result": {
            "jsonrpc": "2.0",
            "id": "0",
            "result": {
                "count": 22298,
                "status": "OK"
            }
        },
        "success": true,
        "error": "0"
  }
 Test:
   curl  -H "Content-Type: application/json" --request POST   "http://52.13.195.226:8804/get_blockcount"


10. get_blockhash
-------------------
   Get blockhash.
 Input: {"blockchain":{"block_number": N1}}
 Output:{
        "msg": "get_blockhash OK",
        "result": {
            "jsonrpc": "2.0",
            "id": "0",
            "result": "7dfb5b31a3e9e04f389a7db3c8f7d75c37db46fc73383bc4f157b300f9f3753c"
        },
        "success": true,
        "error": "0"
    }
  Test:
  curl  -H "Content-Type: application/json" --request POST -d '{"blockchain":{"block_number": 21}}' "http://52.13.195.226:8804/get_blockhash"


11. get_lastblockheader
---------------------------
 Input: {}
 Output:{
    "msg": "get_lastblockheader OK",
    "result": {
        "jsonrpc": "2.0",
        "id": "0",
        "result": {
            "status": "OK",
            "block_header": {
                "nonce": 2736453672,
                "reward": 70000000000,
                "hash": "9c1a588d05134642bde20bf2f2e9c6558ad6284f61855102dc50931e0da2a057",
                "timestamp": 1546519127,
                "major_version": 1,
                "minor_version": 0,
                "difficulty": 9934,
                "depth": 0,
                "prev_hash": "f14bee5b1c4344cccca0cc009500cd1cc5b7a0c94cee45ceaefc3e17e6d34cea",
                "orphan_status": false,
                "height": 26543
            }
        }
    },
    "success": true,
    "error": "0"
 }
 Test:
  Get last block.
    curl  -H "Content-Type: application/json" --request POST   "http://52.13.195.226:8804/get_lastblockheader"

