#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""Kribbz python module
   send commands to wallet
"""

import json
import os
from multiprocessing import Process, Value, Array

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
CRYPTONOTE_DISPLAY_DECIMAL_POINT = 8

WALLET_FOLDER = "/opt/kribbz/"
APP_FOLDER = "/home/ubuntu/kribbz_v1/build/"  # "/home/alex/devel/Blockchain/kribbz_v1/build/"
__cmd__ = None

DEMON_URL = 'http://127.0.0.1:23926'

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
import binascii

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


def get_amount(amount):
    """encode amount (float number) to the cryptonote format. Hope its correct.

    Based on C++ code:
    https://github.com/monero-project/bitmonero/blob/master/src/cryptonote_core/cryptonote_format_utils.cpp#L211
    """

    str_amount = str(amount)

    fraction_size = 0

    if '.' in str_amount:

        point_index = str_amount.index('.')

        fraction_size = len(str_amount) - point_index - 1

        while fraction_size < CRYPTONOTE_DISPLAY_DECIMAL_POINT and '0' == str_amount[-1]:
            print(44)
            str_amount = str_amount[:-1]
            fraction_size = fraction_size - 1

        if CRYPTONOTE_DISPLAY_DECIMAL_POINT < fraction_size:
            return False

        str_amount = str_amount[:point_index] + str_amount[point_index+1:]

    if not str_amount:
        return False

    if fraction_size < CRYPTONOTE_DISPLAY_DECIMAL_POINT:
        str_amount = str_amount + '0'*(CRYPTONOTE_DISPLAY_DECIMAL_POINT - fraction_size)

    return str_amount


def get_money(amount):
    """decode cryptonote amount format to user friendly format. Hope its correct.

    Based on C++ code:
    https://github.com/monero-project/bitmonero/blob/master/src/cryptonote_core/cryptonote_format_utils.cpp#L751
    """

    s = amount

    if len(s) < CRYPTONOTE_DISPLAY_DECIMAL_POINT + 1:
        # add some trailing zeros, if needed, to have constant width
        s = '0' * (CRYPTONOTE_DISPLAY_DECIMAL_POINT + 1 - len(s)) + s

    idx = len(s) - CRYPTONOTE_DISPLAY_DECIMAL_POINT

    s = s[0:idx] + "." + s[idx:]

    return s

def get_payment_id():
    """generate random payment_id

    generate some random payment_id for the
    transactions

    payment_id is 32 bytes (64 hexadecimal characters)
    thus we first generate 32 random byte array
    which is then change to string representation, since
    json will not not what to do with the byte array.
    """

    random_32_bytes = os.urandom(32)
#    payment_id = "".join(map(chr, binascii.hexlify(random_32_bytes)))
    payment_id = binascii.hexlify(random_32_bytes)
    return payment_id


def proxy_f1():
    global __cmd__
    os.system(__cmd__)


def run_wallet(s_stop):
    global __cmd__
    prx2 = Process(target=proxy_f1, args=())
    prx2.start()
    while(1):
        if (int(s_stop.value) == 1):
            print 'break:'
            break
        time.sleep(0.5)



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


def run_wallet2(wallet = "wallet6", pwd = "Password12345"):
    run_folder="/home/alex/devel/Blockchain/kribbz_v1/build/"  # "./"
#    pwd = "Password12345"
#    wallet = "wallet6"

    from subprocess import Popen, PIPE
    from tempfile import SpooledTemporaryFile as tempfile
    f = tempfile()
    f.write('exit\n')
    f.seek(0)
    #    print Popen(['/bin/grep','f'],stdout=PIPE,stdin=f).stdout.read()
    #./simple_wallet  --wallet-file ./wal2 --password Vatson2008  --rpc-bind-port 18082

    cmd1 = "{0}simple_wallet".format(run_folder)
    cmd2 = "--wallet-file {0}".format(wallet)
    cmd3 = "--password={0}".format(pwd)
    cmd4 = "--rpc-bind-port 18082"

    prx =  Popen([cmd1,cmd2,cmd3,cmd4],stdout=PIPE,stdin=f)

    out =  prx.stdout.read()
    #    out =  Popen([cmd1,cmd2,cmd3,cmd4],stdout=PIPE,stdin=f).stdout.read()
    print (out)
    f.close()


def start_wallet(run_folder, wallet, pwd, s_stop=None):
    import sys
    from subprocess import *
    global __cmd__
    cmd = '{0}simple_wallet --wallet-file {1}{2}  --password={3} --rpc-bind-port 18082'.format(run_folder, WALLET_FOLDER, wallet, pwd)
    __cmd__ = cmd
    proc = Popen(cmd, shell=True, stdout=PIPE)
    cnt = 0
    ret = True
    while True:
        cnt += 1
        if cnt > 4000:
            break
        data = proc.stdout.readline()   # Alternatively proc.stdout.read(1024)
        find_cnt =  data.find('Idle')
        if find_cnt != -1:
            break
        find_stop =  data.find('Stopped')
        if find_stop != -1:
            ret = False
            break
        if len(data) == 0:
            break
        sys.stdout.write(data)   # sys.stdout.buffer.write(data) on Python 3.x
        if s_stop is not None:
            if (int(s_stop.value) == 1):
                print 'break:'
                break
        time.sleep(0.01)
    return ret

###    run_wallet(s_stop, cmd)
#    print(__cmd__)
#    run_wallet(s_stop)
#    print('Wallet loaded OK')
#Wallet initialize failed: can't load wallet file '/opt/kribbz/kribbz_wallet.wallet', check password



def cmd_wallet(cmd= "stop_wallet"):
    try:
        rpc_input = {
            "method": cmd,
            }
        headers = {'content-type': 'application/json'}
        rpc_input.update({"jsonrpc": "2.0", "id": "0"})
        response = requests.post(
            WALLET_URL,
            data=json.dumps(rpc_input),
            headers=headers)
    except:
        print('No connect or other error')
        pass


def stop_wallet():
    cmd_wallet(cmd= "stop_wallet")


def save_wallet():
    cmd_wallet(cmd= "store")


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
            },
         "transfer": {
             "amount":12.54321,
             "destination_address":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
         },
         "smart_contract": {
             "agent_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
             "agent_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
             "investor_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
             "investor_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
             "owner_signature":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
             "owner_pkey":"ckbzzBGZpWBZiPyQmxN3NCK8DJ8S37Vhxb69a9pbYXgMAwKKPDGeZ93aZgSXfX1E3GMEbk6tgLGPK8gDAeGquLmASXKvRim7pzN",
         },
        }
    Return:
       reply(JSON) {"reply":
                 {"msgId":cursor.lastrowid,"error":{"errorCode":PSI.errorCode,"errorMessage":PSI.errorMessage}}
    }
    """

    psi_log_info(request.url)
    psi_log_info("POST: %s" % request.POST.dict)
    kr_data = None
    try:
        kr_data = parse_request("kribbz")
#        for key,val in kr_data.items():
#            d = kr_data[key]
#            psi_log_debug( str(d) + ' = ' + str(val))
    except Exception as errtxt:
        psi_log_error(str(errtxt))
        pass
    print(kr_data)

    d_address = None
    amnt = None
    kr_amnt = None
    wallet = None
    pwd =  None

    try:
        kr_amnt = parse_request("transfer")
        for key,val in kr_data.items():
            d = kr_data[key]
#            psi_log_debug( str(d) + ' = ' + str(val))
        amnt = kr_amnt["amount"]
        d_address = kr_amnt["destination_address"]
    except Exception as errtxt:
        psi_log_error(str(errtxt))
        pass
    print(amnt, d_address)

    sec = None
    try:
        sec = parse_request("wallet")
        for key,val in sec.items():
            d = sec[key]
#            psi_log_debug( str(d) + ' = ' + str(val))
        pwd = sec["password"]
        wallet = sec["wallet_name"]
    except Exception as errtxt:
        psi_log_error(str(errtxt))
        pass
    print(pwd, wallet)


#    run_wallet(wallet, pwd)
    from subprocess import Popen, PIPE
    from tempfile import SpooledTemporaryFile as tempfile
    f = tempfile()
    f.write('exit\n')
    f.seek(0)

    # Start wallet
    #    print Popen(['/bin/grep','f'],stdout=PIPE,stdin=f).stdout.read()
    #./simple_wallet  --wallet-file ./wal2 --password Vatson2008  --rpc-bind-port 18082
    # ./simple_wallet --wallet-file /opt/kribbz/kribbz_wallet  --password Password12345 --rpc-bind-port 18082
    run_folder= APP_FOLDER
    cmd1 = "{0}simple_wallet".format(run_folder)
    cmd2 = "--wallet-file"
    cmd3 = "{0}{1}".format(WALLET_FOLDER, wallet)
    cmd4 = "--password"
    cmd5 = "{0}".format(pwd)
    cmd6 = "--rpc-bind-port"
    cmd7 = "18082"
#    proc =  Popen([cmd1,cmd2,cmd3,cmd4,cmd5,cmd6,cmd7],stdout=PIPE,stdin=f).stdout.read()
#    out =  prx.stdout.read()
#    print(out)


#    import sys
#    from subprocess import *
#    cmd = "{0}simple_wallet --wallet-file {1}{2}  --password={3} --rpc-bind-port 18082".format(run_folder, WALLET_FOLDER, wallet, pwd)
#    proc = Popen(cmd, shell=True, stdout=PIPE)
#    cnt = 0
#    while True:
#        cnt += 1
#        if cnt > 40:
#            break
#        data = proc.stdout.readline()   # Alternatively proc.stdout.read(1024)
#        if len(data) == 0:
#            break
#        sys.stdout.write(data)   # sys.stdout.buffer.write(data) on Python 3.x

    s_stop = Value('d', 0.0)

    ret = start_wallet(run_folder, wallet, pwd, s_stop)
    if not ret:
        rez2 = {"tx_hash": None, "msg": 'wallet error', "error":True, "success":False}
        return (json.dumps(rez2, indent=4))

    # simple wallet is running on the localhost and port of 18082
    url = WALLET_URL   # "http://localhost:18082/json_rpc"

    # standard json header
    headers = {'content-type': 'application/json'}
#    destination_address = "ckbzzBr9AquP7taMtmySt5PLPRAAxoC9ueGu2bqgveWf62d9X8DawW4gHBxmjLBuYDF5vspjRoQU37SgFYbHAKTS83vfWonzRKq"  #wal5

    destination_address = d_address
#    destination_address = "ckbzz7dYVt6T4sBWhjp8wqQUMgoE8hWyfFCcBjjdLrzEdJU9SQsXjm73rb4VzZt7RxGzuLCAs4ZtQQMJzeELHP841TbYDt4Rm9V" # wal6

    # amount of xmr to send
    amount = float(amnt)
#    amount = 12.54321

    # cryptonote amount format is different then
    # that normally used by people.
    # thus the float amount must be changed to
    # something that cryptonote understands
    int_amount = int(get_amount(amount))

    # just to make sure that amount->coversion->back
    # gives the same amount as in the initial number
    t_amount = float(get_money(str(int_amount)))
    print(t_amount, amount, int_amount)
    assert amount == float(get_money(str(int_amount))), "Amount conversion failed"

    # send specified xmr amount to the given destination_address
    recipents = [{"address": destination_address,
                  "amount": int_amount}]

    # using given mixin
    mixin = 0

    # get some random payment_id
    payment_id = get_payment_id()
    kr1 =  kr_data
#    kr1 =    {
#        "transactionId":"643427363","streeAddress":"700 Rodeo Drive","cityName":"Beverly Hills",
#        "stateCode":"CA","zipCode":"90210","latitude":"34.079678","longitude":"-118.413515",
#        "transactionDateTime":"1523855778",
#        "transactionTotal":"9975000.00",
#        "sellerName":"John Clark",
#        "buyerName":"Emily Stevens",
#        }

    kribbz_info =json .dumps(kr1)
    #    kribbz_info ='01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
#    kribbz_info ='test_transfer'
    print(kribbz_info)
    # simplewallet' procedure/method to call
    rpc_input = {
        "method": "transfer",
        "params": {"destinations": recipents,
                   "mixin": mixin,
#                   "payment_id" : payment_id,
                   "kribbz_info": kribbz_info,
                   "get_tx_key": True,
                   },
        }
    # add standard rpc values
    rpc_input.update({"jsonrpc": "2.0", "id": "0"})
    try:
        # execute the rpc request
        response = requests.post(
            url,
            data=json.dumps(rpc_input),
            headers=headers)
    #    rez = json.dumps(response.json())
        rez = response.json()
#        f.close()
        save_wallet()
        time.sleep(2)  # sleep 
        s_stop.value = 1
        stop_wallet()
        success = True
    except   Exception as ex1:
        out = 'coin transfer not successful'
        error = "simple wallet not started"
        success = False
        tx_hash = None

#    {u'jsonrpc': u'2.0', u'id': u'0', u'result': {u'tx_hash': u'00000000000000001701000000000000320e5717afca5e5e0000000000000000'}}
    if success:
        try:
            tx_hash = rez[u'result'][u'tx_hash']
        except :
            tx_hash = None
        if tx_hash is not None:
            out = 'coin transfer successful'
            success = True
            error = "0"
        else:
            out = 'coin transfer not successful'
            error = rez
            success = False

    rez2 = {"tx_hash": tx_hash, "msg": out, "error":error, "success":success}

    print(rez2)
    return (json.dumps(rez2, indent=4))

def wallet_cmd(cmd="getbalance"):
    sec = None
    try:
        sec = parse_request("wallet")
        for key,val in sec.items():
            d = sec[key]
            #            psi_log_debug( str(d) + ' = ' + str(val))
        pwd = sec["password"]
        wallet = sec["wallet_name"]
    except Exception as errtxt:
        psi_log_error(str(errtxt))
        return None
    print(pwd, wallet)

    w_ret = start_wallet(APP_FOLDER, wallet, pwd)
    if not w_ret:
        return None

    try:
        # simple wallet is running on the localhost and port of 18082
        url = WALLET_URL
        # standard json header
        headers = {'content-type': 'application/json'}
        # simplewallet' procedure/method to call
        rpc_input = {
            "method": cmd
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
        rez = json.dumps(response.json())
        print(json.dumps(response.json(), indent=4))
    except:
        rez = None
    stop_wallet()

    return (rez)


@app.post("/get_balance")
def get_balance():
    rez = wallet_cmd("getbalance")
    if rez is not None:
        out = 'get_balance OK'
        success = True
        error = "0"
    else:
        out = 'get_balance error'
        error = 'get_balance error'
        success = False
    rez = {"result": rez, "msg": out, "error":error, "success":success}
    return (json.dumps(rez, indent=4))


@app.post("/get_payments")
def get_payments():

    # simple wallet is running on the localhost and port of 18082
    url = WALLET_URL  # "http://localhost:18082/json_rpc"

    # standard json header
    headers = {'content-type': 'application/json'}

    # simplewallet' procedure/method to call
    rpc_input = {
        "method": "get_payments",
        "params": {"payment_id": "f8f4638f4b1d958868aa1c1884ae603f8ccf5423e3d8d7a976ae6038d6a72f71"}
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


@app.post("/get_transfers")
def get_transfers():
    rez = wallet_cmd(cmd="get_transfers")
    if rez is not None:
        out = 'get_transfers OK'
        success = True
        error = "0"
    else:
        out = 'get_transfer error'
        error = 'get_transfers error'
        success = False
    rez = {"result": rez, "msg": out, "error":error, "success":success}
    return (json.dumps(rez, indent=4))


@app.post("/search_kribbz")
def search_kribbz():
    rez_s = wallet_cmd(cmd="get_transfers")
    rez = json.loads(rez_s)
    try:
        transfers = rez['result']['transfers']
    except   Exception as ex1:
        transfers = None

    sec_filter = None
    try:
        sec_filter = parse_request("filter")
        print(sec_filter)
    except Exception as errtxt:
        psi_log_error(str(errtxt))
        pass

    rez_output = []
    cnt = 0
    if transfers is not None  and sec_filter is not None:
        for tr in transfers:
            found = True
            try:
                kribbz2 = json.loads(tr['kribbz_info'])
                for key,val in sec_filter.items():
                    d = sec_filter[key]
                    if kribbz2[key] != d:
                        found = False
                        break
                    print(key, d, 'OK')
            except :
                found = False

            if found:
                rez_output.append(tr)
                cnt += 1
        out = 'kribbz search successful'
        success = True
        error = "0"
    else:
        out = 'kribbz search  not successful'
        error = rez
        success = False

    print('cnt found=' + str(cnt))
    rez2 = {"transfers": rez_output, "msg": out, "error":error, "success":success}

    print(rez2)
    return (json.dumps(rez2, indent=4))


def get_money(amount):
    """decode cryptonote amount format to user friendly format. Hope its correct.

    Based on C++ code:
    https://github.com/monero-project/bitmonero/blob/master/src/cryptonote_core/cryptonote_format_utils.cpp#L751
    """

#    CRYPTONOTE_DISPLAY_DECIMAL_POINT = 8

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


@app.post("/create_address")
def create_address():

    sec = None
    try:
        sec = parse_request("wallet")
        for key,val in sec.items():
            d = sec[key]
            psi_log_debug( str(d) + ' = ' + str(val))
        pwd = sec["password"]
        wallet = sec["wallet_name"]
    except Exception as errtxt:
        psi_log_error(str(errtxt))
        pass
    print(pwd, wallet)

    run_folder= APP_FOLDER
#    pwd = "Password12345"
#    wallet = "wallet6"

#    code = os.system("{0}simple_wallet  --password={1} --generate-new-wallet /opt/kribbz/{2}".format(run_folder, pwd, wallet))
#    print (code)

    from subprocess import Popen, PIPE
    from tempfile import SpooledTemporaryFile as tempfile
    f = tempfile()
    f.write('exit\n')
    f.seek(0)
    #    print Popen(['/bin/grep','f'],stdout=PIPE,stdin=f).stdout.read()

    cmd1 = "{0}simple_wallet".format(run_folder)
    cmd2 = "--password={0}".format(pwd, wallet)
    cmd3 = "--generate-new-wallet"
    cmd4 = "{0}{1}".format(WALLET_FOLDER, wallet)

    debug =  Popen([cmd1,cmd2,cmd3,cmd4],stdout=PIPE,stdin=f).stdout.read()

    print (debug)

    f.close()

    import os.path
    fname = "{0}{1}.address".format(WALLET_FOLDER ,wallet)

#    if os.path.isfile(fname):
#        address = None


    try:
        with open(fname) as f:
            address = f.readline()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        address = address.strip()
    except :
        address = None
    if address is not None:
        out = 'Wallet existed or created successfully'
        success = True
        error = "0"
    else:
        out = 'Wallet error'
        error = debug
        success = False

    rez = {"address": address, "msg": out, "error":error, "success":success}
    return (json.dumps(rez, indent=4))


@app.post("/get_address")
def get_address():
    rez = wallet_cmd(cmd="get_address")

    if rez is not None:
        out = 'get_address OK'
        success = True
        error = "0"
    else:
        out = 'get_address error'
        error = 'get_address error'
        success = False
    rez = {"result": rez, "msg": out, "error":error, "success":success}
    return (json.dumps(rez, indent=4))


@app.post("/get_height")
def get_height():
    rez = wallet_cmd(cmd="get_height")
    if rez is not None:
        out = 'get_height OK'
        success = True
        error = "0"
    else:
        out = 'get_height error'
        error = 'get_height error'
        success = False
    rez = {"result": rez, "msg": out, "error":error, "success":success}
    return (json.dumps(rez, indent=4))


@app.post("/get_transaction")
def get_transaction():
    rez = None
    psi_log_info(request.url)
    psi_log_info("POST: %s" % request.POST.dict)
    trx_data = None
    try:
        kr_amnt = parse_request("transaction")
        trx_data = kr_amnt["txs_hash"]
    except Exception as errtxt:
        psi_log_error(str(errtxt))
        pass
#    print(trx_data)

    url = DEMON_URL  + '/gettransactions'

    headers = {'content-type': 'application/json'}
    rpc_input = {
        "txs_hashes":[trx_data],
        "decode_as_json":True,
    }

    # add standard rpc values
    rpc_input.update({"jsonrpc": "2.0", "id": "0"})

    # execute the rpc request
    response = requests.post(
        url,
        data=json.dumps(rpc_input),
        headers=headers)

    # make json dict with response
    rez = response.json()

    if rez is not None:
        out = 'get_transaction OK'
        success = True
        error = "0"
    else:
        out = 'get_transaction error'
        error = 'get_transaction error'
        success = False
    rez = {"result": rez, "msg": out, "error":error, "success":success}
    return (json.dumps(rez, indent=4))


#curl  -H 'Content-Type: application/json' --request POST -d '{"jsonrpc":"2.0","id":"0","method":"getblockcount","params": {}}' 'http://127.0.0.1:23926/json_rpc'
@app.post("/get_blockcount")
def get_blockcoun():
    rez = None
    psi_log_info(request.url)
    psi_log_info("POST: %s" % request.POST.dict)

    url = DEMON_URL  + '/json_rpc'

    try:
        rpc_input = {
            "method": 'getblockcount',
            "params": {},
            }
        headers = {'content-type': 'application/json'}
        rpc_input.update({"jsonrpc": "2.0", "id": "0"})
        response = requests.post(
            url,
            data=json.dumps(rpc_input),
            headers=headers)
    except:
        print('No connect or other error')
        pass

    # make json dict with response
    rez = response.json()
    print (rez)

    if rez is not None:
        out = 'get_transaction OK'
        success = True
        error = "0"
    else:
        out = 'get_transaction error'
        error = 'get_transaction error'
        success = False
    rez = {"result": rez, "msg": out, "error":error, "success":success}
    return (json.dumps(rez, indent=4))


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
