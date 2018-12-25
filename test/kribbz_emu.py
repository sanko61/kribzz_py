#!/usr/bin/env python
#-*- coding:utf-8 -*-

""" Send JSON request to emercom generator

"""
import json
import requests
#import requests0 as requests
import base64
import sqlite3
import datetime
import time
import thread
import os
import binascii

#HOST = "http://localhost"
HOST = "http://ec2-52-13-195-226.us-west-2.compute.amazonaws.com"
#HOST = "http://52.13.195.226"
PORT = "8804"


class Exception403(Exception):
    pass


def post(action, data):
    """Send POST request to server HOST PORT.

      Args:
         action (str):  URL name.
         data  (dict):  JSON data.

      Returns:
         dict.  The JSON response

      Raises:
         Exception403

   .. note::

       Module requests0  is used instead of request.
      """

    url = "%s:%s/%s" % (HOST, PORT, action)
    args = {json.dumps(data): ""}
    r = requests.post(url, data=args, verify=False)
    if r.status_code == 200:
        return r.json()
    else:
        print r.text
        raise Exception403(r.json()['dsc'].encode("utf8"))


def get(action):
    """
    Send GET request to server.

      Args:
         action (str):  URL name.

      Returns:
         dict.  The JSON response

      Raises: Exception403

    """
    url = "%s:%s/%s" % (HOST, PORT, action)
    r = requests.get(url, verify=False)
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception403(r.json['dsc'].encode("utf8"))


def transfer_coin():
    """Send message (type=0,PES version).

      Returns:
         dict.  The JSON response ::
      """
    rep = post('transfer_coin',
        { "kribbz": {
            "transactionId":"643427363", "streeAddress":"700 Rodeo Drive", "cityName":"Beverly Hills",
            "stateCode":"CA","zipCode":"90210","latitude":"34.079678","longitude":"-118.413515",
            "transactionDateTime":"1523855778",
            "transactionTotal":"9975000.00",
            "sellerName":"John Clark",
            "buyerName":"Emily Stevens",
        },
          "transfer": {
              "amount":22.2222,
#              "destination_address":"ckbzz7dYVt6T4sBWhjp8wqQUMgoE8hWyfFCcBjjdLrzEdJU9SQsXjm73rb4VzZt7RxGzuLCAs4ZtQQMJzeELHP841TbYDt4Rm9V",
              "destination_address": "ckbzz6v3RFwV3s5je4PzcDGTZdsHy5Dg13dCrXwYDctYQi1UXYd3jVDPAfNHJmrSxx4TvMnh1pVUUNudRrqXEL7D46nY8D4Virp", #wallet24
             # "ckbzz6v3RFwV3s5je4PzcDGTZdsHy5Dg13dCrXwYDctYQi1UXYd3jVDPAfNHJmrSxx4TvMnh1pVUUNudRrqXEL7D46nY8D4Virp",
             #  "ckbzzAbqtqhcrN89awPysMBjQLZwAsVvGC8yFaa5hJ1E6cY6oHEsJyY6rjLCuXWRc1dWCXZSCecGMWUPYrpJPHYP9LkKo5Q8QNz", #wallet23
             # "ckbzz9ntUJj4mx3j75nAss3CzvCGXASnYTejDexmfC7k6f4XLqsMJUKN7i84SEz6CTR9LM4ggBMRUgXBHhAtUAgtCvWzv8dGjPr"  #wallet22
             # "ckbzzAkpo6cY3hRGrVhyYFNaH9uowjUDhVwN2APDo8TRjWsBewnM39i5MXxJmnDAJkbYFVA6rxMAuTSACbZbAMwT5FzK3sQnLro",  # wallet7
             # "ckbzz9ntUJj4mx3j75nAss3CzvCGXASnYTejDexmfC7k6f4XLqsMJUKN7i84SEz6CTR9LM4ggBMRUgXBHhAtUAgtCvWzv8dGjPr"
             # "ckbzz7dYVt6T4sBWhjp8wqQUMgoE8hWyfFCcBjjdLrzEdJU9SQsXjm73rb4VzZt7RxGzuLCAs4ZtQQMJzeELHP841TbYDt4Rm9V"  wal6

              },
          "smart_contract": {
              "agent_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
              "agent_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
              "investor_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
              "investor_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
              "owner_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
              "owner_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
              },
          "wallet":
              {
                  "password":"Password12345",
                  "wallet_name":"kribbz_wallet",
                  },
        },
    )
    return rep


def get_balance(w_name="wal22", pwd="Password12345"):
    rep = post('get_balance',
        {"wallet":
             {
                 "password":pwd,
#                 "wallet_name":"wal6",
                 "wallet_name":w_name,
                 }
        },
    )
    return rep


def get_transfers():
    rep = post('get_transfers',
        {"wallet":
             {"password":"Password12345","wallet_name":"wallet22",}},  # "wallet7"
    )
    return rep


def search_kribbz():
    rep = post('search_kribbz',
        {"wallet":
             {"password":"Password12345","wallet_name":"wallet7",},  # "wallet7"
        "filter":
             {"stateCode":"CA", "zipCode":"90210"}},
    )
    return rep


def get_payments():
    rep = post('get_payments',{}, )
    return rep


def create_address():
#     curl  -H "Content-Type: application/json" --request POST -d '{"wallet":{ "password":"Password12345","wallet_name":"wallet7"}}' "http://52.13.195.226:8804/create_address"

    rep = post('create_address',
        {"wallet":
             {
                "password":"Password12345",
                "wallet_name":"wallet7",
             }
        },
    )

    return rep


def delete_address():
    rep = post('delete_address',{}, )
    return rep


if __name__ == "__main__":
#    random_32_bytes = os.urandom(32)
#    tt1 = binascii.hexlify(random_32_bytes)
#    tt2 = map(chr,tt1)
#    payment_id = "".join(map(chr, binascii.hexlify(random_32_bytes)))
#    payment_id = tt1


#    r = transfer_coin()
#    print(r)

#    r1 = get_balance()
#    print (r1)
#
#    r2 = get_payments()
#    print (r2)

#    r = delete_address()
#    print(r)

    r= create_address()
    print (r)

    pass
