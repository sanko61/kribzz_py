#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""Kribbz python module
   send commands to wallet
"""

import json


DBTIME_FMT = "%Y-%m-%d %H:%M:%S"

ERRORS = {
    1: "Error: non correct format",
    2: "Error: no DB connection",
    3: "Error: DB error",
    4: "Error: non correct password",
    5: "kill process error ",
}

# simple wallet is running on the localhost and port of 18082
WALLET_URL = "http://localhost:18082/json_rpc"


from bottle import Bottle, run, request, server_names, ServerAdapter, HTTPError, route, static_file
import requests
import sqlite3
import datetime
import time
import thread
import sys
import Queue
import os
import signal
from check_process import *

server = None

def psi_log_debug(msg):
    """
    Write debug log

    Args:
         msg (str):  message.
    """
    print ('(debug):', msg)

def psi_log_info(msg):
    """
    Write info log

    Args:
         msg (str):  message.
    """
    print( '(Info):', msg)

def psi_log_error(msg):
    """
    Write error log

    Args:
         msg (str):  message.
    """
    print ('(Error):', msg)


def encode_dict(map):
    """encode_dict to UTF-8

    """
    return dict([(key, val.encode('utf-8')) for key, val in map.items()
                 if isinstance(val, basestring)])


def parse_request(section):
    """parse_request
    :raise:
        :HTTPError: a probleme occured
                      and it can't be passed
    """
    #LOG
    try:
        p = request.POST.dict.keys()[0]
        return json.loads(p)[section]
    except:
        raise HTTPError(403, 1)


class MySSLCherryPy(ServerAdapter):
    """
    Server CherryPyis used
    """

    def run(self, handler):
        """
        Run server
        """
        try:
            from cheroot.wsgi import Server as WSGIServer
        except ImportError:
            from cherrypy.wsgiserver import CherryPyWSGIServer as WSGIServer

        global server
        # server = wsgiserver.CherryPyWSGIServer((self.host, self.port), handler)
        server = WSGIServer((self.host, self.port), handler)
        #        cert = 'server.pem' # certificate path
        #        server.ssl_certificate = cert
        #        server.ssl_private_key = cert

        try:
            server.start()
        finally:
            server.stop()


t_loop = None
server_names['mysslcherrypy'] = MySSLCherryPy
app = Bottle()


# Errors
@app.error(404)
def error404(error):
    """
    Error 404 respons
    """
    return 'Nothing here, sorry'


@app.error(403)
def error403(error):
    """
    Error 403 respons
        {
            "error_no": number,
            "dsc": string
        }
    """
    response = {"err_no": error.output, "dsc": ERRORS[error.output]}
    return json.dumps(response)


@app.route("/error")
def error():
    """
    Error respons
    """
    raise HTTPError(403, 2)


@app.post("/transfer_coin")
def transfer_coin():
    """
    transfer money
    Arg:
        {"kribzz":
            {"transactionId":"643427363","streeAddress":"700 Rodeo Drive","cityName":"Beverly Hills",
            "stateCode":"CA","zipCode":"90210","latitude":"34.079678","longitude":"-118.413515",
            "transactionDateTime":"1523855778",
            "transactionTotal":"9975000.00",
            "sellerName":"John Clark",
            "buyerName":"Emily Stevens",
            "wallet":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
            }
        }
    Return:
       reply(JSON) {"reply":
                 {"msgId":cursor.lastrowid,"error":{"errorCode":PSI.errorCode,"errorMessage":PSI.errorMessage}}
    }
    """

    psi_log_info(request.url)
    psi_log_info("POST: %s" % request.POST.dict)
    try:
        query_data = parse_request("kribzz")
        for key,val in query_data.items():
            d = query_data[key]
            psi_log_debug( str(d) + ' = ' + str(val))
    except Exception as errtxt:
        psi_log_error(str(errtxt))
        pass
    reply = {"reply":
                 {"error": {"errorCode": 0, "errorMessage": None}}
    }
    psi_log_debug(reply)
    return json.dumps(reply)


@app.post("/get_balance")
def get_balance():

    # simple wallet is running on the localhost and port of 18082
    url = WALLET_URL
    # standard json header
    headers = {'content-type': 'application/json'}
    # simplewallet' procedure/method to call
    rpc_input = {
        "method": "getbalance"
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
    return (json.dumps(response.json()))


@app.post("/incoming_transfers")
def incoming_transfers():

    # simple wallet is running on the localhost and port of 18082
    url = WALLET_URL  # "http://localhost:18082/json_rpc"

    # standard json header
    headers = {'content-type': 'application/json'}

    # simplewallet' procedure/method to call
    rpc_input = {
        "method": "incoming_transfers",
        "params": {"transfer_type": "all"}
    }

    # add standard rpc values
    rpc_input.update({"jsonrpc": "2.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers)

    # make json dict with response
    response_json = response.json()

    # amounts in cryptonote are encoded in a way which is convenient
    # for a computer, not a user. Thus, its better need to recode them
    # to something user friendly, before displaying them.
    #
    # For examples:
    # 4760000000000 is 4.76
    # 80000000000   is 0.08
    #
    if "result" in response_json:
        if "transfers" in response_json["result"]:
            for transfer in response_json["result"]["transfers"]:
                transfer["amount"] = float(get_money(str(transfer["amount"])))


    # pretty print json output
    print(json.dumps(response_json, indent=4))
    return (json.dumps(response.json()))


def get_money(amount):
    """decode cryptonote amount format to user friendly format. Hope its correct.

    Based on C++ code:
    https://github.com/monero-project/bitmonero/blob/master/src/cryptonote_core/cryptonote_format_utils.cpp#L751
    """

    CRYPTONOTE_DISPLAY_DECIMAL_POINT = 12

    s = amount

    if len(s) < CRYPTONOTE_DISPLAY_DECIMAL_POINT + 1:
        # add some trailing zeros, if needed, to have constant width
        s = '0' * (CRYPTONOTE_DISPLAY_DECIMAL_POINT + 1 - len(s)) + s

    idx = len(s) - CRYPTONOTE_DISPLAY_DECIMAL_POINT

    s = s[0:idx] + "." + s[idx:]

    return s



@app.post("/version")
def version():
    """
    Get version

    Arg:  No

    Return:
        reply = {reply':
        {'version': '0.1.0105'}
        }

    """
    psi_log_info(request.url)
    psi_log_info("POST: %s" % request.POST.dict)

    reply = {"reply":
                 {"version": "1.0.0001" }
    }
    psi_log_info(reply)
    return json.dumps(reply)


@app.route('/hello/:name')
def index(name='World'):
    """
    test URL
    """
    return '<b>Hello %s!</b>' % name


def signal_handler(signal, frame):
    """
    Ctr-C handler
    """
    psi_log_info('You pressed Ctrl+C! Stop application.')
    exit(0)



if __name__ == '__main__':

    """Check exist process
    """

    #check pid file  / server exist
    pid = str(os.getpid())
    #    pidfile = os.path.join("/", "tmp", __file__+".pid")
    pidfile = '/tmp/' + os.path.basename(__file__).split('.')[0] + '.pid'

    if os.path.isfile(pidfile) and checkPidRunning(int(file(pidfile, 'r').readlines()[0])):
        print "%s already exists, exiting" % pidfile
        sys.exit()
    else:
        file(pidfile, 'w').write(pid)


    # Set signal handler
    signal.signal(signal.SIGINT, signal_handler)


    run(app, host='0.0.0.0', port='8804', server='mysslcherrypy')

    os.unlink(pidfile)
    psi_log_debug("finish process %s" % pidfile)
