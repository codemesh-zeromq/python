#!/usr/bin/env python
import zmq
import sys

hello_world_port = 7313
discovery_port = 7314

ctx = zmq.Context.instance()

def wait_for_someone_to_connect_to_and_say_hello():
    socket = ctx.socket(zmq.SUB)
    socket.setsockopt_string(zmq.SUBSCRIBE, '')
    socket.bind('tcp://*:{}'.format(discovery_port))
    print('Bound to *:{}, waiting for announce'.format(discovery_port))
    while True:
        msg = socket.recv()
        ip = msg.decode('UTF-8')
        print('Got announce from {}'.format(ip))
        say_hello_and_read_reply(ip)

def say_hello_and_read_reply(ip):
    socket = ctx.socket(zmq.REQ)
    print('Connecting to {}'.format(ip))
    socket.connect('tcp://{}:{}'.format(ip, hello_world_port))
    socket.send_string('hello')
    msg = socket.recv()
    print('Received \'{}\' from {}'.format(msg.decode('UTF-8'), ip))

if __name__ == '__main__':
    wait_for_someone_to_connect_to_and_say_hello()
