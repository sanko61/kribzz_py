# Python kribbz server

WEB API requests
====================
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





2. RUN, CONFIGS AND WALLETS  FILES
==================================
Folder /home/ubuntu/kribbz_v1/
  build/  :  C++  demon and wallet applications
  py_server/ :  Python server
  tests/      :  Python unitetsts


Folder /opt/kribbz  us used to store security files wallets and configs:

1)  demon_config:
 ....................................
start-mining=ckbzzCofaszeTMJXydCdJxiVgjdkv6TW9XGnpX3WfaNsf85y4L5vRNSbAYygPHbiYP7D7ZRMkPoGm3Zyop7CfMTu6j29UfBeXjT
.....................................

2)  wallet_config  kribbz_config:
 ..........................
wallet-file=/opt/kribbz/kribbz_wallet
password=Password12345
........................

3) Wallet files:  kribbz_wallet.wallet, kribbz_wallet.address, ..............



3.SUPERVISOR control
==============================
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



4. BUILD FROM REPO
======================
Python server:  https://github.com/sanko61/kribzz_py
C++  demon :    https://github.com/sanko61/KribbzDemon.git
Used  boost 1.64.0 version
