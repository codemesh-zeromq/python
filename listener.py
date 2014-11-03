import zmq
import time
import sys
import socket

ctx = zmq.Context()

if __name__ == '__main__':
    sock = ctx.socket(zmq.SUB)
    sock.setsockopt(zmq.SUBSCRIBE, '')
    sock.bind('tcp://*:7314')
    while True:
        print sock.recv()
