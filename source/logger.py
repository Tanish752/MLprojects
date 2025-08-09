import logging
import os
from datetime import datetime

log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), 'logs', log_file)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)
logging.basicConfig(
	filename=logs_path,
	level=logging.INFO,
	format='%(asctime)s - %(levelname)s - %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S'
)
log_file_path = os.path.join(logs_path, log_file)
logging.basicConfig(
	filename=log_file_path,
	level=logging.INFO,
	format='%(asctime)s - %(levelname)s - %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S'
)

if __name__ == "__main__":
	logging.info("Logging has started.")