#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  get_payments
"""

import requests
import json
import datetime
from kribbz_emu import transfer_full

if __name__ == "__main__":

    tx_id = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    r2 = transfer_full(amnt=11.1111,
        dst="ckbzz6v3RFwV3s5je4PzcDGTZdsHy5Dg13dCrXwYDctYQi1UXYd3jVDPAfNHJmrSxx4TvMnh1pVUUNudRrqXEL7D46nY8D4Virp",
        wal_name = "kribbz2", pwd="Password12345", transactionId = tx_id, fee=100000, mixin=0,
        st_address="700 Rodeo Drive", cityName ="Beverly Hills", stateCode="CA", zipCode="90210",
        latitude="34.079678", longitude ="-118.413515",
        transactionDateTime ="1523855778", transactionTotal = "9975000.00",
        sellerName="John Clark", buyerName="Emily Stevens")

#    r2 = transfer_full(transfer, kribbz, wal_name = "kribbz2" )
#    r2 = transfer_full(transfer, kribbz={}, wal_name = "kribbz2" )
#    r2 = transfer_full(transfer, kribbz=None, wal_name = "kribbz2" )
    print (r2)

