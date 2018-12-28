#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  Get balance

"""
import requests
import json
from kribbz_emu import get_blockcount

if __name__ == "__main__":

    r= get_blockcount()
    print (r)

