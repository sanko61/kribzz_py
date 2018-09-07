#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  get_payments
"""

import requests
import json
from kribbz_emu import get_transfers

if __name__ == "__main__":
    r1 = get_transfers()
    print (r1)
