#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  Get mining status

"""

import requests
import json

def main():

    # bitmonerod' is running on the localhost and port of 18081
#    url = "http://localhost:18081/mining_status"
    url = "http://localhost:8070/mining_status"

    # standard json header
    headers = {'content-type': 'application/json'}

    # execute the rpc request
    response = requests.post(
        url,
        headers=headers)

    # pretty print json output
    print(json.dumps(response.json(), indent=4))

if __name__ == "__main__":
    main()