import sys
#from logger import logging

## The sys module controls program input, output and error streams, 
# enabling precise data handling beyond standard input and print functions.


def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()

    ## This exc_tb contains the data of which function and file has the exception/error occurred and all
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))
    
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message
    

#if __name__=="__main__":

#   try:
#        a=1/0
#    except Exception as e:
#        logging.info("Zero Divided Error")
#        raise CustomException(e,sys)
        