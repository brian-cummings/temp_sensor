import get_ip
import send_email
import sys


ip = get_ip.get_ipv4('wlan0')
try:
    status = send_email.send_ip(ip)
except:
    status = sys.exc_info()[0]


