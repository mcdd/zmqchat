#!/usr/bin/env python

import zmq
from time import sleep


class ChatServer(object):
    def __init__(self):
        """Sets up the chat server. Basically gets the sockets ready but don't do any
        real work yet."""
        self.ctx = zmq.Context()
        self.pub = self.ctx.socket(zmq.PUB)
        self.pub.bind('tcp://*:4455')

        self.reqs = self.ctx.socket(zmq.PULL)
        self.reqs.bind('tcp://*:4456')

    def run(self):
        """Starts the message processing loop."""
        while True:
            try:
                msg = self.reqs.recv()
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
    ChatServer().run()
