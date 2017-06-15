import gspread
import datetime
import sys
import get_ip
from oauth2client.service_account import ServiceAccountCredentials

ip = get_ip.get_ipv4('wlan0')
GDOCS_OAUTH_JSON = 'API Project-eecc64142440.json'


def append_to_sheet(spreadsheet, temp, humidity):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    try:
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(GDOCS_OAUTH_JSON, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1
        worksheet.append_row((datetime.datetime.now(), temp, humidity, ip))
    except Exception as ex:
        worksheet = None
        sys.exit(1)


