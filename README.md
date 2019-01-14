KRIBBZ BLOCKCHAIN
=================================
1. Source code
======================
C++  demon :    https://github.com/sanko61/KribbzDemon.git
Python server:  https://github.com/sanko61/kribzz_py
Used  boost 1.64.0 version

Cryptonote  standard:
https://cryptonote.org/standards
C++  Cryptonote fork is used:  https://catalyst.cash/
Based on https://cryptonotestarter.org/inner.html


2. Server  configuration
=========================
Folder /home/ubuntu/kribbz_v1/
  build/  :  C++  demon and wallet applications
  py_server/ :  Python server
  tests/      :  Python unitetsts

Folder /opt/kribbz  us used to store security files wallets and configs:
demon_config:
 ....................................
start-mining=ckbzzCofaszeTMJXydCdJxiVgjdkv6TW9XGnpX3WfaNsf85y4L5vRNSbAYygPHbiYP7D7ZRMkPoGm3Zyop7CfMTu6j29UfBeXjT
.....................................

wallet_config  kribbz_config:
 ..........................
wallet-file=/opt/kribbz/kribbz_wallet
password=Password12345
........................

Wallet files:  kribbz_wallet.wallet, kribbz_wallet.address, ..............


3.SUPERVISOR control
==============================
Supervisor is used to run Py server and C++ demon.

Two sections should be added to supervisor config file /etc/supervisor/supervisord.conf:
.....................................
[program:kribbz_server]
command=python  /home/ubuntu/kribbz_v1/py_server/kribbz_main.py
directory=/home/ubuntu/kribbz_v1/py_server/
user=ubuntu
autostart=true
autorestart=true
stdout_logfile=/var/log/kribbz/kribbz_server.log
stderr_logfile=/var/log/kribbz/kribbz_err.log
stopsignal=INT

[program:kribbzd]
command=sudo /home/ubuntu/kribbz_v1/build/kribbzd --config-file /opt/kribbz/demon_config --data-dir /home/ubuntu/.kribbz
directory=/home/ubuntu/kribbz_v1/build/
user=ubuntu
autostart=true
autorestart=true
stdout_logfile=/var/log/kribbz/kribbzd.log
stderr_logfile=/var/log/kribbz/kribbzd_err.log
stopsignal=INT
..................................
Commands:
  supervisorctl reread  - read modified config  file
  supervisorctl update  - update from config
  supervisorctl start all  -  start all demons


4. Python kribbz server. Wallet WEB API requests
=================================================
The requests work with simple_wallet application.  Kribbz Python server runs simple_wallet  with wallet name & password  and perform POST requests to the simple_wallet.
In first version password and wallet name are sended unsecure.

Test case of simple wallet operations:
1. Create address of a wallet
 curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet7"}}' "http://52.13.195.226:8804/create_address"

2. Get balance of a wallet
curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet7"}}' "http://52.13.195.226:8804/get_balance"

3. Get  wallet transfers
curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet7"}}' "http://52.13.195.226:8804/get_transfers"

4. Transfer coin(JSON file: transfer.json)
curl -X POST \
-H "Content-Type: application/json" \
-d @transfer.json \
-X POST http://52.13.195.226:8804/transfer_coin

5. Get  wallet address
   curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet7"}}' "http://52.13.195.226:8804/get_address"

6. Get  wallet height
   curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet7"}}' "http://52.13.195.226:8804/get_height"

7. Search by kribbz fields in wallet
   curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet7"},"filter":{"stateCode":"CA", "zipCode":"90210"}}' "http://52.13.195.226:8804/search_kribbz"

8. Get transaction by hash:
   curl  -H "Content-Type: application/json" --request POST -d '{"transaction":{"txs_hash": "35b09d24dd11d4b5616951bfe7b0c460a1e2b759daee5ac02c76e1b53741e9d3"}}' "http://52.13.195.226:8804/get_transaction"

9. Get blockchain count:
   curl  -H "Content-Type: application/json" --request POST   "http://52.13.195.226:8804/get_blockcount"
    Result JSON:
    {
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

10. Get blockhash:
   curl  -H "Content-Type: application/json" --request POST -d '{"blockchain":{"block_number": 21}}' "http://52.13.195.226:8804/get_blockhash"
   Result JSON:
    {
        "msg": "get_blockhash OK",
        "result": {
            "jsonrpc": "2.0",
            "id": "0",
            "result": "7dfb5b31a3e9e04f389a7db3c8f7d75c37db46fc73383bc4f157b300f9f3753c"
        },
        "success": true,
        "error": "0"
    }



5. Kribbz blockchain server. DEMON RPC API requests
=======================================================

1. getblockcount
curl  -H 'Content-Type: application/json' --request POST -d '{"jsonrpc":"2.0","id":"0","method":"getblockcount","params": {}}' 'http://127.0.0.1:23926/json_rpc'
return:
{"id":"0","jsonrpc":"2.0","result":{"count":11106,"status":"OK"}}


2. on_getblockhash
curl  -H 'Content-Type: application/json' --request POST -d '{"jsonrpc":"2.0","id":"0","method":"on_getblockhash","params":[21]}' 'http://127.0.0.1:23926/json_rpc'
return:
{"id":"0","jsonrpc":"2.0","result":"7dfb5b31a3e9e04f389a7db3c8f7d75c37db46fc73383bc4f157b300f9f3753c"}root@ip-172-31-20-249:~/kribbz_v1/build#
or return an error:
{"error":{"code":-32603,"message":"JsonValue type is not INTEGER"}

3. getcurrencyid
curl  -H 'Content-Type: application/json' --request POST -d '{"jsonrpc":"2.0","id":"0","method":"getcurrencyid","params":[]}' 'http://127.0.0.1:23926/json_rpc'
{"id":"0","jsonrpc":"2.0","result":{"currency_id_blob":"3d6cfcec34840b54e09456ea448c4dc865522ea099ed37bcd3de0dde0c73897c"}}root@ip-172-31-20-249:~/kribbz_v1/build#


4. f_transaction_json
curl  -H 'Content-Type: application/json' --request POST -d '{"jsonrpc":"2.0","id":"0","method":"f_transaction_json","params":{"hash":"72b4fac1975054749e7e79a0ce62e298a5b8f454a4051062054455b1da3bd08e"}}' 'http://127.0.0.1:23926/json_rpc'

{"id":"0","jsonrpc":"2.0","result":{"block":
{"cumul_size":774,"difficulty":72057594037927996,"hash":"26b0981af4e25af26dbed584908d15341749d8fe1b37c97e292328001345ea97","height":6937,
"timestamp":1537487369,"tx_count":2},"status":"OK",
"tx":{"":"72864e0a86d382d9995c7677c8ceff480cd1f718db5447159ea420b07d885106ecfecf3a92bc861042be32190d34282ed1594d9b170cb150c82e51488dec1309",
"extra":"01798c4473bff2e1a92d64d46567aa85e9f426a6164597ecde1b0f6700ab7c78a0","unlock_time":0,"version":1,
"vin":[{"type":"02","value":{"amount":70000000000,"k_image":"4ed4e7817b27c6fc2488e3863524502d493d67fc46872d63a8330e328929c3bb","key_offsets":[3253,1555]}}],
"vout":[{"amount":300000,"target":{"data":{"key":"0b436180bff4c0c355d8040202cf02e1b8b9917132f26f69f1f282aa69198ac1"},"type":"02"}},{"amount":2000000,"target":{"data":{"key":"f3d1fb08936965040d271546b20d4c2f10c4ec1a917df8f3d99ef37597ff801a"},"type":"02"}},{"amount":6000000,"target":{"data":{"key":"0dc252a5baa0b112fb38b255983863511ac70477c8c2a938df7eb0a47f28fa94"},"type":"02"}},{"amount":10000000,"target":{"data":{"key":"d586aae1118fd15bf7ea8d593cf8c7935ec5ec9e21fec7aae61006175b759e84"},"type":"02"}},{"amount":80000000,"target":{"data":{"key":"d3bf8f88b5bbfa7788be430360b3bb82cce196781d4dfd905a96edbb39fe094f"},"type":"02"}},{"amount":100000000,"target":{"data":{"key":"687c51b215ef77519521428d0882139949f9bc89423816b892aa5394ac090072"},"type":"02"}},{"amount":800000000,"target":{"data":{"key":"7be6f0144dec1214431c71bdcbc6d98da621c2f5a8b1c4d60c66e8e8253ae393"},"type":"02"}},{"amount":9000000000,"target":{"data":{"key":"5de86bdd13d563dc1f6a38b087c3f0150ed89a08de11d6883c4216a6ad23c33c"},"type":"02"}},{"amount":60000000000,"target":{"data":{"key":"90e8b50431ac35645f23b7a4fae08b14371d39b4229f551ef9869b0921b3948a"},"type":"02"}}]},"txDetails":{"amount_out":69998300000,"fee":1700000,"hash":"72b4fac1975054749e7e79a0ce62e298a5b8f454a4051062054455b1da3bd08e","mixin":2,"paymentId":"","size":545}}}root@ip-172-31-20-249:~/kribbz_v1/build#


5.getlastblockheader
curl  -H 'Content-Type: application/json' --request POST -d '{"jsonrpc":"2.0","id":"0","method":"getlastblockheader","params":{}}' 'http://127.0.0.1:23926/json_rpc'

{"id":"0","jsonrpc":"2.0","result":{"block_header":{"depth":0,"difficulty":9234,"hash":"a681cab8faf47cecd6511e5c0f3e5d07704e31cdba8c8d29700606c5bb2288aa","height":13315,
"major_version":1,"minor_version":0,"nonce":2958415970,"orphan_status":false,"prev_hash":"cbe0fdf59d38d0f419884e75b1126e29f6599dc2fedeb10d489818c134adebf1",
"reward":70000000000,"timestamp":1538424436},"status":"OK"}}


6. gettransactions
curl  -H 'Content-Type: application/json' --request POST -d '{"jsonrpc":"2.0","id":"0","txs_hashes":["4e5fa2439ce317be2af025f887a773d962c9dd76bc5a5442cdf7a8715ab37543"], "decode_as_json":true }' 'http://127.0.0.1:23926/gettransactions'

See   more requests  in:  https://getmonero.org/resources/developer-guides/daemon-rpc.html#get_transaction_pool

