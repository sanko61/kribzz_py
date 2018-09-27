#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""  Get balance

"""
import requests
import json

def main():

    # simple wallet is running on the localhost and port of 18082
#    url = "http://localhost:18082/json_rpc"
    url = "http://localhost:8070/json_rpc"

    # standard json header
    headers = {'content-type': 'application/json'}

    # simplewallet' procedure/method to call
    rpc_input = {
#        "method": "getBalance"
#        "method": "reset"
#        "method": "createAddress",
        "method": "deleteAddress",
        "params": {"address": "ckbzzBEWU9rPs5Ak8peR79UGib1Krc4usjFLvEKfzRaa17EWCGCHSrqDQn1gi1ut2xf2vNJivQmkfXPTdPWEGyZi9JD6GyG1AdQ",
        },
    }


    # add standard rpc values
    rpc_input.update({"jsonrpc": "2.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers)

    # amounts in cryptonote are encoded in a way which is convenient
    # for a computer, not a user. Thus, its better need to recode them
    # to something user friendly, before displaying them.
    #
    # For examples:
    # 4760000000000 is 4.76
    # 80000000000   is 0.08
    #
    # In example 3 "Basic example 3: get incoming transfers" it is
    # shown how to convert cryptonote values to user friendly format.

    # pretty print json output
    print(json.dumps(response.json(), indent=4))

if __name__ == "__main__":
    main()