#!/usr/bin/env python
import zmq
import sys

port = 7313

def wait_for_hello_and_say_world():
    ctx = zmq.Context.instance()
    socket = ctx.socket(zmq.REP)
    socket.bind('tcp://0.0.0.0:{}'.format(port))
    while True:
        msg = socket.recv()
        if msg.decode('UTF-8').lower() == 'hello':
            socket.send_string('world')
    
if __name__ == '__main__':
    wait_for_hello_and_say_world()
