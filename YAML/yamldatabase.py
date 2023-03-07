import yaml
import mysql.connector
with open('yamldemo.ymi','r') as f:
    config=yaml.safe_load(f)['database']
    conn=mysql.connector.connect(
        host=config['host'],
        port=config['port'],
        database=config['dbname'],
        user=config['user'],
        password=config['password'],
        auth_plugin='mysql_native_password'
    )
cur=conn.cursor()
cur.execute("SELECT * FROM books")
rows=cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()