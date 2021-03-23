# -*- coding = utf-8 -*-
# @Time : 2021/3/14 16:04
# @Author : 136 李嘉俊
# @File : student_methods.py
# @Software : PyCharm

# 记录所有学生列表
student_list = []
# 记录分数列表
total_list = []
# 记录添加学生人数
num = 0


def show_menu():
    """ 显示菜单 """
    menu = [

        "*-学生管理系统-*",
        "•1.新增学生",
        "•2.查询学生",
        "•3.修改学生",
        "•4.删除学生",
        "•5.遍历(排序)学生",
        "•6.修改删除查询整合",
        "•0.退出系统"

    ]

    print_star()
    for i in menu:
        print("|%s" % i.strip().center(18))
    print_star()


# 打印星星函数
def print_star():
   print("=" * 25)


# 增加学生函数
def add_student():
    """新增学生"""
    # 记录已添加的学生个数
    global num
    print("-" * 50)
    while True:
        # 1.提示用户输入学生的详细信息
        classroom_str = input("请输入班级(几班?):")
        name_str = input("请输入姓名(中文):")
        num_str = input("请输入学号(三位):")
        sex_str = input("请输入性别(男女?):")
        print("输入三门成绩：")
        # 2.使用用户输入的信息建立一个学生字典
        student_dict = {"name": name_str,
                        "classroom": classroom_str,
                        "num": num_str,
                        "sex": sex_str}
        math = int(input("请输入数学成绩:"))
        english = int(input("请输入英语成绩:"))
        chinese = int(input("请输入语文成绩:"))
        total = math + english + chinese
        average = (math + english + chinese)/3
        student_dict['math'] = math
        student_dict['english'] = english
        student_dict['chinese'] = chinese
        student_dict['total'] = total
        student_dict['average'] = average
        total_list.append(student_dict['total'])
        # 3.将学生字典添加到列表中
        student_list.append(student_dict)
        num += 1
        answer = input("是否继续添加?yes/no\n")
        # 判断是否一次输入多个学生记录
        if answer == "yes":
            continue
        else:
            break
    print("-" * 50)
    # 4.提示用户添加成功
    print("%d位学生信息添加成功" % num)


# 遍历学生函数
def show_student():
    """遍历列表"""
    print("-" * 60)
    # 打印表头
    # 判断列表是否为空
    if not student_list:
        print("没有任何记录,请新增一个学生记录")
    else:
        for name in ["班级", "姓名", "学号", "性别", "数学成绩", "英语成绩", "语文成绩", "总成绩", "平均分"]:
            print(name, end="\t\t")
        print(" ")
        print("=" * 88)
        # 打印分割线
        # 遍历学生列表以此输出字典信息
        student_new = []
        for student_dict in student_list:
            # 将遍历出来的字典重新加入新的列表中
            student_new.append(student_dict)
            print("%s\t\t%s\t%s\t\t%s\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t   %.2f" % (student_dict["classroom"],
                                                                                   student_dict["name"],
                                                                                   student_dict["num"],
                                                                                   student_dict["sex"],
                                                                                   student_dict["math"],
                                                                                   student_dict["english"],
                                                                                   student_dict["chinese"],
                                                                                   student_dict["total"],
                                                                                   student_dict["average"]))
            print("-" * 88)
        answer = input("是否进行排序？yes/no\n")
        if answer == "yes":
            # 在新的列表对总分进行重新排序
            switch = input("对一下哪项排序(1.总分 2.平均分)\n")
            if switch == "1":
                student_new.sort(key=lambda x: x['total'], reverse=True)
            else:
                student_new.sort(key=lambda x: x['average'], reverse=True)
            for name in ["班级", "姓名", "学号", "性别", "数学成绩", "英语成绩", "语文成绩", "总成绩", "平均分"]:
                print(name, end="\t\t")
            print(" ")
            print("=" * 88)
            for student_dict in student_new:
                print("%s\t\t%s\t%s\t\t%s\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t   %.2f" % (student_dict["classroom"],
                                                                                       student_dict["name"],
                                                                                       student_dict["num"],
                                                                                       student_dict["sex"],
                                                                                       student_dict["math"],
                                                                                       student_dict["english"],
                                                                                       student_dict["chinese"],
                                                                                       student_dict["total"],
                                                                                       student_dict["average"]))
            print("-" * 88)
            print("\n")
        else:
            return


# 查询学生函数
def search_info():
    """查询信息"""
    print("-" * 60)
    # 1.提示用户输入要搜索的姓名
    name_match = input("请输入要查找信息的姓名")
    # 2.遍历学生列表，查询要搜索的姓名，如果没有找到应该提示用户
    for student_dict in student_list:
        if student_dict["name"] == name_match:
            for name in ["班级", "姓名", "学号", "性别", "数学成绩", "英语成绩", "语文成绩", "总成绩", "平均成绩"]:
                print(name, end="\t\t")
            print(" ")
            print("=" * 88)
            print("%s\t\t%s\t%s\t\t%s\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t   %.2f" % (student_dict["classroom"],
                                                                                   student_dict["name"],
                                                                                   student_dict["num"],
                                                                                   student_dict["sex"],
                                                                                   student_dict["math"],
                                                                                   student_dict["english"],
                                                                                   student_dict["chinese"],
                                                                                   student_dict["total"],
                                                                                   student_dict["average"]))
            print("-" * 88)

            break

    else:
        print("输入错误或没有该学生哦~")


# 查询学生PRO
def search_pro():
    """查询信息"""
    print("-" * 60)
    # 1.提示用户输入要搜索的姓名
    name_match = input("请输入要查找信息的姓名")
    # 2.遍历学生列表，查询要搜索的姓名，如果没有找到应该提示用户
    for student_dict in student_list:
        if student_dict["name"] == name_match:
            for name in ["班级", "姓名", "学号", "性别", "数学成绩", "英语成绩", "语文成绩", "总成绩", "平均成绩"]:
                print(name, end="\t\t")
            print(" ")
            print("=" * 88)
            print("%s\t\t%s\t%s\t\t%s\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t   %.2f" % (student_dict["classroom"],
                                                                                   student_dict["name"],
                                                                                   student_dict["num"],
                                                                                   student_dict["sex"],
                                                                                   student_dict["math"],
                                                                                   student_dict["english"],
                                                                                   student_dict["chinese"],
                                                                                   student_dict["total"],
                                                                                   student_dict["average"]))
            print("-" * 88)
            deal_student(student_dict)

            break

    else:
        print("输入错误或没有该学生哦~")


# 处理学生
def deal_student(find_dict):
    """
    :param find_dict: 处理找到的学生字典
    """
    action_str = input("请输入要执行的操作 1删除 2修改 0 返回主菜单\n")
    if action_str == "1":
        student_list.remove(find_dict)
        print("删除成功了哦~")
    elif action_str == "2":
        find_dict['classroom'] = input_info(find_dict['classroom'], "请输入新的班级：[回车不输入]")
        find_dict['name'] = input_info(find_dict['name'], "请输入新的名字：[回车不输入]")
        find_dict['num'] = input_info(find_dict['num'], "请输入新的学号：[回车不输入]")
        find_dict['sex'] = input_info(find_dict['sex'], "请输入新的性别：[回车不输入]")
        find_dict['math'] = int(input_info(find_dict['math'], "请输入新的数学成绩：[回车不输入]"))
        find_dict['english'] = int(input_info(find_dict['english'], "请输入新的英语成绩：[回车不输入]"))
        find_dict['chinese'] = int(input_info(find_dict['chinese'], "请输入新的语文成绩：[回车不输入]"))
        find_dict['total'] = count_score(find_dict)
        find_dict['average'] = average_score(find_dict)
        print("学生%s信息修改成功" % find_dict['name'])


# 输入判断函数
def input_info(dict_value, tips_message):
    """

    :param dict_value: 原字典值
    :param tips_message: 用户输入信息
    :return:用户输入内容返回内容，否则返回原内容
    """
    result = input(tips_message)
    # 针对用户输入进行判断，若用户输入内容，直接返回结果，
    if len(result) > 0:
        return result
    # 如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value


# 修改学生函数
def student_revise():
    print("-" * 60)
    # 1.提示用户输入要修改的姓名
    name_match = input("请输入要修改信息的姓名")
    # 2.遍历学生列表，查询要搜索的姓名，如果没有找到应该提示用户
    for student_dict in student_list:
        if student_dict["name"] == name_match:
            for name in ["班级", "姓名", "学号", "性别", "数学成绩", "英语成绩", "语文成绩", "总成绩", "平均成绩"]:
                print(name, end="\t\t")
            print(" ")
            print("=" * 88)
            print("%s\t\t%s\t%s\t\t%s\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t   %.2f" % (student_dict["classroom"],
                                                                                   student_dict["name"],
                                                                                   student_dict["num"],
                                                                                   student_dict["sex"],
                                                                                   student_dict["math"],
                                                                                   student_dict["english"],
                                                                                   student_dict["chinese"],
                                                                                   student_dict["total"],
                                                                                   student_dict["average"]))
            print("-" * 88)

            student_dict['classroom'] = input_info(student_dict['classroom'], "请输入新的班级：[回车不输入]")
            student_dict['name'] = input_info(student_dict['name'], "请输入新的名字：[回车不输入]")
            student_dict['num'] = input_info(student_dict['num'], "请输入新的学号：[回车不输入]")
            student_dict['sex'] = input_info(student_dict['sex'], "请输入新的性别：[回车不输入]")
            student_dict['math'] = int(input_info(student_dict['math'], "请输入新的数学成绩：[回车不输入]"))
            student_dict['english'] = int(input_info(student_dict['english'], "请输入新的英语成绩：[回车不输入]"))
            student_dict['chinese'] = int(input_info(student_dict['chinese'], "请输入新的语文成绩：[回车不输入]"))
            student_dict['total'] = count_score(student_dict)
            student_dict['average'] = average_score(student_dict)
            print("学生%s信息修改成功" % student_dict['name'])
            break
    else:
        print("输入错误或没有该学生哦~")


# 删除学生函数
def student_del():
    name_match = input("请输入要删除信息的姓名")
    # 2.遍历学生列表，查询要搜索的姓名，如果没有找到应该提示用户
    for student_dict in student_list:
        if student_dict["name"] == name_match:
            print(" ")
            student_list.remove(student_dict)
            print("删除成功了哦~")
        break
    else:
        print("输入错误或没有该学生哦~")


# 计算总分函数
def count_score(find_score):
    total = find_score['math'] + find_score['english'] + find_score['chinese']
    return total


# 计算平均分函数
def average_score(find_average):
    average = (find_average['math'] + find_average['english'] + find_average['chinese'])/3
    return average
