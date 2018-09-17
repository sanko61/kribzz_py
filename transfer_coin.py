#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  get_payments
"""

import requests
import json
from kribbz_emu import transfer_coin

if __name__ == "__main__":
    r1 = transfer_coin()
    print (r1)


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
