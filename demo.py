#!/usr/bin/env python

from injunction import Command
from injunction import CommandHandler
from injunction import CommandBus


class Greeting(Command):

    def __init__(self, greeting):
        self.greeting = greeting

    def get_target(self):
        return Greeter


class Greeter(CommandHandler):

    def handle(self, command: Greeting):
        print(command.greeting)


if __name__ == '__main__':

    hello = Greeting('hello there')

    CommandBus.issue_synchronous(hello)
