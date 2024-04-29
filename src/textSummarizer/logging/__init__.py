import os
import sys 
import logging

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(
   level=logging.INFO,
   format=logging_str,

   handlers=[
       logging.FileHandler(log_filepath),# responsible for creating file
       logging.StreamHandler(sys.stdout)# responsible for showing logs on terminal as print sattemnt

   ]


)



logger=logging.getLogger("Text-SummarizationLogger")