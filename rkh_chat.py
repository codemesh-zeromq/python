import multiprocessing
import zmq
import time
import sys
from fabric import colors
import random

rainbow = [getattr(colors, color) for color in dir(colors) if not color.startswith("_")]

def ctx():
    return zmq.Context()

port = 7315

def random_color(s):
    return random.choice(rainbow)(s)

def ip_range(ip_string):
    parts = ip_string.split('.')
    network = '.'.join(parts[:-1])
    me = int(parts[-1])
    return [network + '.' + str(host_number) for host_number in range(2, 255)]

def connected_subscriber(ip_addresses):
    sock = ctx().socket(zmq.SUB)
    sock.setsockopt(zmq.SUBSCRIBE, '')
    for ip in ip_addresses:
        destination = 'tcp://{}:{}'.format(ip, port)
        sock.connect(destination)
    return sock

def bound_publisher():
    sock = ctx().socket(zmq.PUB)
    sock.bind('tcp://*:{}'.format(port))
    return sock

def ui_loop():
    sock = bound_publisher()
    while True:
        line = sys.stdin.readline()
        sock.send(('<{}> '.format(sys.argv[1]) + random_color(line.strip())).encode('utf-8'))

def listen_loop():
    addresses = ip_range(sys.argv[2])
    sock = connected_subscriber(addresses)
    while True:
        print unicode(sock.recv(), 'utf-8')

if __name__ == '__main__':
    multiprocessing.Process(target=listen_loop).start()
    ui_loop()
