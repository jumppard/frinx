import os
import logging
from logging.handlers import TimedRotatingFileHandler
import json
import psycopg2 as db

import data_layer as dl


#################################################
# INIT GLOBAL CONSTANTS
#################################################

root_folder = os.path.dirname(os.path.abspath(__file__))

logger = logging.getLogger()
handler = TimedRotatingFileHandler(root_folder + '/logs/frinx_logs.log', 'D', 30, 12)
fmt = '%(asctime)s %(levelname)s %(filename)s %(message)s [line:%(lineno)d]'
formatter = logging.Formatter(fmt=fmt, datefmt='%m/%d/%Y %H:%M:%S')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logging.info('root: ######### SCRIPT STARTED #########')
logging.info('root: app_config.json content:')
with open(root_folder + '/config_files/app_config.json', 'r') as json_file:
    app_config_data = json_file.read()
logging.info(app_config_data)
logging.info('root: BEGIN: constants initialization ...')

base_path = os.path.dirname(os.path.abspath(__file__))
db_conn = db.connect("dbname=frinx user=postgres password=emoýveRš")  # todo postgres db conn
logging.info('root: END: success (constants initialization ...)')
#################################################
# END OF INIT GLOBAL CONSTANTS
#################################################


def run():

    # load app_config.json
    with open(root_folder + '/config_files/app_config.json') as json_file:
        app_config_01 = json.load(json_file)
    relevant_interface_types = app_config_01['relevant_interface_types']

    # load configClear_v2.json
    with open(root_folder + '/config_files/configClear_v2.json') as json_file:
        input_config_json = json.load(json_file)

    # extract relevant data from json
    data = input_config_json['frinx-uniconfig-topology:configuration']['Cisco-IOS-XE-native:native']['interface']

    # main loop
    for key in data:
        if key in relevant_interface_types:
            out_data = dl.get_data(key, data[key])
            if out_data is not None:
                dl.insert(db_conn, key, out_data)


def main():
    logging.info('main: BEGIN: main application logic')
    run()
    logging.info('main: END: success (main application logic)')


if __name__ == '__main__':
    try:
        main()
        logging.info('root:  ######### SCRIPT FINISHED #########')
    except Exception as e:
        logging.error(e)
        logging.info('root:  ######### SCRIPT FINISHED #########')


