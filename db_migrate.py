import pymysql as sql
from config import Config
from secret_service import secrets

Config.DB_PASS = secrets.get_db_instance_password()

cnx = sql.connect(database=Config.DB_NAME,
                  unix_socket=Config.DB_SOCKET_DIR,
                  user=Config.DB_USER,
                  password=Config.DB_PASS)

ptCursor = cnx.cursor()
ptCursor.execute('SELECT * FROM parkFactors')
ptTypes = ptCursor.fetchall()

putCursor = cnx.cursor()
records = []

valid_from_date = sql.Date(2020, 12, 27)
valid_to_date = sql.Date(9999, 12, 31)

for ptype in ptTypes:
    params = [
        'PF',  # range type
        ptype[0],  # abbr
        ptype[1],  # name
        valid_from_date,  # valid_from
        valid_to_date,  # valid_to
        ptype[2],  # rangeHR
        ptype[3],  # range3B
        ptype[4],  # range2B
        ptype[5],  # range1B
        ptype[6],  # rangeBB
        ptype[7],  # rangeFO
        ptype[8],  # rangeK
        ptype[9],  # rangePO
        ptype[10],  # rangeRGO
        ptype[11]  # rangeLGO
    ]
    records.append(params)

putCursor.executemany(
    'INSERT INTO ranges VALUES (%s, %s, %s, DATE(%s), DATE(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', records)
cnx.commit()

newPTCursor = cnx.cursor()
newPTCursor.execute('SELECT * FROM ranges')
newPTTypes = newPTCursor.fetchall()

print(newPTTypes)
