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

    kribbz = \
    {
        "transactionId":tx_id, "streeAddress":"700 Rodeo Drive", "cityName":"Beverly Hills",
        "stateCode":"CA","zipCode":"90210","latitude":"34.079678","longitude":"-118.413515",
        "transactionDateTime":"1523855778",
        "transactionTotal":"9975000.00",
        "sellerName":"John Clark",
        "buyerName":"Emily Stevens",
        "agent_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
        "agent_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
        "investor_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
        "investor_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
        "owner_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
        "owner_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
    }
    transfer ={
    "amount": 0.5,
        "destination_address": "ckbzz6v3RFwV3s5je4PzcDGTZdsHy5Dg13dCrXwYDctYQi1UXYd3jVDPAfNHJmrSxx4TvMnh1pVUUNudRrqXEL7D46nY8D4Virp",  # wallet24
                    # "ckbzz6v3RFwV3s5je4PzcDGTZdsHy5Dg13dCrXwYDctYQi1UXYd3jVDPAfNHJmrSxx4TvMnh1pVUUNudRrqXEL7D46nY8D4Virp",  # wallet24
                    #  "ckbzzAbqtqhcrN89awPysMBjQLZwAsVvGC8yFaa5hJ1E6cY6oHEsJyY6rjLCuXWRc1dWCXZSCecGMWUPYrpJPHYP9LkKo5Q8QNz", #wallet23
                    # "ckbzz9ntUJj4mx3j75nAss3CzvCGXASnYTejDexmfC7k6f4XLqsMJUKN7i84SEz6CTR9LM4ggBMRUgXBHhAtUAgtCvWzv8dGjPr"  #wallet22
                    # "ckbzzAkpo6cY3hRGrVhyYFNaH9uowjUDhVwN2APDo8TRjWsBewnM39i5MXxJmnDAJkbYFVA6rxMAuTSACbZbAMwT5FzK3sQnLro",  # wallet7
                    # "ckbzz9ntUJj4mx3j75nAss3CzvCGXASnYTejDexmfC7k6f4XLqsMJUKN7i84SEz6CTR9LM4ggBMRUgXBHhAtUAgtCvWzv8dGjPr"
                    # "ckbzz7dYVt6T4sBWhjp8wqQUMgoE8hWyfFCcBjjdLrzEdJU9SQsXjm73rb4VzZt7RxGzuLCAs4ZtQQMJzeELHP841TbYDt4Rm9V"  wal6
        "fee": 0100000,
    }

    r2 = transfer_full(transfer, kribbz, wal_name = "kribbz2" )
#    r2 = transfer_full(transfer, kribbz={}, wal_name = "kribbz2" )
#    r2 = transfer_full(transfer, kribbz=None, wal_name = "kribbz2" )

    print (r2)

