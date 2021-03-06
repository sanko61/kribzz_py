#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  get_payments
"""

import requests
import json
import time
from kribbz_emu import search_kribbz, search_by_filter

if __name__ == "__main__":
#    print ("wallet22:==========================================================================")
#    r1 = search_kribbz(w_name="wallet22", pwd="Password12345", stateCode="CA", zipCode="90210" )
#    print (r1)

#    print ("wallet23:==========================================================================")
#    r1 = search_kribbz(w_name="wallet23", pwd="Password12345", stateCode="CA", zipCode="90210" )
#    print (r1)

    kr = { "streeAddress":"700 Rodeo Drive"}
    s_kr = json.dumps (kr)
    print(s_kr)

    print ("wallet24:==========================================================================")
    r1 = search_kribbz(w_name="wallet24", pwd="Password12345", stateCode="CA", zipCode="90210" )
    print (r1)
    print ("cnt=", r1["cnt"])
    transfers = r1['transfers']
    ii = 0
    for tr in transfers:
        print(ii, tr["fee"], tr["time"], tr["transactionHash"], tr[ "amount"], tr["output"])
        ii += 1



    print ("kribbz2:==========================================================================")
    r1 = search_kribbz(w_name="kribbz2", pwd="Password12345", stateCode="CA", zipCode="90210" )
    print (r1)
    print ("cnt=", r1["cnt"])

    time.sleep(2)
    print ("kribbz2:==========================================================================")
    r1 = search_kribbz(w_name="kribbz2", pwd="Password12345", stateCode="CA", zipCode="90210" )
    print (r1)
    print ("cnt=", r1["cnt"])

    time.sleep(2)
    print ("==========================================================================")
    r2 = search_by_filter(w_name="wallet24", pwd="Password12345", filter={ "streeAddress":"700RodeoDrive"})
    print(r2)
    print ("cnt=", r2["cnt"])

    time.sleep(2)
    print ("==========================================================================")
    r2 = search_by_filter(w_name="wallet24", pwd="Password12345", filter={ "streeAddress":"700RodeoDrive", "cityName":"BeverlyHills"})
    print(r2)
    print ("cnt=", r2["cnt"])

    time.sleep(2)
    print ("==========================================================================")
    r2 = search_by_filter(w_name="wallet24", pwd="Password12345", filter={ "streeAddress":"700RodeoDrive", "cityName":"BeverlyHills", "latitude":"34.079678"})
    print(r2)
    print ("cnt=", r2["cnt"])

    time.sleep(2)
    print ("==========================================================================")
    r2 = search_by_filter(w_name="wallet24", pwd="Password12345", filter={ "streeAddress":"700RodeoDrive", "cityName":"BeverlyHills", "latitude":"34.079678", "longitude":"-118.413515"})
    print(r2)
    print ("cnt=", r2["cnt"])

    time.sleep(2)
    print ("==========================================================================")
    r2 = search_by_filter(w_name="wallet24", pwd="Password12345", filter={ "streeAddress":"700RodeoDrive", "cityName":"BeverlyHills", "latitude":"34.079678", "longitude":"-118.413515", "transactionDateTime":"1523855778"})
    print(r2)
    print ("cnt=", r2["cnt"])

    time.sleep(2)
    print ("==========================================================================")
    r2 = search_by_filter(w_name="wallet24", pwd="Password12345",
        filter={ "streeAddress":"700RodeoDrive", "cityName":"BeverlyHills", "latitude":"34.079678", "longitude":"-118.413515",
                 "transactionDateTime":"1523855778", "transactionTotal":"9975000.00", "sellerName":"JohnClark", "buyerName":"EmilyStevens"
        })
    print(r2)
    print ("cnt=", r2["cnt"])


    time.sleep(2)
    print ("==========================================================================")
    r2 = search_by_filter(w_name="wallet24", pwd="Password12345",
        filter={ "streeAddress":"700RodeoDrive", "cityName":"BeverlyHills", "latitude":"34.079678", "longitude":"-118.413515",
                 "transactionDateTime":"1523855778", "transactionTotal":"9975000.00", "sellerName":"JohnClark", "buyerName":"EmilyStevens",
                 "agent_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 "agent_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
        })
    print(r2)
    print ("cnt=", r2["cnt"])

    time.sleep(2)
    print ("==========================================================================")
    r2 = search_by_filter(w_name="wallet24", pwd="Password12345",
        filter={ "streeAddress":"700RodeoDrive", "cityName":"BeverlyHills", "latitude":"34.079678", "longitude":"-118.413515",
                 "transactionDateTime":"1523855778", "transactionTotal":"9975000.00", "sellerName":"JohnClark", "buyerName":"EmilyStevens",
                 "agent_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 "agent_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 "investor_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 "investor_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 })
    print(r2)
    print ("cnt=", r2["cnt"])

    time.sleep(2)
    print ("==========================================================================")
    r2 = search_by_filter(w_name="wallet24", pwd="Password12345",
        filter={ "streeAddress":"700RodeoDrive", "cityName":"BeverlyHills", "latitude":"34.079678", "longitude":"-118.413515",
                 "transactionDateTime":"1523855778", "transactionTotal":"9975000.00", "sellerName":"JohnClark", "buyerName":"EmilyStevens",
                 "agent_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 "agent_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 "investor_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 "investor_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 "owner_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 "owner_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 })
    print(r2)
    print ("cnt=", r2["cnt"])

    time.sleep(2)
    print ("==========================================================================")
    r2 = search_by_filter(w_name="kribbz2", pwd="Password12345",
        filter={ "streeAddress":"700RodeoDrive", "cityName":"BeverlyHills", "latitude":"34.079678", "longitude":"-118.413515",
                 "transactionDateTime":"1523855778", "transactionTotal":"9975000.00", "sellerName":"JohnClark", "buyerName":"EmilyStevens",
                 "agent_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 "agent_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 "investor_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 "investor_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 "owner_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 "owner_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
                 })
    print(r2)
    print ("cnt=", r2["cnt"])
