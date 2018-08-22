#! /usr/bin/env python
"""
  Emercom generator Utilities
"""

import subprocess
import signal
import os
from datetime import datetime as dt


def kill_proc(process_name, log_file_name=''):
    """
      Kill process

    Args:
         process_name(str),log_file_name(str)
    """
    proc = subprocess.Popen(["pgrep", process_name], stdout=subprocess.PIPE)
    print( "kill " + process_name)

    # Kill process.
    for pid in proc.stdout:
        os.kill(int(pid), signal.SIGTERM)
        # Check if the process that we killed is alive.
    #        try:
    #            os.kill(int(pid), 0)
    #            raise Exception("""wasn't able to kill the process
    #                              HINT:use signal.SIGKILL or signal.SIGABORT""")
    #        except OSError as ex:
    #            continue
    if len(log_file_name) > 0:
        # Save old logging file and create a new one.
        os.system("cp {0} '{0}-dup-{1}'".format(log_file_name, dt.now()))

        #    Empty the logging file.
        with open(log_file_name, "w") as f:
            pass
            # Check if the process that we killed is alive.


def check_proc_live(process_name):
    """
    Check process live

    Args:
         process_name(str)
    """
    proc = subprocess.Popen(["pgrep", process_name], stdout=subprocess.PIPE)
    ret = 0
    for pid in proc.stdout:
        # print process_name, " pid =", proc.stdout
        if checkPidRunning(pid):
            ret = ret + 1
    return ret


def check_proc_active(process_name):
    """
    Check process live

    Args:
         process_name(str)
    """
    proc = subprocess.Popen(["pgrep", process_name], stdout=subprocess.PIPE)
    ret = 0
    for pid in proc.stdout:
        # print process_name, " pid =", proc.stdout
        ret = ret + 1
    return ret


def checkPidRunning(pid):
    """
    Check For the existence of a unix pid.

    Args:
         pid(int)
    """

    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


def checksum256(st):
    """
    Check sum computation

    Args:
         st(str):  byte sequence
    """
    #   !!!Stupid bug!!!  Unpredictable $ as first symbol
    # if st[0]=='$':
    #     st=st[1:]
    cs = reduce(lambda x, y: x ^ y, map(ord, st)) % 256
    return cs


if __name__ == '__main__':
    check_proc_live("ssu-update.sh")

