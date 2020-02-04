#!/usr/bin/env python

from injunction import Command
from injunction import CommandHandler
from injunction import CommandBus


class HandlerDependency:

    def mutate_output(self, stuff_in: str):
        return stuff_in + ': MUTATED'


class Greet(Command):

    def __init__(self, greeting):
        self.greeting = greeting

    def get_target(self):
        return Greeter


class Greeter(CommandHandler):

    def __init__(self, handler_dependency=HandlerDependency):
        self.handler_dependency = handler_dependency()

    def handle(self, command: Greet):
        greeting = self.handler_dependency.mutate_output(command.greeting)
        print(greeting)


if __name__ == '__main__':

    hello = Greet('hello there')

    CommandBus.issue_synchronous(hello)
