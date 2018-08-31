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
