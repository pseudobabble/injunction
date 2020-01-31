#!/usr/bin/env python

from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def get_target(self):
        """
        Returns an uninitialised handler for the command
        """
        raise NotImplemented
