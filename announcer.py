import zmq
import time
import sys
import socket

ctx = zmq.Context()

if __name__ == '__main__':
    ip_range = sys.argv[1]
    published_ip = sys.argv[2]
    sock = ctx.socket(zmq.PUB)
    candidates = sys.argv[1].split('.')[-1]
    first, last = map(int, candidates.split('-'))
    ip_range = range(first, last)
    network = '.'.join(sys.argv[1].split('.')[:-1])
    for ip in ip_range:
        candidate = '{}.{}'.format(network, ip)
        sock.connect('tcp://{}:7314'.format(candidate, 7314))
    while True:
        sock.send(published_ip)
        time.sleep(1)
