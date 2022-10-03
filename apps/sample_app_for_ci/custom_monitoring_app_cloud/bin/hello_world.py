#!/usr/bin/env python

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import \
    dispatch, StreamingCommand, Configuration, Option, validators


@Configuration()
class HelloWorldCommand(StreamingCommand):
    def stream(self, events):
       # Put your event transformation code here
       for event in events:
	        event["hello"] = "world"
	        yield event 

dispatch(HelloWorldCommand, sys.argv, sys.stdin, sys.stdout, __name__)
