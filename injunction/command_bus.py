#!/usr/bin/env python

from injunction import Command


class CommandBus:

    @classmethod
    def issue_synchronous(cls, command: Command):
        handler = command.get_target()()
        handler.handle(command)

    @classmethod
    def issue_asynchronous(cls, command: Command):
        #  Implement message queue integration
        pass
