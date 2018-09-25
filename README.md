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


5. Get  wallet address
   curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet7"}}' "http://52.13.195.226:8804/get_address"

6. Get  wallet height
   curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet7"}}' "http://52.13.195.226:8804/get_height"


Server 2:  54.70.55.32

1. Create address of a wallet
 curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet7"}}' "http://54.70.55.32:8804/create_address"

4. Transfer coin(JSON file: transfer.json)
curl -X POST \
-H "Content-Type: application/json" \
-d @transfer.json \
-X POST http://54.70.55.32:8804/transfer_coin


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
command=/home/ubuntu/kribbz_v1/build/run_kribbz.sh
directory=/home/ubuntu/kribbz_v1/build/
user=ubuntu
autostart=true
autorestart=true
stdout_logfile=/var/log/kribbz/kribbzd.log
stderr_logfile=/var/log/kribbz/kribbzd_err.log
stopsignal=INT
