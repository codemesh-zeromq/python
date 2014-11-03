import zmq

ctx = zmq.Context()

if __name__ == '__main__':
    rep = ctx.socket(zmq.REP)
    rep.bind('tcp://*:7313')
    while True:
        hello = rep.recv()
        print hello
        if hello.lower() == 'hello':
            rep.send("world")
        else:
            raise Exception("Broken client")
