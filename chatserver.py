#!/usr/bin/env python

import zmq
from time import sleep

def run_server():
    ctx = zmq.Context()
    pub = ctx.socket(zmq.PUB)
    pub.bind('tcp://*:4455')

    i = 0
    while True:
        pub.send("message %d" % i)
        i += 1
        sleep(1)

if __name__ == '__main__':
    run_server()
