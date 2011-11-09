#!/usr/bin/env python

import zmq
from sys import stdin

def run_client():
    ctx = zmq.Context()
    sub = ctx.socket(zmq.SUB)
    sub.connect('tcp://localhost:4455')
    sub.setsockopt(zmq.SUBSCRIBE, "")

    push = ctx.socket(zmq.PUSH)
    push.connect('tcp://localhost:4456')

    plr = zmq.Poller()
    plr.register(stdin.fileno(), zmq.POLLIN)
    plr.register(sub, zmq.POLLIN)

    while True:
        try:
            fds = dict(plr.poll())
        except KeyboardInterrupt:
            print "\nClosing gracefully..."
            return

        if stdin.fileno() in fds:
            line = stdin.readline()[:-1] # trim newline char
            push.send(line)

        if sub in fds:
            msg = sub.recv()
            print "Got message: %r" % (msg,)

if __name__ == '__main__':
    run_client()
