'''Logging is a means of tracking events that happen when some software runs.

'''
import logging
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s')

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

#Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")

'''
Levels of Log Message

There are two built-in levels of the log message.

Debug : These are used to give Detailed information, typically of interest only when diagnosing problems.
Info : These are used to Confirm that things are working as expected
Warning : These are used an indication that something unexpected happened, or indicative of some problem in the near future
Error : This tells that due to a more serious problem, the software has not been able to perform some function
Critical : This tells serious error, indicating that the program itself may be unable to continue running


'''