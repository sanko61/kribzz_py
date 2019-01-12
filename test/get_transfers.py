#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  get_payments
"""

import requests
import json
from kribbz_emu import get_transfers

if __name__ == "__main__":
    print ("==wallet22========================================")
    r1 = get_transfers(w_name="wallet22", pwd="Password12345")
#    print (r1)
    rez = json.loads(r1['result'])
    try:
        transfers = rez['result']['transfers']
    except   Exception as ex1:
        transfers = None

    rez_output = []
    ii = 0
    if transfers is not None:
        for tr in transfers:
            print(ii, tr["fee"], tr["time"], tr["transactionHash"], tr[ "amount"], tr["output"])
            ii += 1



    #    print ("==wallet23========================================")
#    r1 = get_transfers(w_name="wallet23", pwd="Password12345")
#    print (r1)
#
#    print ("==wallet24========================================")
#    r1 = get_transfers(w_name="wallet24", pwd="Password12345")
#    print (r1)
#
#    print ("==wallet7========================================")
#    r1 = get_transfers(w_name="wallet7", pwd="Password12345")
#    print (r1)
#
#    print ("==kribbz_wallet========================================")
#    r1 = get_transfers(w_name="kribbz_wallet", pwd="Password12345")
#    print (r1)
