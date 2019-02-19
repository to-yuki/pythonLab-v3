from logging import getLogger,basicConfig,INFO,WARNING,ERROR,DEBUG,CRITICAL

# フォーマットを定義
formatter = '%(asctime)s [%(levelname)-8s] %(message)s (%(filename)s:%(lineno)s)'
basicConfig(format=formatter,level=INFO)

LOGGER = getLogger(__name__)

LOGGER.debug("debug")
LOGGER.info("info")
LOGGER.warning("warn")
LOGGER.error("error")
LOGGER.critical("critical")