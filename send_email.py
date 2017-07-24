import sys
from sparkpost import SparkPost
import sconfig
import socket

sp_token = sconfig.config_section("spark-config")["spark-token"]
recipient = sconfig.config_section("spark-config")["recipient"]
hostname = socket.gethostname()
sp = SparkPost(sp_token)


def send_ip(ip):
    try:
        status = sp.transmissions.send(
            recipients=[recipient],
            template="pi-online",
            substitution_data={
                "ip": ip,
                "hostname": hostname
            }
        )
    except:
        status = sys.exc_info()[0]
    return status
