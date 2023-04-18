#import list
import time
#先构建主菜单
def menu():
    print('*'*66)
    print('欢迎使用【宿舍管理系统】')
    print('1.查找学生')
    print('2.新增学生')
    print('3.显示全部')
    print('4.清空全部数据')
    print('0.退出系统')
    print('*' * 66)
student_data=[]
#为2.新增学生构建函数
def add_students():
    print('-'*66)
    print('新增学生')
    print('')
    id_string=input('请输入学号:')
    name_string=input('请输入姓名：')
    sex_string=input('请输入性别：')
    room_string=input('请输入房间号：')
    phone_string=input('请输入电话：')
    #构建每个人的字典
    dict={'学号':id_string,'姓名':name_string,'性别':sex_string,'房间号':room_string,'电话':phone_string}
    student_data.append(dict)
    print('添加学生%s，学号为%s，性别为%s,房间号为%s,电话号为%s'%(name_string,id_string,sex_string,room_string,phone_string))
    print('加载成功！')
#为1.查找学生构建函数
def search_students():
    print('-'*66)
    print('搜索学生')
    search_id = input('请输入要搜索的学号：')
    n=0
    for dict in student_data:
        if dict['学号'] == search_id:
            print('学号\t\t\t姓名\t\t\t性别\t\t\t房间号\t\t\t电话')
            print('=' * 66)
            print('%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s' % (dict['学号'],dict['姓名'],dict['性别'],dict['房间号'],dict['电话']))
            print('='*66)
            n=1
            break
    if n==0:
        print('-'*66)
        print('在宿管系统中并未找到该学生!')
#为3.显示全部构建函数
def show_all():
    print('-' * 66)
    print('显示所有学生')
    if len(student_data)==0:
        print('当前宿管系统并无学生，如要查询请先添加！')
    else:
        print('学号\t\t\t姓名\t\t\t性别\t\t\t房间号\t\t\t电话')
        print('=' * 66)
        for dict in student_data:
            print('%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s' % (
            dict['学号'], dict['姓名'], dict['性别'], dict['房间号'], dict['电话']))
#主程序

def sgxt_main():
    while True:
        #为了来得及看结果我选择暂停一段时间
        time.sleep(1.5)
        menu()
        command=input('请选择希望执行的操作：')
        if command=='0':
            print('正在退出系统...')
            print('欢迎再次使用【名片管理系统】')
            break
        elif command=='1':
            search_students()
        elif command=='2':
            add_students()
        elif command=='3':
            show_all()
        elif command=='4':
            student_data.clear()
        else:
            print('请仔细阅读主菜单，并输入正确的数字！')
#使用主程序
sgxt_main()