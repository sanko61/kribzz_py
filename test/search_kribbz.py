#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  get_payments
"""

import requests
import json
from kribbz_emu import search_kribbz

if __name__ == "__main__":
    r1 = search_kribbz()
    print (r1)
