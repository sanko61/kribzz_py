#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  Get balance

"""
import requests
import json
from kribbz_emu import get_balance

if __name__ == "__main__":
    r1 = get_balance()
    print (r1)
