import pytest
import logging

logger = logging.getLogger('')

def main():
     print "-Printing the line: : : sample python file"
     print "End"
     logger.info('just an info')
     return False

if __name__== "__main__":
  main()