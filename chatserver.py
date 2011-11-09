#!/usr/bin/env python

import zmq
from time import sleep

def chat_action(f):
    """Decorator for chat action handlers."""
    f.chat_action = True
    return f

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

            action_func = self.get_action(action)
            if not action_func:
                print "Don't know how to handle action %r, args %r" % (action, args)
                continue
            action_func(args)

    def get_action(self, action):
        """Try to find a handler for the specified action."""
        if not hasattr(self, action):
            return None

        x = getattr(self, action)
        if not hasattr(x, 'chat_action'):
            return None

        return x

    @chat_action
    def say(self, args):
        target, source, message = args.split(' ', 2)
        self.pub.send("say %(target)s %(source)s %(message)s" % locals())


if __name__ == '__main__':
    ChatServer().run()
