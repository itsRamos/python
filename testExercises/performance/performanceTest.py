import logging
from parameterized import parameterized

class LogBaseClass(object):
    def __init__(self):
        self.LOG_FORMAT = "%(asctime)s, %(levelname)s, %(message)s"
        
    @classmethod
    def BaseLog(cls):
        logging.basicConfig(filename = "/home/ubuntu/workspace/exercise2/test.log", level = logging.DEBUG, format = LogBaseClass().LOG_FORMAT,filemode = 'w')
        cls.logger = logging.getLogger()
        return cls.logger
        
class LogsClass(LogBaseClass):
    def __init__(self):
        self.INFO_CODE = "4661"
        
    @staticmethod
    def GenerateLog(condition):
        logger = LogBaseClass.BaseLog()
        if (condition == 1):
            logger.info("4661, key event 1 FINALLY")
            logger.error("7140, something went wrong")
            logger.debug("7140, -1")
            logger.warning("5689, mem threshhold exceeded 51k>50k")
            logger.info("4661, key event 1 end")
        else:
            logger.info("4661, key event 1 start")
            logger.warning("5689, mem threshhold exceeded 51k>50k")
            logger.info("4661, key event 1 end")
            
            
    # @parameterized(randomizedData)
    # @parameterized([1,0,1,0,1,0,1,0,1,0])
    # @parameterized(["1","0","1","0","1","0","1","0","1","0"])
    # @parameterized([(1),(0),(1),(0),(1),(0),(1),(0),(1),(0)])
    def createLogs(self, randomizedCondition):
        test = LogsClass()
        test.GenerateLog(randomizedCondition)
    
    # def createLogs(self, randomizedCondition):
    #     test = LogsClass()
    #     test.GenerateLog(randomizedCondition)
            
        
if __name__ == "__main__":
    # LogsClass().GenerateLog()
    test = LogsClass()
    test.createLogs(1)
    test.createLogs(0)
    test.createLogs(0)
    
    # randomizedData = [(1),(0),(1),(0),(1),(0),(1),(0),(1),(0)]
    # randomizedData = [1,0,1,0,1,0,1,0,1,0]
    
    # @parameterized([1,0,1,0,1,0,1,0,1,0])
    
    # test = LogsClass()
    # test.createLogs()
    # test.createLogs(0)
    
   
