# -*- coding: utf-8 -*-

import yaml
import logging
from logging import config
import os


class Logger:

    @staticmethod
    def init():
        with open('util/logger/config.yaml', 'r') as f:
            dic = yaml.safe_load(f.read())
            config.dictConfig(dic)

    @staticmethod
    def release_logger():
        Logger.init()
        return logging.getLogger('release')

    @staticmethod
    def debug_logger():
        Logger.init()
        return logging.getLogger('debug')
