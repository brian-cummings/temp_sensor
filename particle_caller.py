import json
import sys
import requests
import sconfig

device_id = sconfig.config_section("particle-credentials")["device-id"]
oauth = sconfig.config_section("particle-credentials")["oauth-token"]


def set_temp(web_temp):
    uri="https://api.particle.io/v1/devices/" + device_id + "/setTemp"
    headers = {'authorization': oauth}
    payload = {'args': web_temp}
    try:
        r = requests.post(url=uri, headers=headers, data=payload)
        if r.status_code == 200:
            response = json.loads(r.text)
            str_to_return = response["return_value"]
        else:
            str_to_return = str(r.status_code)
    except KeyboardInterrupt:
        sys.exit()
    except:
        str_to_return = "500"
        pass
    return str_to_return
