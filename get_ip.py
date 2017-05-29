import netifaces as ni

def get_ipv4( iface ):
    ip = None
    try:
        ip = ni.ifaddresses( iface )[ ni.AF_INET ][ 0 ][ 'addr' ]
    except:
        pass
    return ip