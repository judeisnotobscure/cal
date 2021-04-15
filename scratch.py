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
## Load in customer
###############
try:
    cur.execute('''
    SELECT * FROM customer
    ''')
    customers = cur.fetchall()
    if customers != None:
        for i in customers:
            print(i)
except Exception as e:
    print("Error: {}". format(e))
##############
## Load in instrument type
# uses
###############
try:
    cur.execute('''
    SELECT * FROM instrument_uses
    ''')
    uses = cur.fetchall()
    if uses != None:
        for i in uses:
            print(i)
except Exception as e:
    print("Error: {}". format(e))

    
##########
# location

###########
try:
    cur.execute('''
    SELECT * FROM instrument_location
    ''')
    location = cur.fetchall()
    if location != None:
        for i in location:
            print(i)
except Exception as e:
    print("Error: {}". format(e))

##########
# Status
##########
try:
    cur.execute('''
    SELECT * FROM instrument_status
    ''')
    status = cur.fetchall()
    if status != None:
        for i in status:
            print(i)
except Exception as e:
    print("Error: {}". format(e))

#########
# Contam Status
#########
try:
    cur.execute('''
    SELECT * FROM contam_status
    ''')
    contam_status = cur.fetchall()
    if contam_status != None:
        for i in contam_status:
            print(i)
except Exception as e:
    print("Error: {}". format(e))
############################# dependent models
##############
## Load in Models
# models
###############
try:
    cur.execute('''
    SELECT * FROM instrument_models
    ''')
    models = cur.fetchall()
    if models != None:
        for i in range(len(models)-1):
            model = models[i]
            # print(model)
            # if model != None:
                # if model[3] != None:
                #     cur.execute('''
                #     SELECT instrument_types FROM instrument_uses 
                #     WHERE instrument_type_id = {}
                #     '''.format(model[3]))
                #     it = cur.fetchone()   
                    # it = model[3]
                    # print(it)
            
                # it=1
            # if it[0] != None:
            #     it = it[0]
            # model = (model[0], model[1], model[2], it)
            # models[i] = model
            print(model)
except Exception as e:
    print("Error: {}". format(e))
######
## Get Instruments
####
try:
    cur.execute('''
    SELECT * FROM instruments
    ''')
    instruments = cur.fetchall()
    if instruments != None:
        for i in instruments:
            print(i)
except Exception as e:
    print("Error: {}". format(e))

######
## close pg conn
####
conn.close()
###############################################################
###############################################################
#######
## open sqlite3 conn
#######
try:
    conn = sqlite3.connect("/Users/jfonz/Desktop/fleet/proj_folder/fcf2/db.sqlite3")
except Exception as e:
    print("ERROR: {}".format(e))

cur = conn.cursor()
##############
## Load in customers
###############
# for id,comp,site in customers:
#     try:
#         cur.execute('''
#         INSERT INTO customer (company_name, site_name)
#         VALUES ('{}', '{}')
#         '''.format(comp, site))
#         print("Uses uploaded")
#     except Exception as e:
#         print("Error: {}". format(e))

##############
## Load in instrument type
# uses
###############
# for id,use in uses:
#     try:
#         cur.execute('''
#         INSERT INTO instrument_uses (instrument_types)
#         VALUES ('{}')
#         '''.format(use))
#         print("uses uploaded")
#     except Exception as e:
#         print("Error: {}". format(e))

##########
# location
###########
# for id,l in location:
#     try:
#         cur.execute('''
#         INSERT INTO instrument_location (instrument_location)
#         VALUES ('{}')
#         '''.format(l))
#         print("locaiton updated")
#     except Exception as e:
#         print("Error: {}". format(e))
##########
# Status
##########
# for id,l in status:
#     try:
#         cur.execute('''
#         INSERT INTO instrument_status (instrument_status)
#         VALUES ('{}')
#         '''.format(id,l))
#         print("status updated")
#     except Exception as e:
#         print("Error: {}". format(e))
#########
# Contam Status
#########
# for id,l in contam_status:
#     try:
#         cur.execute('''
#         INSERT INTO contam_status (contam_id, contam_status)
#         VALUES ({}, '{}')
#         '''.format(id,l))
#         print("contam updated")
#     except Exception as e:
#         print("Error: {}". format(e))
################################### DEPENDENT MODELS
# conn.commit()
##############
## Load in Models
# models
###############
# for id,man,model,it in models:
#     try:
#         cur.execute('''

#         ''')
#         cur.execute('''
#         INSERT INTO instrument_models (manufacturer, model, instrument_type)
#         VALUES ('{}', '{}', {})
#         '''.format(man,model,it))
#         print("models uploaded")
#     except Exception as e:
#         print("Error: {}". format(e))
########################### fix instrument_type
######
## Get Instruments
####
for id,sn,cd,im,own,notes,location,status,contam,slug in instruments:
    try:
        cur.execute('''
        INSERT INTO instruments (instrument_id, serial_number, cal_due, instrument_model, owner, notes, location, status, contam_status, slug)
        VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}')
        '''.format(id,sn,cd,im,own,notes,location,status,contam,slug))
        print("instruments updated")
    except Exception as e:
        print("Error: {}". format(e))

######
## close conn
####
conn.commit()
cur.close()