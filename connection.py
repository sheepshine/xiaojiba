import MySQLdb

db = MySQLdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='python-test',
    charset='utf8'
)

cursor = db.cursor()

# create table
# sql = '''CREATE TABLE TEST (
#   FIRST_NAME CHAR(20) NOT NULL
# )'''

#insert table
# sql = '''INSERT INTO TEST(FIRST_NAME) VALUES ('haha')'''
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()

#update
sql = '''SELECT * FROM TEST WHERE FIRST_NAME = "haha"'''
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    print results
except:
    print 'Error'

db.close()