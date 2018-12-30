#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  Get balance

"""
import requests
import json
from kribbz_emu import get_balance

if __name__ == "__main__":
    r1 = get_balance("wallet22")
    print ("wallet22 = " + str(r1["result"]))

    r2 = get_balance("wallet23")
    print ("wallet23 = " + str(r2["result"]))

    r2 = get_balance("wallet24")
    print ("wallet24 = " + str(r2["result"]))

    r2 = get_balance("wallet7")
    print ("wallet7 = " + str(r2["result"]) )

    r2 = get_balance("wal5")
    print ("wal5 = " + str(r2["result"]) )

    r2 = get_balance("wal6")
    print ("wal6 = " + str(r2["result"]) )

    r2 = get_balance("walletK1")
    print ("walletK1 = " + str(r2["result"]) )

    r2 = get_balance("walletK2")
    print ("walletK2 = " + str(r2["result"]) )

    r2 = get_balance("kribbz2")
    print ("kribbz2 = " + str(r2["result"]) )

    r2 = get_balance("kribbz_wallet")
    print ("kribbz_wallet = " + str( r2["result"]) )


