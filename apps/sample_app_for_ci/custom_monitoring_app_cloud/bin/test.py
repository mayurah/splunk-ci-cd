
from random import randint
import os
import splunk
import logging, logging.handlers
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration


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

# for lab brevity, just return a random number from 1 to 5!
def getAvgReviewScore():
   logger = setup_logging()
   randomReview = randint(1,5)
   if (randomReview == 3 or randomReview == 4) :
      logger.warn("Generating error for custom user log file")
   
   return str(randomReview)

@Configuration()
class GetReviewScoresCommand(StreamingCommand):
   def stream(self, events):
      for event in events:
         event["review"] = getAvgReviewScore()
         yield event

if __name__ == "__main__":
   dispatch(GetReviewScoresCommand, sys.argv, sys.stdin, sys.stdout, __name__)