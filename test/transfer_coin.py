#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  get_payments
"""

import requests
import json
import datetime
from kribbz_emu import transfer_coin

if __name__ == "__main__":
    # "ckbzz6v3RFwV3s5je4PzcDGTZdsHy5Dg13dCrXwYDctYQi1UXYd3jVDPAfNHJmrSxx4TvMnh1pVUUNudRrqXEL7D46nY8D4Virp",  # wallet24
    #  "ckbzzAbqtqhcrN89awPysMBjQLZwAsVvGC8yFaa5hJ1E6cY6oHEsJyY6rjLCuXWRc1dWCXZSCecGMWUPYrpJPHYP9LkKo5Q8QNz", #wallet23
    # "ckbzz9ntUJj4mx3j75nAss3CzvCGXASnYTejDexmfC7k6f4XLqsMJUKN7i84SEz6CTR9LM4ggBMRUgXBHhAtUAgtCvWzv8dGjPr"  #wallet22
    # "ckbzzAkpo6cY3hRGrVhyYFNaH9uowjUDhVwN2APDo8TRjWsBewnM39i5MXxJmnDAJkbYFVA6rxMAuTSACbZbAMwT5FzK3sQnLro",  # wallet7
    # "ckbzz7dYVt6T4sBWhjp8wqQUMgoE8hWyfFCcBjjdLrzEdJU9SQsXjm73rb4VzZt7RxGzuLCAs4ZtQQMJzeELHP841TbYDt4Rm9V"  wal6
    #  ckbzzBUC8KrZduCS9svqE7B1FvqBCpV2CBqkrLtqn6JmFHF9qQXyiE1Xf1aTd9YT6nbfqwZAhr5inGZVjZcdVVzSHPthTWMeNpV  kribbz_b
    #  ckbzz7nUJw9KX3ky4JFa168Qu7PSoiwfqCDczt4BJo7CZHk7UmPWcDkhnfTUZZPvXpRhHDAHUtJe7hjuoZAeseXb6TnCC27gLad  kribbz2

    tx_id = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#    r2 = transfer_coin(amnt=0.00000001, dst = "ckbzz6v3RFwV3s5je4PzcDGTZdsHy5Dg13dCrXwYDctYQi1UXYd3jVDPAfNHJmrSxx4TvMnh1pVUUNudRrqXEL7D46nY8D4Virp" , transactionId = tx_id)
    r2 = transfer_coin(amnt=3.3300000, dst = "ckbzz9ntUJj4mx3j75nAss3CzvCGXASnYTejDexmfC7k6f4XLqsMJUKN7i84SEz6CTR9LM4ggBMRUgXBHhAtUAgtCvWzv8dGjPr", wal_name = "kribbz2" , transactionId = tx_id, fee=100000)  #wallet22

#    r2 = transfer_coin(amnt=1500000., dst = "ckbzz7nUJw9KX3ky4JFa168Qu7PSoiwfqCDczt4BJo7CZHk7UmPWcDkhnfTUZZPvXpRhHDAHUtJe7hjuoZAeseXb6TnCC27gLad", transactionId = tx_id, fee=20000 )  #kribbz2
    print (r2)


#    r3 = transfer_coin(amnt=0.00000001, dst = "ckbzzAbqtqhcrN89awPysMBjQLZwAsVvGC8yFaa5hJ1E6cY6oHEsJyY6rjLCuXWRc1dWCXZSCecGMWUPYrpJPHYP9LkKo5Q8QNz" )
#    print (r3)
#
#    r4 = transfer_coin(amnt=0.00000001, dst = "ckbzz9ntUJj4mx3j75nAss3CzvCGXASnYTejDexmfC7k6f4XLqsMJUKN7i84SEz6CTR9LM4ggBMRUgXBHhAtUAgtCvWzv8dGjPr" )
#    print (r4)
#
#    r5 = transfer_coin(amnt=0.00000001, dst = "ckbzzAkpo6cY3hRGrVhyYFNaH9uowjUDhVwN2APDo8TRjWsBewnM39i5MXxJmnDAJkbYFVA6rxMAuTSACbZbAMwT5FzK3sQnLro" )
#    print (r5)
#
#    r6 = transfer_coin(amnt=0.00000001, dst = "ckbzz7dYVt6T4sBWhjp8wqQUMgoE8hWyfFCcBjjdLrzEdJU9SQsXjm73rb4VzZt7RxGzuLCAs4ZtQQMJzeELHP841TbYDt4Rm9V" )
#    print (r6)


#    run_folder="/home/alex/devel/Blockchain/kribbz_v1/build/"  # "./"
#    pwd = "Password12345"
#    wallet = "wallet6"
#
#    from subprocess import Popen, PIPE
#    from tempfile import SpooledTemporaryFile as tempfile
#    f = tempfile()
#    f.write('exit\n')
#    f.seek(0)
#
#    cmd1 = "{0}simple_wallet".format(run_folder)
#    cmd2 = "--wallet-file {0}".format(wallet)
#    cmd3 = "--password={0}".format(pwd)
#    cmd4 = "--rpc-bind-port 18082"
#
#    prx =  Popen([cmd1,cmd2,cmd3,cmd4],stdout=PIPE,stdin=f)
#
#    out =  prx.stdout.read()
#    print (out)
#    f.close()
