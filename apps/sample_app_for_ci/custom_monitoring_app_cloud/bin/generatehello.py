#!/usr/bin/env python
# coding=utf-8
#
# Copyright © 2011-2015 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from __future__ import absolute_import, division, print_function, unicode_literals
import os,sys
import time
from random import randint
import splunk
import logging, logging.handlers


splunkhome = os.environ['SPLUNK_HOME']
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

libdir = os.path.realpath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "lib"))
sys.path.append(libdir)

from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators
from splunklib.six.moves import range


def setup_logging():
    logger = logging.getLogger('splunk.butter')
    #SPLUNK_HOME = os.environ['SPLUNK_HOME']

    LOGGING_DEFAULT_CONFIG_FILE = os.path.join('/opt/splunk', 'etc', 'log.cfg')
    LOGGING_LOCAL_CONFIG_FILE = os.path.join('/opt/splunk','etc', 'log-local.cfg')
    LOGGING_STANZA_NAME = 'python'
    LOGGING_FILE_NAME = "custom_monitoring_app_cloud.log"
    BASE_LOG_PATH = os.path.join('var', 'log', 'splunk')
    LOGGING_FORMAT = "%(asctime)s %(levelname)-s\t%(module)s:%(lineno)d - %(message)s"
    splunk_log_handler = logging.handlers.RotatingFileHandler(os.path.join('/opt/splunk', BASE_LOG_PATH, LOGGING_FILE_NAME), mode='a')
    splunk_log_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))
    logger.addHandler(splunk_log_handler)
    splunk.setupSplunkLogger(logger, LOGGING_DEFAULT_CONFIG_FILE, LOGGING_LOCAL_CONFIG_FILE, LOGGING_STANZA_NAME)
    return logger

@Configuration()
class GenerateHelloCommand(GeneratingCommand):
    count = Option(require=True, validate=validators.Integer(0))
 
    def generate(self):
        logger = setup_logging()
        logger.warn("Too many requests detected by application")
        for i in range(1, self.count + 1):
            text = 'Hello World %d' % i
            yield {'_time': time.time(), 'event_no': i, '_raw': text}
 
dispatch(GenerateHelloCommand, sys.argv, sys.stdin, sys.stdout, __name__)