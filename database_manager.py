import sqlite3
class DatabaseManager:
    def __init__(self,db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
        )
        ''')
    def insert_student(self, name, age):
        self.cursor.execute('''INSERT INTO students(name, age) VALUES(?,?)''',(name,age))
        self.conn.commit()
    def select_all_students(self):
        self.cursor.execute('''SELECT * FROM students''')
        return self.cursor.fetchall()
    def close(self):
        self.conn.commit()
        self.conn.close()
if __name__ == '__main__':
    db = DatabaseManager('school.db')
    db.create_table()
    db.insert_student('王五', 21)
    rows = db.select_all_students()
    for row in rows:
        print(row)
    db.close()