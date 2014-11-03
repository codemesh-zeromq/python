#!/usr/bin/env python
import zmq
import readline
import multiprocessing
import sys
from fabric.colors import blue, cyan, green, magenta, red, white, yellow
import random

colors = [blue, cyan, green, magenta, red, white, yellow]
port = 7315
ctx = zmq.Context()

#sub, connect to everyone, read everything. must run in background thread
def read_messages(first_3_octets):
    def _read_messages():
        socket = ctx.socket(zmq.SUB)
        socket.setsockopt_string(zmq.SUBSCRIBE, '')
        all_ips = [first_3_octets + '.' +  str(i) for i in range(2,255)]
        for ip in all_ips:
            print('Connecting to {}'.format(ip))
            socket.connect('tcp://{}:{}'.format(ip, port))
        while True:
            msg = socket.recv()
            if msg.decode('UTF-8').strip():
                print(msg.decode('UTF-8').strip())
    return _read_messages


def random_color(msg):
    return random.choice(colors)(msg)

#pub, bind to 7315, send on enter
def send_messages(nickname):
    socket = ctx.socket(zmq.PUB)
    socket.bind('tcp://*:7315')
    while True:
        msg = input()
        if msg.strip():
            socket.send_string('<{}> {}'.format(nickname, random_color(msg.strip())))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise RuntimeError('usage: chat.py PARTIAL_IP')
    subscriber = multiprocessing.Process(target=read_messages(sys.argv[1]))
    subscriber.start()
    send_messages(sys.argv[2])
