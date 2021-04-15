import fnmatch, os, os.path, datetime, re
import psycopg2 as pg
import shutil
import pandas as pd
import sqlite3
#################
# Create database connection to pg
#################
try:
    conn = pg.connect("dbname='fleet' user='admin' host='localhost' password=''")
except Exception as e:
    print("ERROR: {}".format(e))

cur = conn.cursor()

##############
## Load in Models
# models
###############
# try:
#     cur.execute('''
#     SELECT * FROM instrument_models
#     ''')
#     models = cur.fetchall()
#     if models != None:
#         for i in range(len(models)-1):
#             model = models[i]
#             # print(model)
#             if model != None:
#                 if model[3] != None:
#                     cur.execute('''
#                     SELECT instrument_types FROM instrument_uses 
#                     WHERE instrument_type_id = {}
#                     '''.format(model[3]))
#                     it = cur.fetchone()
#             else:
#                 it=1
#             if it[0] != None:
#                 it = it[0]
#             model = (model[0], model[1], model[2], it)
#             models[i] = model
# except Exception as e:
#     print("Error: {}". format(e))

######
## Get Instruments
####
try:
    cur.execute('''
    SELECT * FROM instruments
    ''')
    instruments = cur.fetchall()
    if instruments != None:
        for i in range(len(instruments)-1):
            instrument = instruments[i]
            cur.execute('''
                    SELECT model FROM instrument_model 
                    WHERE id = {}
                    '''.format(instrument[3]))
 ###################################                   
            model = cur.fetchone()
  ###################################
            cur.execute('''
                    SELECT site_name FROM customer 
                    WHERE id = {}
                    '''.format(instrument[4]))              
            site_name = cur.fetchone()
 ###################################
            cur.execute('''
                SELECT instrument_location FROM instrument_location 
                WHERE id = {}
                '''.format(instrument[6]))              
            instrument_location = cur.fetchone()
  ###################################
            cur.execute('''
                SELECT instrument_location FROM instrument_location 
                WHERE id = {}
                '''.format(instrument[6]))              
            instrument_location = cur.fetchone()
except Exception as e:
    print("Error: {}". format(e))