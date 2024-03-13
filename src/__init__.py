import logging
from datetime import date
import os,sys

def get_log_file_name():
    return str(date.today())+".log"

LOG_FILE_NAME=get_log_file_name()
LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE_PATH= os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode="a", # a for appending to existing file , w for overwriting
                    format="%(asctime)s - %(name)s -%(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s")

logger = logging.getLogger("ChickenDiseaseClassification")
logger.setLevel(logging.DEBUG)


class ChickenException(Exception):
    def __init__(self, error_message:Exception, error_details: sys):
        super().__init__(error_message)
        self.error_message = ChickenException.get_detailed_error_message(
            error_message,error_details)

    @staticmethod
    def get_detailed_error_message(error_message:Exception,
                                    error_detail:sys) -> str:
        """
        error_message: Exception object
        error_detail: object of sys module
        """
        _, _, exec_tb = error_detail.exc_info()
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occurred in script: [ {file_name} ] at line" \
            f"number: [{try_block_line_number}] error " \
                        f"message: [{error_message}] "

        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return str(ChickenException.__name__)
