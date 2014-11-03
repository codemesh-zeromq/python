#!/usr/bin/env python
import zmq
import sys

port = 7313
def say_hello_and_read_reply(ip):
    ctx = zmq.Context.instance()
    socket = ctx.socket(zmq.REQ)
    socket.connect('tcp://{}:{}'.format(ip, port))
    socket.send_string('hello')
    msg = socket.recv()
    print(msg.decode('UTF-8'))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise RuntimeError('usage: hello_world_client.py SERVER_IP')
    ip = sys.argv[1]
    say_hello_and_read_reply(ip)
