import utils
utils.print_loop()
utils.print_multiplication_table()
from database_manager import DatabaseManager
def main():
    db=DatabaseManager('school.db')
    while True:
        print('1.添加学生')
        print('2.查看所有学生')
        print('3.退出')
        choice=input('请输入（1/2/3）:')
        if choice=='1':
            name=input('请输入学生姓名：')
            age=int(input('请输入学生年龄：'))
            db.insert_student(name,age)
        elif choice=='2':
            rows=db.select_all_students()
            if not rows:
                print('列表为空')
            else:
                for row in rows:
                    print(f'id:{row[0]},name:{row[1]},age:{row[2]}')
        elif choice=='3':
            db.close()
            print('再见')
            break
        else:
            print('无效选项')
main()

