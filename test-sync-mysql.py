#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Marcos V. M. Araujo
# Created Date: 08-13-2021
# version ='0.1'
# ---------------------------------------------------------------------------


import MySQLdb # para o MySQL
import uuid
import time

host_a = "10.0.21.209"
host_b = "10.0.21.210"
user = "master"
passwd = "Neopath123!"
db_name = "opensips_3_1"

def ExecuteSQLCreate(host, user, passwd, sql):
    con = MySQLdb.connect(host=host, user=user, passwd=passwd)
    con.select_db(db_name)
    cursor = con.cursor()
    resultSQL = cursor.execute(sql)
    con.commit()
    #print ("resultSQL=",resultSQL)
    con.close()

def ExecuteSQLRead(host, user, passwd, sql):
    con = MySQLdb.connect(host=host, user=user, passwd=passwd)
    con.select_db('opensips_3_1')
    cursor = con.cursor()
    resultSQL = cursor.execute(sql)
    #print ("resultSQL=",resultSQL)
    results = cursor.fetchall()
    con.close()
    return results  



sql = "SELECT * FROM subscriber"

resultsa = ExecuteSQLRead (host_a,user,passwd,sql)
resultsb = ExecuteSQLRead (host_b,user,passwd,sql)

print ("Count DB A:",len(resultsa))

print ("Count DB B:",len(resultsb))

print ("Inserting data")
for i in range(10000):     
    guid = uuid.uuid4() 
    sql= "INSERT INTO subscriber (username,domain,password,email_address ) VALUES ('%s', 'neo.neo', 'Neopath123!', '');"%(guid)
    ExecuteSQLCreate(host_b,user,passwd,sql)

time.sleep(2)

sql = "SELECT * FROM subscriber"

resultsa = ExecuteSQLRead (host_a,user,passwd,sql)
resultsb = ExecuteSQLRead (host_b,user,passwd,sql)

print ("Count DB A:",len(resultsa))
print ("Count DB B:",len(resultsb))

if len(resultsa) == len(resultsb):
    print ("SYNC OK")
else:
    print ("SYNC NOK")
