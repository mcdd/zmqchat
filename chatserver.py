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

        try:
            action, args = msg.split(' ', 1)
        except ValueError:
            print "discarding invalid message: %r" % (msg,)
            continue
        print "TODO: handle message"


if __name__ == '__main__':
    run_server()
