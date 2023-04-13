import os
filename = 'student.txt'
def menum():
    print("==============学生信息管理系统===============")
    print("================功能菜单===================")
    print("             1.录入学生信息")
    print("             2.查找学生信息")
    print("             3.删除学生信息")
    print("             4.修改学生信息")
    print("             5.排序")
    print("             6.统计学生总人数")
    print("             7.显示所有学生信息")
    print("             0.退出系统")
    print("------------------------------------------")

def main():
    while True:
        menum()
        choise = int(input("请选择："))
        if choise in [0,1,2,3,4,5,6,7]:
            if choise==0:
                answer=input("您确定要退出系统吗？（y/n）:")
                if answer =="y" or answer =="Y":
                    print("谢谢您的使用！")
                    break #退出系统
                else:
                    continue
            elif choise ==1:
                insert()   #录入学生信息
            elif choise ==2:
                search()
            elif choise ==3:
                delect()
            elif choise ==4:
                modify()
            elif choise ==5:
                sort()
            elif choise ==6:
                total()
            elif choise ==7:
                show()

def insert():
    student_list=[]
    while True:
        id=input("请输入ID(如1000):")
        if not id:
            break
        name = input("请输入姓名：")
        if not name:
            break

        try:
            english=int(input("请输入英语成绩："))
            python =int(input("请输入python成绩："))
            java   =int(input("请输入Java成绩："))
        except:
            print("输入无效，请重新输入!")
            continue
        #将录入的学生信息保存再字典当中
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        #将学生信息添加到列表当中
        student_list.append(student)
        answer = input("是否继续添加（y/n）\n")
        if answer =='y':
            continue
        else:
            break

    #调用save函数
    save(student_list)
    print("学生信息录入完毕！！！")

def save(list):
    try:
        stu_txt=open(filename,"a",encoding='utf-8')
    except:
        stu_txt=open(filename,"w", encoding='utf-8')

    for item in list:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
    def search():
    student_query=[]
    while True:
        id=""
        name=""
        if os.path.exists(filename):
            mode=int(input("按ID查找输入1，按姓名查找输入2："))
            if mode==1:
                id= input("请输入学生ID")
            elif mode==2:
                name =input("请输入学生姓名：")
            else:
                print("您的输入有误，请重新输入")
                search()
            with open(filename,'r',encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        student_query.append(d)
                    elif name!="":
                        student_query.append(d)
            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer=input("是否要继续查询？（y/n）\n")
            if answer == 'y':
                continue
            else:
                break
        else:
            print("未保存学生信息！")
            return

def show_student(lst):
    if len(lst)==0:
        print("没有查询到学生信息，无数据显示！！！")
        return
    format_title="{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t(:^8)"
    print(format_title.format("ID","姓名","英语成绩","python成绩","java成绩","总成绩"))

    format_data="{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t(:^8)"
    for item in lst:
        print(format_data.format(item.get("id"),
                                 item.get("name"),
                                 item.get("english"),
                                 item.get("python"),
                                 item.get("java"),
                                 int(item.get("english"))+int(item.get("python"))+int(item.get("java"))
                                 ))


def delect():
    while True:
        student_id=input("请输入要删除的学生的ID：")
        if student_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old =[]
            flag=False
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print(f"id为{student_id}的学生信息已删除")
                    else:
                        print(f"没有找到ID为P{student_id}的学生信息")
            else:
                print("无学生信息")
                break
            show()
            answer=input("是否继续删除？（y/n）\n")
            if answer=='y':
                continue
            else:
                break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id = input("请输入要修改的学员的ID:")
    with open (filename,'w',encoding='utf-8') as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d['id'] ==student_id:
                print("找到了！")
                while True:
                    try:
                        d['name']=input("请输入姓名：")
                        d['english'] = input("请输入英语成绩：")
                        d['python'] = input("请输入python成绩：")
                        d['java'] = input("请输入java成绩：")
                    except:
                        print("您的输入有误，请重新输入！！！")
                    else:
                        break
                wfile.write(str(d)+'\n')
                print("修改成功")
            else:
                wfile.write(str(d)+'\n')
        answer = input("是否继续修改其他学生的信息？（y/n）")
        if answer=='y':
            modify()

def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list=rfile.readlines()
        student_new=[]
        for item in student_list:
            d=dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc=input("请选择（0.升序  1.降序）:")
    if asc_or_desc=="0":
        asc_or_desc_bool=False
    elif asc_or_desc=="1":
        asc_or_desc_bool=True
    else:
        print("您的输入有误，请重新输入")
        sort()
    mode=input("请选择排序方式（1.按英语成绩排序 2.按python成绩排序 3.按java成绩排序 0.按总成绩排序）：")
    if mode=='1':
        student_new.sort(key=lambda x: int(x['english']),reverse=asc_or_desc_bool)
    elif mode=='2':
        student_new.sort(key=lambda x: int(x['python']),reverse=asc_or_desc_bool)
    elif mode=="3":
        student_new.sort(key=lambda x: int(x['java']),reverse=asc_or_desc_bool)
    elif mode=="0":
        student_new.sort(key=lambda x: int(x['english'])+int(x['java'])+int(x['python']),reverse=asc_or_desc_bool)
    else:
        print("您的输入有误，请重新输入！！！")
        sort()
    show_student(student_new)

def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f"一共有{len(students)}名学生")
            else:
                print("还没录入学生信息")
    else:
        print("暂未保存数据信息。。。。")

def show():
    student_list=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
        for item in students:
            student_list.append(eval(item))
        if student_list:
            show_student(student_list)
    else:
        print("暂未保存数据信息")

if __name__ == '__main__':
    main()
