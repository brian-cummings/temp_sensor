import get_ip
import send_email

ip = get_ip.get_ipv4('wlan0')
send_email.send_ip(ip)
