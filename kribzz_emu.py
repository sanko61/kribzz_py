#!/usr/bin/env python
#-*- coding:utf-8 -*-

""" Send JSON request to emercom generator

"""
import json
# import requests
import requests0 as requests
import base64
import sqlite3
import datetime
import time
import thread
import os

HOST = "http://localhost"
#HOST = "https://10.137.190.159"
#HOST = "https://10.137.190.187"
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
        return r.json
    else:
        print r.text
        raise Exception403(r.json['dsc'].encode("utf8"))


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
        return r.json
    else:
        raise Exception403(r.json['dsc'].encode("utf8"))


#PES   version
def send_message0():
    """Send message (type=0,PES version).

      Returns:
         dict.  The JSON response ::
      """
    return post('send_message',
                {"msg_ids":
                     {'type': 0, "priority": 3, "id": 57, "cnt_rep": 1, 'interval': 5, 'emercom_version': 3},
                 "msg_data":
                     {'startdate': '', 'enddate': '31-12-2012 10:10:00', "title": "Alarma",
                      "text": "Emergency message", 'footer': 'EMERCOM footer', "audio_track": "out2.ts"
                      #"out2.ts"  "437351101028.ts"
                     },
                },
    )['reply']


def send_message1():
    """Send message (type=1,PES version).

      Returns:
         dict.  The JSON response ::
      """
    return post('send_message',
                {"msg_ids":
                     {'type': 1, "priority": 1, "id": 58, "cnt_rep": 1, 'interval': 2},
                 "msg_data":
                     {'startdate': '', 'enddate': '31-12-2012 14:12:12', "title": "Alarma",
                      "text": "Emergency message", 'footer': 'EMERCOM footer', "audio_track": "437351101028.ts"
                      #"avtest2.ts"
                     },
                 "msg_desc": {
                     "stbs": ['12345678901234', '43210987654321']
                 }
                },
    )['reply']


def send_message2():
    """Send message (type=2,PES version).

      Returns:
         dict.  The JSON response ::
      """
    return post('send_message',
                {"msg_ids":
                     {'type': 2, "priority": 1, "id": 59, "cnt_rep": 555, 'interval': 1},
                 "msg_data":
                     {'startdate': '', 'enddate': '31-12-2012 14:12:12', "title": "Alarma",
                      "text": "Emergency message", 'footer': 'EMERCOM footer', "audio_track": "danger.ts"
                     },
                 "msg_desc": {
                     "addresses": ['1234567890123456789', '9876543210123456789'],
                 }
                },
    )['reply']


def send_geo():
    """Send geo metka message (type=3,PES version).

      Returns:
         dict.  The JSON response ::
      """
    return post('send_geo',
                {"msg_ids":
                     {'type': 3, "priority": 1, "id": 60, "cnt_rep": 444, 'interval': 2},
                 "msg_desc": {
                     "addresses": ['1234567890123456789', '9876543210123456789'],
                     "stbs": ['12345678901234', '43210987654321']
                 },
                 "msg_data":
                     {"audio_track": ''},
                }
    )['reply']


#EMM   version
def send_message_e2():
    """Send message (type=0,EMM version).

      Returns:
         dict.  The JSON response ::
      """
    return post('send_message',
                {"msg_ids":
                     {'type': 0, "priority": 3, "id": 57, "cnt_rep": 99999, "audio_length": 60, 'interval': 5,
                      'emercom_version': 2},
                 "msg_data":
                     {'startdate': '', 'enddate': '31-12-2012 10:10:00', "title": "Alarma",
                      "text": "Navodnenie em3 Test ", 'footer': 'EMERCOM footer', "audio_track": "tanki2.ts",
                      #"out2.ts"  "437351101028.ts"  avtest20.ts  avtest2.ts  tk-24.ts
                     },
                 "msg_cfg": {
                     "pcr_pid": 2007, "audio_pid": 2001, "video_pid": 2007, "config_type": 1, "id": 23
                 }
                },
    )['reply']


def send_message1_e2():
    """Send personal message (type=1,EMM version).

      Returns:
         dict.  The JSON response ::
      """
    return post('send_message',
                {"msg_ids":
                     {'type': 1, "priority": 3, "id": 58, "cnt_rep": 1, "audio_length": 60, 'interval': 5,
                      'emercom_version': 2},
                 "msg_data":
                     {'startdate': '', 'enddate': '31-12-2012 14:12:12', "title": "Alarma",
                      "text": "Индивидуальное сообщение для карты 23007300031612 Емерком 3", 'footer': 'EMERCOM footer',
                      "audio_track": "tanki2.ts"          # avtest2.ts  437351101028.ts  tanki2.ts
                     },
                 "msg_desc": {
                     # "stbs": [ "16007300032010" ]  #0a007d0a
                     "stbs": ["23007300031612", "16007300032010"]
                     # "stbs": [  "3007300031612", "26007300032010", "A600730003201A"]  #bad IDs


                 },
                 "msg_cfg": {
                     "pcr_pid": 2007, "audio_pid": 2001, "video_pid": 2007, "config_type": 1, "id": 0x2C
                 }
                },
    )['reply']


def send_message_e2_test():
    """Send personal test message viuga (type=0,EMM version).

      Returns:
         dict.  The JSON response ::
      """
    return post('send_message',
                {
                 #    "msg_ids":
                 #     {"interval": 180, "priority": 2, "cnt_rep": 4, "audio_length": 60, "type": 0, "id": 14},
                 # "msg_data":
                 #     {"audio_track": "caf8bf683e094d0bb3a6cbacad34ae64-z1-60c.wav.ts",
                 #      "startdate": "20-09-2013 18:51:00", "text": "сообщение Емерком ",
                 #      "title": "\\u04101 - \\u041a3 - \\u0428\\u0412\\u0421"},
                 # "msg_cfg":
                 #     {"name": "test", "audio_pid": 2001, "config_type": 2, "audio_bitrate": 1100720, "id": 7}


                 "msg_desc": {"addresses": [[83, 0, 1, 0, 0, 0, 0]]},
                 "msg_ids": {"interval": 300, "priority": 3, "cnt_rep": 1, "audio_length": 38, "type": 2, "id": 16},
                 "msg_data": {"audio_track": "864d584fccbf4e8db9db2afd28824dde-Sirena-Pogar-R.mp3.ts", "startdate": "22-11-2013 18:01:58",
                              "text": "\\u041a\\u0430\\u0440\\u0442\\u0430-12-\\u0410\\u041e-\\u041d\\u0435\\u043d\\u0435\\u0446\\u043a\\u0438\\u0439-\\u0433\\u043e\\u0440\\u043e\\u0434-\\u041d\\u0430\\u0440\\u044c\\u044f\\u043d-\\u041c\\u0430\\u0440",
                              "title": "\\u041a\\u0430\\u0440\\u0442\\u0430-12"},
                 "msg_cfg": {"fec_id": None, "name": "K2001", "pcr_pid": None, "audio_pid": 2001, "default": True, "symbol_rate": None, "video_pid": None, "polarization": None, "channel_id": None, "config_type": 1, "frequency": None,
                             "audio_bitrate": 1100720, "id": 6}

                }
    )['reply']


def send_message2_e2():
    """Send address message (type=2,EMM version).

      Returns:
         dict.  The JSON response ::
      """
    return post('send_message',
                {"msg_ids":
                     {'type': 2, "priority": 1, "id": 0x2C, "cnt_rep": 100, "audio_length": 60, 'interval': 0,
                      'emercom_version': 2},
                 "msg_data":
                     {'startdate': '', 'enddate': '31-12-2012 14:12:12', "title": "Alarma",
                      # "text": "Ш1-русский текст Рязань групповое",  'footer':'EMERCOM footer', "audio_track":  "437351101028.ts" # "avtest2.ts"  u'\u04281-\u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u0442\u0435\u043a\u0441\u0442',
                      "text": "\\u043c\\u043e\\u0441\\u043a\\u0432\\u0430",
                      "title": "\\u043c\\u043e\\u0441\\u043a\\u0432\\u0430", "audio_track": "437351101028.ts"
                     },
                 "msg_desc": {
                     # "addresses": [[ 0x04,0x02,    0xffff , 0x0002 , 0xffff , 0xffffff , 0x00000c ]],
                     # "addresses": [[ 0x04, 0xFF,    0xffff , 0xFFFF , 0xffff , 0xffffff , 0xFFFFFF ]],
                     "addresses": [[0x15, 0x07, 0x00, 0x00, 0x00, 0x000, 0x000]],  # Кострома
                     # "addresses": [[ 0x15, 12,  0x00 , 0x00 , 0x00 , 0x000 , 0x000 ]],  #Рязань
                 },
                 "msg_cfg": {
                     "pcr_pid": 2007, "audio_pid": 2003, "video_pid": 2007, "config_type": 1, "id": 0x2C
                 }
                },
    )['reply']


# {'{"msg_desc": {"addresses": [[77, 0, 0, 0, 0, 0, 0]]}, "msg_ids": {"interval": 300, "priority": 2, "cnt_rep": 3, "audio_length": 219, "type": 2, "id": 18}, "msg_data": {"audio_track": "95ca41ba66e644f488f95de261b9b76e-Instrumental.mp3.
# ts", "startdate": "04-09-2013 14:55:00", "text": "\\u043c\\u043e\\u0441\\u043a\\u0432\\u0430", "title": "\\u043c\\u043e\\u0441\\u043a\\u0432\\u0430"}, "msg_cfg": {"fec_id": null, "name": "\\u043a\\u043e\\u043d\\u04441", "pcr_pid": null, "audio_pid": 2002, "default": true
# , "symbol_rate": null, "video_pid": null, "polarization": null, "channel_id": null, "config_type": 1, "frequency": null, "audio_bitrate": 2100720, "id": 1}}': ['']}


def send_message2_e2_kostroma():
    """Send address message to Kostroma(type=2,EMM version).

      Returns:
         dict.  The JSON response ::
      """
    return post('send_message',
                {"msg_ids":
                     {'type': 2, "priority": 1, "id": 0x2C, "cnt_rep": 1, 'interval': 15, 'emercom_version': 2},
                 "msg_data":
                     {'startdate': '', 'enddate': '31-12-2012 14:12:12', "title": "Alarma",
                      "text": "Ш1-русский текст Кострома групповое", 'footer': 'EMERCOM footer',
                      "audio_track": "437351101028.ts"
                      # "avtest2.ts"  u'\u04281-\u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u0442\u0435\u043a\u0441\u0442',
                     },
                 "msg_desc": {
                     "addresses": [[0x15, 0x07, 0x00, 0x00, 0x00, 0x000, 0x000]],  # Кострома
                     # "addresses": [[ 0x15, 7,  0x00 , 0x00 , 0x00 , 0x000 , 0x000 ]],  #FIAS
                 },
                 "msg_cfg": {
                     "pcr_pid": 2006, "audio_pid": 2001, "video_pid": 2006, "config_type": 1, "id": 0x2C
                 }
                },
    )['reply']


def send_message2_e2_ryazan():
    """Send address message to Ryazan(type=2,EMM version).

      Returns:
         dict.  The JSON response ::
      """
    return post('send_message',
                {"msg_ids":
                     {'type': 2, "priority": 1, "id": 0x2C, "cnt_rep": 1, 'interval': 15, 'emercom_version': 2},
                 "msg_data":
                     {'startdate': '', 'enddate': '31-12-2012 14:12:12', "title": "Alarma",
                      "text": "Русский текст Рязань групповое", 'footer': 'EMERCOM footer',
                      "audio_track": "437351101028.ts"
                      # "avtest2.ts"  u'\u04281-\u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u0442\u0435\u043a\u0441\u0442',
                     },
                 "msg_desc": {
                     "addresses": [[0x15, 12, 0x00, 0x00, 0x00, 0x000, 0x000]],  # Рязань
                 },
                 "msg_cfg": {
                     "pcr_pid": 2006, "audio_pid": 2001, "video_pid": 2006, "config_type": 1, "id": 0x2C
                 }
                },
    )['reply']

# 00 80  (serv)   00 00 00 00 (tarID)  40 (type) 00  00 00 2c  (id)  00 00 (res)  00 10  (geoLen)  90
# 0e  (geo tag)  01 (g1) 00 (g2)  00 00 (g3) 00 00(g4) 00  00 (g5)  00 00 00 (g6) 00 00 00 (g7) 02 (type)
# 1f ff (v_pid) 10 02 (a_pid)  1f ff (pcr_pid)  10 (crypt) 00  0a (len)  be 3a e8 39  2e cb c7
# d5  ae a2 3a ad  aa 9b 6f 0c  (CRYPT TEXT)  d0 37 6a 5b (CRC)

# 15 07 00 00 00 00 00  00 00 00 00 00 00 00 02


def send_message1_e2m():
    """Send test personal message to STB id(type=1,EMM version).

      Returns:
         dict.  The JSON response ::
      """
    return post('send_message',
                {
                    "msg_desc": {
                        "stbs": [[0x0c007d0c]]   # "78000000000"    [ [0x0c007d0c] ]
                    },
                    "msg_ids":
                        {"interval": 120, "priority": 2, "cnt_rep": 1, "audio_length": 263, "type": 1, "id": 284},

                    "msg_data":
                        {
                            "audio_track": "437351101028.ts", "startdate": "03-04-2013 13:38:00", "text": "34563456",
                            "title": "4536345"},
                }
    )['reply']


def send_message2_e2m():
    """Send test message to two addresses(type=2,EMM version).

      Returns:
         dict.  The JSON response ::
      """
    return post('send_message',
                {
                    "msg_desc": {
                        "addresses": [[78, 0, 0, 0, 2060, 0, 0], [78, 0, 0, 0, 5900, 0, 0]]
                    },
                    "msg_ids":
                        {"interval": 120, "priority": 2, "cnt_rep": 3, "audio_length": 263, "type": 2, "id": 281},
                    "msg_data":
                        {"audio_track": "437351101028.ts",
                         "startdate": "03-04-2013 09:37:35", "text": "or ressurect", "title": "api config 23"},
                }
    )['reply']


def send_geo_e2():
    """Send geometka with address to STB id(type=3,EMM version).

      Returns:
         dict.  The JSON response ::
      """
    return post('send_geo',
                {"msg_ids":
                     {'type': 3, "priority": 1, "id": 0x6286608a, "cnt_rep": 1, 'interval': 2, 'emercom_version': 2},
                 "msg_desc": {
                     "addresses": [[23, 4, 0, 48, 7, 0, 0]],
                     # "addresses": [[ 0x04,0x02,    0xffff , 0x0002 , 0xffff , 0xffffff , 0x00000c ]],
                     # "addresses": [[ 0x15,0x07,    0xffff , 0x0024 , 0xffff , 0xffffff , 0x000001 ]],  #Кострома
                     # "addresses": [[ 0x15,12,    0xffff , 0x0024 , 0xffff , 0xffffff , 0x000001 ]],  #Рязань
                     # "addresses": [[ 0x15, 7,    0xffff , 0x0024 , 0xffff , 0xffff , 0x000001 ]],  #Emercom 3 FIAS
                     # "addresses": [[5, 0, 1, 0, 0, 0, 0], [17, 0, 1, 0, 291, 0, 0]],
                     "stbs": [  "23007300031612"]
                     # "stbs": [  "16007300032010"]  #Рязань
                     # "stbs": [  "23007300031612"]  #Кострома
                     # "stbs": ["16007300032010", "23007300031612"]

                 },
                 # "msg_data":
                 #     { "audio_track": ''},
                }
    )['reply']

# 47 47 d4 13 00 8c 00 23    01 00  (serv)  0c 00 7b 7c (TargetId)  20  (type & res)  0a
# c8 30 ef (id)   00 00 02   (reserv)   00  ( crypt ) 15  (g1)  07 (g2)  ff ff (g3)  00 24 (g4)  ff ff (g5)  ff
# ff ff (g6)  00 00 01 (g7)   00 (text)  00 (text)  97 c2 87 89  (CRC)


def send_video():
    """Send test video (type=0).

      Returns:
         dict.  The JSON response ::
      """
    return post('send_message',
                {"msg_ids":
                     {'type': 0, "priority": 3, "id": 57, "cnt_rep": 115, 'interval': 5},
                 "msg_data":
                     {'startdate': '', 'enddate': '31-12-2012 10:10:00', "title": "Alarma",
                      "text": "Emergency message", 'footer': 'EMERCOM footer', "audio_track": "firstaudio.ts",
                      "video_track": "firstvideo.ts"
                     },
                },
    )['reply']


def stop_pdg():
    """
    Send stop PDG  message

      Returns:
         dict.  The JSON response
      """
    return post('stop_pdg',
        {}
    )['reply']


def stop_all():
    """
    Send stop all message
        Args: No
    Returns:
        dict.  The JSON response
    """
    return post('stop_all',
        {}
    )['reply']


def stop_all_geo():
    """
    Send stop messages
      Returns:
         dict.  The JSON response ::
    """
    return post('stop_msg',
                {
                    "is_geo": 1, "msg_ids": []
                }
    )['reply']


def stop_msg():
    """
    Send stop messages
      Returns:
         dict.  The JSON response ::
    """
    return post('stop_msg',
                {
                    "is_geo": 0, "msg_ids": []
                }
    )['reply']


def status():
    """
    Send status
      Returns:
         dict.  The JSON response ::
    """
    return post('status',
        {}
    )['reply']


def message_list():
    """
    Send message list
      Returns:
         dict.  The JSON response
      """
    return post('message_list',
        {}
    )['reply']

def len_message_list():
    """
    Send message list  len
      Returns:
         dict.  The JSON response
      """
    return post('len_message_list',
        {}
    )['reply']

def version():
    """
    Send version
      Returns:
         dict.  The JSON response ::
    """
    return post('version',
                { }
    )['reply']

def status():
    """
    Send status
      Returns:
         dict.  The JSON response ::
    """
    return post('status',
        {}
    )['reply']


def bitrates_reload():
    """
    Send bitrates_reload
      Returns:
         dict.  The JSON response ::
    """
    return post('bitrates_reload',
        {}
    )['reply']


def dektec_scan():
    """
    Scan  dektec_hardware  info
      Returns:
         dict.  The JSON response ::
    """
    return post('dektec_scan',
        { }
    )['reply']


def db_read():
    """
    Test SELECT message  from  SQLITE DB
        Returns:
             dict.  The JSON response ::
    """
    DB = sqlite3.connect("pdg.db", check_same_thread=False)  # or use :memory: to put it in RAM
    cursor = DB.cursor()

    dt = datetime.datetime.now()
    print dt.strftime('%d-%m-%Y %H:%M:%S')
    #    cursor.execute("SELECT  id ,priority,time,cnt_replay,body  FROM messages order by priority DESC, time desc")
    cursor.execute(
        "SELECT  id ,priority,emr_time,cnt_replay,strftime('%Y-%m-%d %H:%M:%S', 'now','localtime') as t_now  FROM messages where (strftime('%Y-%m-%d %H:%M:%S', 'now','localtime') >= emr_time) order by priority DESC, emr_time desc")
    #    [sqlite3.Binary( dt.strftime('%Y-%m-%d %H:%M:%S'))])
    #    cursor.execute(query, [sqlite3.Binary(PSI.pes)])
    #    '2009-11-15 00:00:00'

    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print row[2], row[4]


def set_psi():
    """
    Send setting message
      Returns:
         dict.  The JSON response ::
    """
    return post('settings',
                {"metadata":
                     {
                         'service_provider': 'Some provider', 'service_name': 'Some Channel', 'title': 'Track #5',
                         'comment': 'This is message test', 'network_name': 'emercom_rtrs'
                     },
                 "pdg_bitrates": {'bitrate': 3000000, 'cnt_pack': 3, 'sent_null': 0, 'n_loop_print': 1000,
                                  'n_loop_cmd': 10, 'write_ts': 0, 'send_udp': 1,
                                  'send_DEKTEC_ASI': 0},

                 "pdg_address": {'udp_src': "127.0.0.1", 'udp_port': "5678", 'udp_decs': '0.0.0.0',
                                 'second_out': 'out_ts', 'audio_path': '/home/dev/emercom/media/audio',
                                 'DEKTEC_ASI_Serial': '2160001029', 'DEKTEC_ASI_port': '2'}
                }
    )['reply']


def ts_record_on():
    """
    Start recording ts to file
      Returns:
         dict.  The JSON response ::
    """
    return post('settings',
                {"pdg_bitrates": {'sent_null': 0, 'write_ts': 1,},
                }
    )['reply']


def ts_record_off():
    """
    Stop ts recording
      Returns:
         dict.  The JSON response ::
    """
    return post('settings',
                {"pdg_bitrates": {'sent_null': 0, 'write_ts': 0,},
                 }
    )['reply']


def set_dvb():
    """
    Send set_dvb message
      Returns:
         dict.  The JSON response ::
    """
    return post('set_dvb',
                {
                    "pids":
                        {'pmt_pid': 0x1500, 'emercom_message_pid': 2000, 'emercom_video_pid': 2006,
                         'emercom_carousel_pid': 2004, 'PCR_PID': 2006, 'dsmcc_service_id': 2, 'emercom_unt_pid': 1006, 'emercom_dsmcc_pid': 2100,
                         'transport_stream_id': 1, 'original_transport_stream_id': 1, 'service_id': 1, 'network_id': 1
                        },
                    "bitrates":
                        {'bmuxer': 2300000, 'bpat': 186400, 'bpmt': 186400,
                         'bsdt': 36720, 'bstamp': 24969160, 'btxt': 28000 , 'bcat': 28000 , 'bcarousel': 28000
                        },
                    "av_info": {
                        "a_pids": [2001, 2002, 2003],
                        "a_bitrates": [2100720, 2100720, 2100720],
                    },
                }
    )['reply']


def test_kb1251():
    """ Check kb1251.

      Returns:
         1  - OK  0 -
      """
    import urllib

    a = u"пример"
    print urllib.quote_plus(a.encode('utf8'))
    # %D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80

    s1 = urllib.quote_plus(a.encode('cp1251'))

    # print urllib.quote_plus(a.encode('cp1251'))
    ##
    if s1 == '%EF%F0%E8%EC%E5%F0':
        print "Russian  cp1251 successfully installed"
        return "Russian  cp1251 successfully installed"
    return []

def clear_logs():
    """Reset logs

      """
    os.system("echo '' > /var/log/emercom/emercom3mux.log")
    os.system("echo '' > /var/log/emercom/emercom3pdg.log")
    os.system("echo '' > /var/log/emercom/pdg_emercom.log")

def dsmcc_generate():
    """
    Stop ts recording
      Returns:
         dict.  The JSON response ::
    """
    return post('dsmcc_generate',
        {}
    )['reply']


def dsmcc_start():
    """
    dsmcc star
      Returns:
         dict.  The JSON response ::
    """
    return post('dsmcc_start',
        {'run': 1}
    )['reply']

def dsmcc_stop():
    """
    dsmcc star
      Returns:
         dict.  The JSON response ::
    """
    return post('dsmcc_start',
        {'run': 0}
    )['reply']


class gen_test(object):
    def __init__(self, msg_id=1, audio_pid=2001, msg_cnt_rep=1):
        """
        init class
        """
        self.msg_id = msg_id
        self.audio_pid = audio_pid
        self.msg_text = 'Viuga em3'
        self.msg_cnt_rep = 1
        self.msg_ids = [67]
        self.audio_track = "viuga.ts"
        self.geo_ids = [[5, 0, 1, 0, 0, 0, 0]]
        self.stb_ids = ["23007300031612"]
        self.polarization = 1
        self.frequency  = 474000

    def send_message1_e2_viuga(self):
        """Send personal message viuga (type=1,EMM version).

          Returns:
             dict.  The JSON response ::
          """
        return post('send_message',
                    {"msg_ids":
                         {"interval": 180, "priority": 0, "cnt_rep": self.msg_cnt_rep, "audio_length": 60, "type": 1,
                          "id": self.msg_id},
                     "msg_data":
                         {'startdate': '', 'enddate': '31-12-2012 14:12:12', "title": "Alarma",
                          "text": "Индивидуальное сообщение для карты 23007300031612 Емерком 3", 'footer': 'EMERCOM footer',
                          "audio_track": self.audio_track              # "viuga.ts" avtest2.ts  437351101028.ts  tanki2.ts
                         },
                     "msg_desc": {
                         "stbs": ["23007300031612", "16007300032010"]  # Кострома
                     },
                     "msg_cfg": {
                         "pcr_pid": 2007, "audio_pid": self.audio_pid, "video_pid": 2007, "config_type": 1, "id": 0x2C
                     }
                    },
                    )['reply']

    def send_message_viuga(self):
        """Send viuga message (type=0,EMM version).

          Returns:
             dict.  The JSON response ::
          """
        return post('send_message',
                    {"msg_ids":
                         {'type': 0, "priority": 3, "id": self.msg_id, "cnt_rep": self.msg_cnt_rep, "audio_length": 60, 'interval': 7},
                     "msg_data":
                         {'startdate': '', 'enddate': '31-12-2012 10:10:00', "title": "Alarma",
                          "text": self.msg_text, 'footer': 'EMERCOM footer', "audio_track": self.audio_track
                          #"437351101028.ts",  #"out2.ts"  "437351101028.ts"  avtest20.ts  avtest2.ts  tk-24.ts
                         },
                     "msg_cfg": {
                         "pcr_pid": 2007, "audio_pid": self.audio_pid, "video_pid": 2007, "config_type": 1
                     }
                    },
                    )['reply']

    def setting(self):
        """Send setting

          Returns:
             dict.  The JSON response ::
          """
        return post("settings",
            {"pdg_bitrates": {"emercom_carousel_pid": "2003", "send_DEKTEC_ASI": "0", "bmuxer": "2300000", "original_transport_stream_id": "1", "bpat": "3008", "geo_type": "3", "sent_null": "1", "bsdt": "1400", "write_ts": "0", "emercom_video_pid": "2006",
                              "n_loop_print": "2000", "n_loop_cmd": "10", "bstamp": "200000", "send_udp": "1", "cnt_pack": "3", "transport_stream_id": "1", "btxt": "1400", "emercom_message_pid":
                "2000", "bitrate": "500000", "pmt_pid": "350", "PCR_PID": "2006", "network_id": "1", "insert_prefix": "0", "service_id": "1", "bpmt": "1500"},
             "bitrates": {},
             "pdg_address": {"DEKTEC_ASI_port": "2", "second_out": "save_ts.ts", "udp_port": "5678", "DEKTEC_ASI_Serial": "2160001029", "udp_decs": "0.0.0.0", "udp_src": "127.0.0.1"},
             "other": {"gen_port": "8804", "geo_times": "3", "gen_addr": "http://localhost", "gen_log_path": "gen.log", "gen_cache_path": "cache.db", "geo_period": "60", "bitrate_emercom_carousel": "1400"},
             "pids": {},
             "metadata": {"msg_prefix": "rus", "audio_path": "/home/dev/emercom/media/audio", "encoding": "cp1251"}       # /var/www/v3/emercom/media/audio
            }
        )['reply']

    def blank_setting(self):
        """Send empty setting

          Returns:
             dict.  The JSON response ::
          """
        return post("settings",
                    {"pdg_bitrates": {"emercom_carousel_pid": "", "send_DEKTEC_ASI": "", "bmuxer": "", "original_transport_stream_id": "", "bpat": "", "geo_type": "", "sent_null": "", "bsdt": "", "write_ts": "", "emercom_video_pid": "",
                                      "n_loop_print": "", "n_loop_cmd": "", "bstamp": "", "send_udp": "", "cnt_pack": "", "transport_stream_id": "", "btxt": "",
                                      "emercom_message_pid":"", "bitrate": "", "pmt_pid": "", "PCR_PID": "", "network_id": "", "insert_prefix": "", "service_id": "", "bpmt": ""},
                     "bitrates": {},
                     "pdg_address": {"DEKTEC_ASI_port": "", "second_out": "", "udp_port": "", "DEKTEC_ASI_Serial": "", "udp_decs": "", "udp_src": ""},
                     "other": {"gen_port": "8804", "geo_times": "3", "gen_addr": "http://localhost", "gen_log_path": "gen.log", "gen_cache_path": "cache.db", "geo_period": "60", "bitrate_emercom_carousel": "1400"},
                     "pids": {},
                     "metadata": {"msg_prefix": "", "audio_path": "", "encoding": ""}
                    }
        )['reply']

    def stop_msg(self):
        """
        Send stop messages
          Returns:
             dict.  The JSON response ::
        """
        return post('stop_msg',
                    {
                        'msg_ids': self.msg_ids
                    }
        )['reply']

    def send_geo(self):
        """Send geometka with address to STB id(type=3,EMM version).

          Returns:
             dict.  The JSON response ::
          """
        return post('send_geo',
                    {"msg_ids":
                         {'type': 3, "priority": 1, "id": self.msg_id, "cnt_rep": self.msg_cnt_rep, 'interval': 2},
                     "msg_desc": {
                         "addresses": self.geo_ids,
                         "stbs": self.stb_ids

                     },
                    }
        )['reply']

    def send_message_transpoder(self):
        """Send transpoder message (type=0,EMM version).

          Returns:
             dict.  The JSON response ::
          """
        return post('send_message',
                    {
                        "msg_ids": {"interval": 40, "priority": 1, "cnt_rep": self.msg_cnt_rep, "audio_length": 38, "type": 0, "id": self.msg_id},
                        "msg_data": {"audio_track": self.audio_track, "startdate": "01-11-2013 17:21:04",
                                     "text": self.msg_text},
                        "msg_cfg": {"fec_id": 2, "name": "T1", "pcr_pid": 2007, "audio_pid": 2037, "default": False, "symbol_rate": 27500, "video_pid": 2007, "polarization": self.polarization, "channel_id": None, "config_type": 3, "frequency": self.frequency, "audio_bitrate": 1100720, "id": 32}
                    },
                    )['reply']


    def send_ota(self):
        """Send transpoder message (type=0,EMM version).

          Returns:
             dict.  The JSON response ::
          """
        return post('send_ota',
            {
                "msg_ids": {"interval": 40, "priority": 1, "cnt_rep": self.msg_cnt_rep, "audio_length": 60, "type": 9, "id": self.msg_id},
                "msg_data": {"audio_track": self.audio_track, "startdate": "01-11-2013 17:21:04",
                             "text": self.msg_text},
                "msg_cfg": {"fec_id": 2, "name": "T1", "pcr_pid": 2007, "audio_pid": 2037, "default": False, "symbol_rate": 27500, "video_pid": 2007, "polarization": self.polarization, "channel_id": None, "config_type": 3, "frequency": self.frequency, "audio_bitrate": 1100720, "id": 32}
            },
        )['reply']


if __name__ == "__main__":

    # # All messages will be canseled
    # resp = stop_all()
    # print  resp
    #
    # # Stress test 1251 + 100 translations+ 1000 msg x 100 pids
    # resp = test_kb1251()
    # print  resp
    #
    # GT=gen_test()
    # GT.audio_pid = 2003
    # GT.msg_id = 111111
    # GT.msg_cnt_rep = 10
    # GT.msg_text = "Test message 3 pid audio=" + str(GT.audio_pid) + " id=" + str(GT.msg_id) + " cnt_rep=" + str(GT.msg_cnt_rep)
    # # resp=send_message_e2_test()
    # resp = GT.send_message1_e2_viuga()
    # print  resp
    # print '  Send ' + GT.msg_text
    # #
    # # # # stress test 1000  msg x 100 pids
    # GT.msg_cnt_rep = 3
    # cnt_err = 0
    # msg_num = 1
    # GT.msg_id = 1
    # GT.audio_pid = 2011
    # total_msg = 200
    # total_pid = 200
    # for i in range(total_msg):
    #     try:
    #         print  "=====================================Iteration i=" + str(i) + " err=" + str(cnt_err)
    #         msg_text = "Test message.  pid audio=" + str(GT.audio_pid) + " id=" + str(msg_num)
    #         resp = GT.send_message_viuga()
    #         msg_num = msg_num + 1
    #         GT.msg_id = GT.msg_id + 1
    #         GT.audio_pid = GT.audio_pid + 1
    #         if GT.audio_pid > 2010 + total_pid:
    #             GT.audio_pid = 2011
    #             # resp =send_geo_e2()
    #         print  resp
    #     except:
    #         print   "Error POST"
    #         cnt_err = cnt_err + 1
    # pass

    # for i in range(1000000):
    #     try:
    #         print  "=====================================message_list i="+ str(i)+ " err="+str(cnt_err)
    #         time.sleep(0.01)
    #         resp = message_list()
    #         print  resp
    #     except:
    #         print   "Error POST"
    #         cnt_err=cnt_err+1
    # pass

    # resp = stop_pdg()
    #     resp = set_psi()
    #     resp = set_dvb2()
    #     print  resp
    #     resp = set_psi()
    #     print  resp
    #    time.sleep(25)

    # # 2 pid translation test

    # resp =send_message2_e2m()
    # resp = send_message1_e2();

    # resp = send_message1_e2_viuga()
    # resp = test_kb1251()
    # print  resp
    # resp = send_geo_e2()

    # time.sleep(5)
    # resp = send_message2_e2();
    # print  resp
    # for i in range(100000):
    #     print  "Message list:-------------"
    #     resp = message_list()
    #     print  resp
    #     time.sleep(35)

    # cnt_err=0
    # for i in range(1000):
    #     try:
    # #
    #         print  "=====================================Iteration i="+ str(i)+ " err="+str(cnt_err)
    # #         resp = send_message_e2()
    # #         print  resp
    # #         time.sleep(1)
    #         msg_text = "Test message.  pid audio=" +str(audio_pid)+ " id="+str(msg_id)
    #         resp =send_message_viuga()
    #         msg_id=msg_id+1
    #         audio_pid=audio_pid+1
    #         if audio_pid> 2190:
    #             audio_pid= 2011
    #         # resp =send_geo_e2()
    #         print  resp
    # #         print  "Message list:-------------"
    # #         resp = message_list()
    # #         print  resp
    # #
    # #         resp = status()
    # #         print  'status:-------------'
    # #         print  resp
    # #
    #         # time.sleep(0.1)
    # #         print  "Stop msg"
    # #         resp = stop_msg()
    # #         print  resp
    # #
    # #         time.sleep(1)
    # #     # try:
    # #         resp = message_list()
    # #         print  'message list:'
    # #         print  resp
    # #         time.sleep(2)
    #     except:
    #         print   "Error POST"
    #         cnt_err=cnt_err+1
    #
    #
    # pass

    # resp = send_message_e2()
    # print  resp
    # time.sleep(1)
    # resp =send_message_viuga()
    # print  resp

    # resp = send_message1_e2()
    # resp = send_message_e2()
    #     resp = send_message2_e2()

    # resp = send_message2_e2()
    # resp = send_message1_e2()

    # resp = send_geo_e2()
    # resp = send_message2_e2_kostroma()
    # time.sleep(2)
    # print  resp

    # resp = send_message1_e2()
    # time.sleep(10)
    # resp = send_message2_e2_kostroma()
    # resp = send_message1_e2bug()

    # time.sleep(2)
    # resp = send_message2_e2_ryazan()
    # resp = send_message_e2()

    #    resp= send_message2_e2m()

    #    resp = send_message01()
    #    resp = send_message2()
    #    resp = send_geo()
    #    resp = send_test()

    # resp = stop_all()
    # resp = stop_msg()
    # resp = status()
    #    resp = set_pdg_adress()

    #    for i in range(100):
    #        resp = set_psi()
    #        time.sleep(2)

    #    resp = set_psi()
    #    resp = db_read()
    #     time.sleep(1)
    #     resp = send_message_e2()
    #     time.sleep(10)
    #     print "stop"
    #     resp = stop_all()
    #     time.sleep(2)
    #     # resp = stop_msg()
    #     print "get message_list"
    #     resp = message_list()
    # #     resp = set_dvb()
    #     print  resp

    #    try:
    #
    #        thread.start_new_thread(cash_read_loop,('MyStringHere',1))
    #
    #    except Exception, errtxt:
    #        print errtxt
    #
    #    time.sleep(5)
    #    dt = datetime.datetime.now() # Текущая дата и время
    #    d2 = datetime.datetime.strptime('2012-12-05 21:40:09','%Y-%m-%d %H:%M:%S')
    #    d3 = datetime.datetime.strptime('2012-12-05 21:46:05','%Y-%m-%d %H:%M:%S')
    #
    #    print dt.strftime("%Y-%m-%d %H:%M:%S"), dt > d2,  d3 > d2, d3,d2# П

    #    dt_str = '9/24/2010 5:03:29 PM'
    #    dt_obj = datetime.datetime.strptime(dt_str, '%m/%d/%Y %I:%M:%S %p')
    #    print dt_obj
    #     resp = set_psi3()
    # print  resp
    pass
