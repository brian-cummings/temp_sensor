#!/usr/bin/python

import Adafruit_DHT, logging.handlers, os, time, google_connector

file_path = os.getcwd()
logger = logging.getLogger("temp_sensor")

log_handler = logging.handlers.TimedRotatingFileHandler(file_path + "/logs/sensor.log", when="midnight", backupCount=5)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)
# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT22



pin = 22
while(True):
# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temperature = temperature * 1.8 + 32


    if humidity is not None and temperature is not None:
        message = 'Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature, humidity)
        try:
            google_connector.append_to_sheet("temp_sensor",temperature,humidity)
        except KeyboardInterrupt:
            raise
        except:
            message = 'Google connector failed'
            pass
    else:
        message = 'Failed to get reading. Try again!'
    logger.info(message)
    time.sleep(30)
