import pymysql

def connection():
    conn = pymysql.connect(host='localhost',
                           database='database',
                           user='root',
                           password='mysqlpwd')
    c = conn.cursor()

    return c, conn

# CREATE TABLE tests (test_id VARCHAR(50), test_name VARCHAR(50), owner_email VARCHAR(40), frequency VARCHAR(20), last_run VARCHAR(15));
# INSERT INTO tests (test_id, test_name, owner_email, frequency, last_run) values ('id','testname', 'owner@email.com', 'hourly', 'Never');
