#!/usr/bin/env python

import zmq
from time import sleep

def run_server():
    ctx = zmq.Context()
    pub = ctx.socket(zmq.PUB)
    pub.bind('tcp://*:4455')

    reqs = ctx.socket(zmq.PULL)
    reqs.bind('tcp://*:4456')

    while True:
        try:
            msg = reqs.recv()
        except KeyboardInterrupt:
            print "\nClosing gracefully..."
            return
        else:
            print "got message, relaying to other nodes"
            pub.send(msg)
            

if __name__ == '__main__':
    run_server()
