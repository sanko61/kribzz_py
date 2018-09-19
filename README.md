# kribzz_py
WEB API requests

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

