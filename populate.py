import fnmatch, os, os.path, datetime, re
import sqlite3 as sq
import shutil
import pandas as pd
import os
from pathlib import Path

#################
# Create database connection
#################
try:
    conn = sq.connect("db.sqlite3")
except Exception as e:
    print("ERROR: {}".format(e))

cur = conn.cursor()

#################
## Import excel data
##################
BASE_DIR = Path(__file__).resolve().parent

df = pd.read_excel(os.path.join(BASE_DIR, 'instruments.xlsm'), sheet_name="Duane_Arnold")
new_header =  df.iloc[0] # grab second row for header
df = df[1:] # strip data from header up
df.columns = new_header




#################
## Data Processing
##################

def get_serial_number(i):
    if type(i) == str:
        return i
    if len(str(i))>3:
        return str(i)
    else:
        return 'none'

def get_instrument_model(i):
    #Unknown = 24
    if type(i) ==str:
        try:
            cur.execute('''
            SELECT id FROM instrument_models WHERE UPPER(model) LIKE '{}'
            '''.format(i.upper()))
            result = cur.fetchone()[0]
            return str(result)
        except Exception as e:
            print(e)
    else:
        return '24'

def get_location(i):
    # unknown = 9
    if type(i)==str:
        try:
            cur.execute('''
            SELECT location_id FROM instrument_location WHERE UPPER(instrument_location) LIKE '{}%'
            '''.format(i[0:3].upper()))
            result = cur.fetchone()[0]
            if result != None:
                return str(result)
            else:
                return '9'
        except Exception as e:
            print(e)
    else:
        return '9'

def get_status(i):
    # unknonw = 6
    if type(i)==str:
        if i == "Recieved":
            return '3'
        if i == "Processed":
            return '4'
        if i == "Returned":
            return '5'
        else: 
            return '6'
    else: 
        return '6'

def get_contam_status(i):
    # unknown = 3
    if type(i) == str:
        if i.upper() == "YES":
            return '2'
        if i.upper() == "NO":
            return '1'
        else:
            return '3'
    else:
        return '3'

def get_cal_due(i):
    standard = '2000-01-01'
    if type(i) == datetime.datetime:
        return i.strftime("%Y-%m-%d")
    else:
        return standard

def get_notes(i):
    if type(i) == str:
        return i
    else:
        return 'none'
#################
# Create json file
#################
FIXTURE_DIR = os.path.join(os.path.join(BASE_DIR, 'instruments'), 'fixtures')
fixture = open(os.path.join(FIXTURE_DIR, "fixtures.json"), 'a')
n = 1

for index, row in df.iterrows():   
    serial_number = get_serial_number(row[0])
    instrument_model = get_instrument_model(row[1]) # fk
    owner = '1' # fk 1 for Duane arnold
    cal_due = get_cal_due(row[2])
    notes = get_notes(row[9])
    location = get_location(row[8])  # fk
    status = get_status(row[7])  # fk
    contam_status = get_contam_status(row[3])   # fk
    pk = str(n)

    try:
                fixture.write('''
                {"model": "instruments.Instrument",
                    "pk":'''+pk+''',
                    "fields":{
                        "serial_number": "'''+serial_number+'''",
                        "instrument_model": '''+instrument_model+''',
                        "owner": '''+owner+''',
                        "cal_due": "'''+cal_due+'''",
                        "notes": "'''+notes+'''",
                        "location": '''+location+''',
                        "status": '''+status+''',
                        "contam_status": '''+contam_status+'''
                    }
                },
                ''')
                
    except Exception as e:
            print(e)
    n += 1  
    print("{} populated".format(serial_number))      
fixture.close()        
conn.commit()
cur.close()
conn.close()

if __name__ == "__main__":
    print(BASE_DIR)