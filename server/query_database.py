#########Pyhton3#####
import sqlite3, os

def inserter(macs, ips, operating_sys):
  conn = sqlite3.connect('db.sqlite3')
  c = conn.cursor()
  default = "INSERT INTO gameapp_identities (mac, ips, opsys) VALUES "
  insert = "('%s', '%s', '%s')" % (macs, ips, operating_sys)
  sql_statement = default + insert
  c.execute(sql_statement)
  conn.commit()
  conn.close()
def finder(mac, ips, operate_sys):
  result = ""
  conn = sqlite3.connect('db.sqlite3')
  c = conn.cursor()
  c.execute('SELECT mac from gameapp_identities')
  a = c.fetchall()
  find = 0
  for i in range(len(a)):
    b = str(a[i][0])
    if b == mac:
      find = 1
  if find == 1:
    result = "exist"
    conn.close()
  if find == 0:
    conn.close()
    result = "found"
    inserter(mac, ips, operate_sys)
  return result
