#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  Get balance

"""
import requests
import json
from kribbz_emu import create_address
import os
import time

if __name__ == "__main__":
#    r1 = create_address()
#    print (r1)
#    { "getbalance", makeMemberMethod(&wallet_rpc_server::on_getbalance) },
#    { "transfer", makeMemberMethod(&wallet_rpc_server::on_transfer) },
#    { "store", makeMemberMethod(&wallet_rpc_server::on_store) },
#    { "stop_wallet" , makeMemberMethod(&wallet_rpc_server::on_stop_wallet) },
#    { "get_payments", makeMemberMethod(&wallet_rpc_server::on_get_payments) },
#    { "get_transfers", makeMemberMethod(&wallet_rpc_server::on_get_transfers) },
#    //{ "get_transaction", makeMemberMethod(&wallet_rpc_server::on_get_transaction) },
#    { "get_height", makeMemberMethod(&wallet_rpc_server::on_get_height) },
#    { "get_address", makeMemberMethod(&wallet_rpc_server::on_get_address) },
#    { "query_key" , makeMemberMethod(&wallet_rpc_server::on_query_key) },
#    { "reset", makeMemberMethod(&wallet_rpc_server::on_reset) },
#    { "get_paymentid" , makeMemberMethod(&wallet_rpc_server::on_gen_paymentid) },



    APP_FOLDER="/home/alex/devel/Blockchain/kribbz_v1/build/"  # "./"
    WALLET_URL = "http://localhost:18082/json_rpc"
    run_folder="/home/alex/devel/Blockchain/kribbz_v1/build/"  # "./"
    pwd = "Password12345"
    wallet = "wallet6"
    cmd = "{0}simple_wallet  --password={1} --generate-new-wallet /opt/kribbz/{2}".format(run_folder, pwd, wallet)
#    code = os.system(cmd)
#    print (code)


#    import sys
#    from subprocess import *
#    proc = Popen(cmd, shell=True, stdout=PIPE)
#    while True:
#        data = proc.stdout.readline()   # Alternatively proc.stdout.read(1024)
#        if len(data) == 0:
#            break
#        sys.stdout.write(data)   # sys.stdout.buffer.write(data) on Python 3.x

#    from subprocess import Popen, PIPE, STDOUT
#
##    p = Popen(['grep', 'f'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
#    p = Popen([cmd], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
#    grep_stdout = p.communicate(input=b'one\ntwo\nthree\nfour\nfive\nsix\n')[0]
#    print(grep_stdout.decode())
#    # -> four
#    # -> five
#    # ->


#    from subprocess import Popen, PIPE
#    from tempfile import SpooledTemporaryFile as tempfile
#    f = tempfile()
#    f.write('exit\n')
#    f.seek(0)
##    print Popen(['/bin/grep','f'],stdout=PIPE,stdin=f).stdout.read()
#
#    cmd1 = "{0}simple_wallet".format(run_folder)
#    cmd2 = "--password={0}".format(pwd, wallet)
#    cmd3 = "--generate-new-wallet"
#    cmd4 = "/opt/kribbz/{0}".format(wallet)
#
#    out =  Popen([cmd1,cmd2,cmd3,cmd4],stdout=PIPE,stdin=f).stdout.read()
#    print (out)
#    f.close()
#
#    WALLET_FOLDER = "/opt/kribbz/"
#    import os.path
#    fname = "{0}{1}.address".format(WALLET_FOLDER ,wallet)
#
#    #    if os.path.isfile(fname):
#    #        address = None
#
#    try:
#        with open(fname) as f:
#            address = f.readline()
#            # you may also want to remove whitespace characters like `\n` at the end of each line
#        address = address.strip()
#    except :
#        address = None
#
#    rez = {"address": address, "msg": out}
#

    #    run_wallet(wallet, pwd)
    from subprocess import Popen, PIPE
    from tempfile import SpooledTemporaryFile as tempfile
    f = tempfile()
    f.write('exit\n')
    f.seek(0)

    # Start wallet
    #    print Popen(['/bin/grep','f'],stdout=PIPE,stdin=f).stdout.read()
    #./simple_wallet  --wallet-file ./wal2 --password Vatson2008  --rpc-bind-port 18082
    run_folder= APP_FOLDER
    cmd1 = "{0}simple_wallet".format(run_folder)
    cmd2 = "--wallet-file {0}".format(wallet)
    cmd3 = "--password={0}".format(pwd)
    cmd4 = "--rpc-bind-port 18082"
    prx =  Popen([cmd1,cmd2,cmd3,cmd4],stdout=PIPE,stdin=f)
    print("Wallet started OK")

    time.sleep(15)

    out = prx.stdout.read()
    print (out)

    f.close()
