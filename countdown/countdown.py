'''A Timer for counting down to get off the work.'''
import os
import math
import threading
import signal
from datetime import datetime, timedelta, timezone
from tokenize import Number
from reprint import output

# reprint is a module to implement multi-line output in terminal.

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
TIME_FORMAT_NOS = "%Y-%m-%d %H:%M"
TIMER_INTERVAL=0.1


def cst_now():
    '''Generate a datetime object with the current time in UTC+8 with tzinfo=None.'''
    now_utc = datetime.utcnow().replace(tzinfo=timezone.utc)
    now_cst = now_utc.astimezone(timezone(timedelta(hours=8)))
    now_cst = now_cst.replace(tzinfo=None)
    return now_cst


def delta_str(delta:timedelta):
    '''Format timedelta object with my own format.'''
    h = math.floor(delta.seconds/60/60)
    m = math.floor((delta.seconds/60) % 60)
    s = delta.total_seconds()-60*60*h-60*m
    return '{0} Hour {1:>2} Min {2:>2.3f} Sec'.format(h, m, s)


def progress_bar(p):
    '''Create a progress bar by chars.'''
    len = 23
    bar = "["
    for i in range(0, int(p*len)):
        bar = bar+'X'
    for i in range(int(p*len), len):
        bar = bar+'_'
    bar = bar+']'
    return bar


def fun_timer():
    '''The main process of countdown.'''
    # when stop flag from Ctrl+C is set, exit
    if stop_flag:
        return
    delta = endtime-cst_now()
    percent = 1-delta.total_seconds()/totaltime.total_seconds()

    if (endtime-cst_now()).total_seconds() < 0:
        output_lines.change([])
        print(
            "Countdown finished at {0}.\nEnjoy your off-work time!".format(endtime.strftime(TIME_FORMAT)))
    else:
        output_lines[0] = "\033[0;36;47m           CALL OF OFF-WORK            \033[0m"
        output_lines[1] = 'Measure From: {0}'.format(starttime.strftime(TIME_FORMAT_NOS))
        output_lines[2] = '          To: {0}'.format(endtime.strftime(TIME_FORMAT_NOS))
        output_lines[3] = 'Current Time: \033[1;34;40m{0}\033[0m'.format(cst_now().strftime(TIME_FORMAT))
        output_lines[4] = 'Remains:      \033[1;31;40m{0}\033[0m'.format(delta_str(delta), delta.total_seconds())
        output_lines[5] = 'Percentage:   {:.6%}'.format(percent)
        output_lines[6] = 'Progress:     {0}'.format(progress_bar(percent))

        global timer
        timer = threading.Timer(TIMER_INTERVAL, fun_timer)
        timer.start()

def goodbye(signum, frame):
    '''Signal Handler when the program will be interrupted.'''
    global stop_flag
    stop_flag = True
    output_lines.change([])
    print("Interrupted at {0}. Bye!".format(cst_now().strftime(TIME_FORMAT)))


# _____PROGRAM STARTS HERE_____ #

# Set signal to receive Ctrl+C
signal.signal(signal.SIGINT, goodbye)
signal.signal(signal.SIGTERM, goodbye)
stop_flag = False

now_cst = cst_now()
# TODO Make starttime/endtime variable
starttime = datetime(now_cst.year, now_cst.month, now_cst.day, 9, 30, 0, 0)
endtime = datetime(now_cst.year, now_cst.month, now_cst.day, 18, 30, 0, 0)
totaltime = endtime-starttime

# Start printing
print("\033c", end="")  # Clear screen (not work in cmd or powershell)
os.system("cls") # Clear screen in cmd
with output(initial_len=7, interval=0) as output_lines:
    output_lines[0] = ""

if (endtime-cst_now()).total_seconds() < 0:
    print("Current Time has already passed the End Time.\nEnjoy your off-work time!")
else:
    fun_timer()
