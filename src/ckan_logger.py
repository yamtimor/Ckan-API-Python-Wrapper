import logging
from pathlib import Path


file_path = Path(__file__)
log_dir = file_path.parent.parent / 'log'
log_dir.mkdir(exist_ok=True)
file_name = log_dir / 'ckan-logger.log'

logging.basicConfig(filename=file_name,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.info("Running ckan")

logger = logging.getLogger(__name__)
