#!/usr/bin/env python

import zmq
from time import sleep

def run_server():
    ctx = zmq.Context()
    pub = ctx.socket(zmq.PUB)
    pub.bind('tcp://*:4455')

    reqs = ctx.socket(zmq.PULL)
    reqs.bind('tcp://*:4456')

    i = 0
    while True:
        msg = reqs.recv()
        print "got message, relaying to other nodes"
        pub.send(msg)

if __name__ == '__main__':
    run_server()
