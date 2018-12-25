#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  Get balance

"""
import requests
import json
from kribbz_emu import get_trans

if __name__ == "__main__":

    print("trx f1706bd00d241844109bd824c013e4fb1a99f88b53d449c7b919ba6e9a3b3eac==================")
    r= get_trans(txs_hash = "f1706bd00d241844109bd824c013e4fb1a99f88b53d449c7b919ba6e9a3b3eac")
    print (r)

    print("trx 4e5fa2439ce317be2af025f887a773d962c9dd76bc5a5442cdf7a8715ab37543==================")
    r= get_trans(txs_hash = "4e5fa2439ce317be2af025f887a773d962c9dd76bc5a5442cdf7a8715ab37543")
    print (r)

    print("trx ea4eb811ed01b805e6f6e1081c8c37f23c46cff7bbbd125e8609605a503fb70a==================")
    r= get_trans(txs_hash = "ea4eb811ed01b805e6f6e1081c8c37f23c46cff7bbbd125e8609605a503fb70a")
    print (r)

    print("trx 542f3fd3fb1bbff306a09eaabc1bca1298005dc6d606e88d6e1cfd9df490eb92==================")
    r= get_trans(txs_hash = "542f3fd3fb1bbff306a09eaabc1bca1298005dc6d606e88d6e1cfd9df490eb92")
    print (r)

    print("trx 542f3fd3fb1bbff306a09eaabc1bca1298005dc6d606e88d6e1cfd9df490eb92==================")
    r= get_trans(txs_hash = "542f3fd3fb1bbff306a09eaabc1bca1298005dc6d606e88d6e1cfd9df490eb92")
    print (r)

