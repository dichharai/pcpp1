import logging
import random
import time

FORMAT = 'LEVEL_NAME - TEMPERATURE_IN_CELSIUS UNIT => %(levelname)s-%(msg)s'

logger = logging.getLogger(__name__)

handler = logging.FileHandler('battery_temperature.log', mode='a')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

count = 60

while count > 0:
    c = random.randrange(20, 41)
    if c < 20:
        logger.debug(f"{c} C")
    elif c >= 30 and c <= 35:
        logger.warning(f"{c} C")
    elif c > 35:
        logger.critical(f"{c} C")
    else:
        continue
    
    time.sleep(60) # sleep for 1 minute

    count -= 1
