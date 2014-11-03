import sys
import zmq

ctx = zmq.Context()

if __name__ == '__main__':
    server = sys.argv[1]
    req = ctx.socket(zmq.REQ)
    req.connect('tcp://{}:7313'.format(server))
    req.send('hello')
    print req.recv()
