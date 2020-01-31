#!/usr/bin/env python

from abc import ABC, abstractmethod

from injunction import Command


class CommandHandler(ABC):

    @abstractmethod
    def handle(self, command: Command):
        """
        This method will be called by the CommandBus
        with the Command as the argument.

        Implement logic to operate with/on the Command's
        properties.

        :param command: Command
        """
        raise NotImplemented
