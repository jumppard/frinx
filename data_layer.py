import psycopg2 as db
import logging
import json
import business_layer as bl


def get_data(key, value):
    out = None
    if key == "BDI":
        out = bl.get_extracted_data_from_bdi(value)
    elif key == "Loopback":
        out = bl.get_extracted_data_from_loopback(value)
    if key == "Port-channel":
        out = bl.get_extracted_data_from_port_channel(value)
    elif key == "TenGigabitEthernet":
        out = bl.get_extracted_data_from_ten_gigabit_ethernet(value)
    elif key == "GigabitEthernet":
        out = bl.get_extracted_data_from_gigabit_ethernet(value)

    return out


def insert(db_conn, key, out_data):
    # https://www.postgresqltutorial.com/postgresql-python/insert/
    sql = "INSERT INTO interface(name,description,config,port_channel_id,max_frame_size) VALUES(%s, %s, %s, %s, %s)"
    insert_values_list = []
    for item in out_data:
        insert_values_list.append((item['name'], item['description'], json.dumps(item['config']), item['port_channel_id'], item['max_frame_size'],))
    try:
        logging.info('insert(): BEGIN trying to insert new records of ' + key + ' interface')
        cur = db_conn.cursor()
        cur.executemany(sql, insert_values_list)
        db_conn.commit()
        cur.close()
        logging.info('insert(): END success (trying to insert new records of ' + key + ' interface)')
    except (Exception, db.DatabaseError) as error:
        logging.error('insert(): ' + error)
        logging.warning('insert(): END failed (trying to insert new records of ' + key + ' interface)')
