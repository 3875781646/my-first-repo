import sqlite3
# 连接数据库
conn = sqlite3.connect('test.db')
# 创建游标
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY,name TEXT,age INTEGER)')
cursor.execute('INSERT INTO students (name,age) VALUES (?,?)',('张三',18))
cursor.execute('SELECT * FROM students')
rows=cursor.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()

print("数据库和表创建成功！")