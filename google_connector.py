import gspread, datetime, sys
import netifaces as ni
from oauth2client.service_account import ServiceAccountCredentials

ni.ifaddresses('wlan0')
ip = ni.ifaddresses('wlan0')[2][0]['addr']

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
        print(
        'Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        worksheet = None
        sys.exit(1)

    print('Wrote a row to {0}'.format(spreadsheet))
