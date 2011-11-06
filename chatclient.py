#!/usr/bin/env python

import zmq

def run_client():
    ctx = zmq.Context()
    sub = ctx.socket(zmq.SUB)
    sub.connect('tcp://localhost:4455')
    sub.setsockopt(zmq.SUBSCRIBE, "")

    while True:
        message = sub.recv()
        print "Got message:", message

if __name__ == '__main__':
    run_client()
