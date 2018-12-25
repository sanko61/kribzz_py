#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  Get balance

"""
import requests
import json
from kribbz_emu import get_balance

if __name__ == "__main__":
    r1 = get_balance("wal22")
    print ("wal22 = " + r1["result"])

    r2 = get_balance("wal23")
    print ("wal23 = " + r1["result"])

    r2 = get_balance("wal24")
    print ("wal24 = " + r1["result"])

    r2 = get_balance("wallet7")
    print ("wallet7 = " + r1["result"])

    r2 = get_balance("kribbz_wallet")
    print ("wal23 = " + r1["result"])
