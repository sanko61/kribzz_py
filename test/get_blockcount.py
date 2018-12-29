#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  Get balance

"""
import requests
import json
from kribbz_emu import get_blockcount, get_blockhash, get_lastblockheader


if __name__ == "__main__":

    r= get_blockcount()
    print (r)

    r = get_blockhash(21)
    print (r)

    r = get_blockhash(1000)
    print (r)

    r = get_blockhash(2551)
    print (r)

    r = get_blockhash(-1)
    print (r)

    print("==============================================")
    r = get_lastblockheader()
    print (r)

    print("==============================================")
    r = get_lastblockheader()
    print (r)
