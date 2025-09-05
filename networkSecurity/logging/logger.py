import logging
import os
from datetime import datetime

LOG_FILE  = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == "__main__":
    logging.info("Logging has been set up successfully.")



















# import logging
# import os
# from datetime import datetime

# # Create directory name based on datetime
# LOG_FOLDER = datetime.now().strftime('%m_%d_%Y_%H_%M_%S')

# # Root logs directory
# logs_root = os.path.join(os.getcwd(), "logs")

# # Subdirectory with timestamp name
# logs_path = os.path.join(logs_root, LOG_FOLDER)
# os.makedirs(logs_path, exist_ok=True)

# # Full log file path inside that directory
# LOG_FILE_PATH = os.path.join(logs_path, f"{LOG_FOLDER}.log")

# # Configure logging
# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO,
#     filemode='w'
# )

# # Export logger instance
# logger = logging.getLogger("networkSecurity")

# if __name__ == "__main__":
#     logger.info("Logging has been set up successfully.")
