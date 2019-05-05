"""Exercise 2 Preface
We have the following log output for a repeating “key event 1” event of interest
•	2018-06-29 08:39:35.401675, INFO, 	  4661,  key event 1 start
•	2018-06-29 08:39:40.336308, ERROR, 	  7140,  something went wrong
•	2018-06-29 08:39:51.766684, DEBUG, 	  7140,  -1
•	2018-06-29 08:39:52.982564, WARNING,  5689,  mem threshold exceeded 51K>50k
•	2018-06-29 08:39:53.013554, INFO,     4661,  key event 1 end
•	...
•	...
•	2018-06-29 09:41:12.002756, INFO, 	  4661,  key event 1 start
•	2018-06-29 09:41:26.114254, WARNING,  8799,  mem threshold exceeded 54K>50k
•	2018-06-29 09:41:26.897602, INFO,     4661,  key event 1 end

This program will measure the performance of key event 1. (Code assignments in full)

Author: Erick Ramos
Date: July 30, 2018
"""

import logging
import time

class LogBaseClass(object):
    """Represents the base class that sets up the log configuration and sets default values"""
    
    def __init__(self):
        self.LOG_FORMAT = "%(asctime)s, %(levelname)s, %(message)s"
        self.FILENAME = "/home/ubuntu/workspace/exercise2/test.log"
        self.LOG_LEVEL = logging.DEBUG
        self.FILE_MODE = 'w'
        
    @classmethod
    def BaseLog(cls):
        logging.basicConfig(filename = LogBaseClass().FILENAME, 
                            level = LogBaseClass().LOG_LEVEL, 
                            format = LogBaseClass().LOG_FORMAT,
                            filemode = LogBaseClass().FILE_MODE)
        cls.logger = logging.getLogger()
        return cls.logger
        
class LogsClass(LogBaseClass):
    """Represents the log class that automates the logs and captures each time to calculate the performance"""

    def __init__(self):
        self.INFO_CODE = "4661"
        
    @staticmethod
    def GenerateLog(condition):
        logger = LogBaseClass.BaseLog()
        
        if (condition==1):
            logger.info("4661, key event 1 start")
            t1_start = time.perf_counter()
            time.sleep(17.611879)

            logger.error("7140, something went wrong")
            logger.debug("7140, -1")
            logger.warning("5689, mem threshhold exceeded 51k>50k")
            t1_stop = time.perf_counter()
            logger.info("4661, key event 1 end set end flag here\n")
            logger.info("Elapsed time of key event 1: %.4f seconds\n" % ((t1_stop-t1_start)))
        
        else:
            logger.info("4661, key event 1 start")
            t2_start = time.perf_counter()
            time.sleep(14.894846)
            logger.warning("5689, mem threshhold exceeded 51k>50k")
            t2_stop = time.perf_counter()
            logger.info("4661, key event 1 end\n")
            logger.info("Elapsed time: %.4f seconds\n" % ((t2_stop-t2_start)))
            
    def createLogs(self, randomizedCondition):
        test = LogsClass()
        test.GenerateLog(randomizedCondition)
        
        
if __name__ == "__main__":
    BEST_CASE_DATA = [0,0,0,0,0,0,0,0,0,0]
    WORST_CASE_DATA = [1,1,1,1,1,1,1,1,1,1]
    
    test = LogsClass()
    
    for i in BEST_CASE_DATA:
        test.createLogs(i)
    
    for i in WORST_CASE_DATA:
        test.createLogs(i)
