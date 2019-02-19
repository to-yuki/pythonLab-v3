from logging import Formatter,getLogger,basicConfig ,INFO,WARNING,ERROR,DEBUG,CRITICAL

# フォーマットを定義
formatter = '%(levelname)s : %(asctime)s : %(message)s'
basicConfig(format=formatter,level=INFO)

LOGGER = getLogger(__name__)

LOGGER.debug("debug")
LOGGER.info("info")
LOGGER.warning("warn")
LOGGER.error("error")
LOGGER.critical("critical")