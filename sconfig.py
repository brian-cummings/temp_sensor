import ConfigParser
import os

file_path = os.getcwd() + "/config.ini"
config = ConfigParser.ConfigParser()
config.read(file_path)


def config_section(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
