import sys
from src.logger import logging

class customexception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename 
    
    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
        

# Main Execution Block
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Ensure logging is configured
    logging.info('Logging has started')
    
    try:
        a = 1 / 0  # Intentional ZeroDivisionError
    except Exception as e:
        logging.error('Division by zero', exc_info=True)
        raise customexception(e, sys)
