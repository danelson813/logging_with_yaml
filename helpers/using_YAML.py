# using_YAML.py
import logging
import logging.config
import yaml

# with open('config.yaml', 'r') as f:
#     config = yaml.safe_load(f.read())
#     logging.config.dictConfig(config)


with open('config.yaml', 'r') as f:
    log_cfg = yaml.safe_load(f.read())
    logging.config.dictConfig(log_cfg)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.info('This is an info message')
logger.error('This is an error message')