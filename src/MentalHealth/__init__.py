import os, sys, logging


log_str = "[%(asctime)s: %(levelname)s - %(module)s : %(message)s]"
log_dir = 'logs'
log_file_path = os.path.join(log_dir, "ruuning_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[logging.FileHandler(log_file_path), logging.StreamHandler(sys.stdout)]   
)

logger = logging.getLogger("MentalHealthLogger")