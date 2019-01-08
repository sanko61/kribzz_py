#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  get_payments
"""

import requests
import json
from kribbz_emu import search_kribbz

if __name__ == "__main__":
#    print ("wallet22:==========================================================================")
#    r1 = search_kribbz(w_name="wallet22", pwd="Password12345", stateCode="CA", zipCode="90210" )
#    print (r1)

#    print ("wallet23:==========================================================================")
#    r1 = search_kribbz(w_name="wallet23", pwd="Password12345", stateCode="CA", zipCode="90210" )
#    print (r1)

    print ("wallet24:==========================================================================")
    r1 = search_kribbz(w_name="wallet24", pwd="Password12345", stateCode="CA", zipCode="90210" )
    print (r1)


    print ("kribbz2:==========================================================================")
    r1 = search_kribbz(w_name="kribbz2", pwd="Password12345", stateCode="CA", zipCode="90210" )
    print (r1)
