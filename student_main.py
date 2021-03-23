# -*- coding = utf-8 -*-
# @Time : 2021/3/14 16:04
# @Author : 136 李嘉俊
# @File : student_main.py
# @Software : PyCharm

import student_methods
# 无限循环，由用户决定循环是否退出
while True:
    # TODO 显示功能菜单
    student_methods.show_menu()
    action_str = input("输入功能键：")
    print("你选择的操作是" + action_str)
    # 成员运算符,判断用户输入是否在指定列表内
    if action_str in ["1", "2", "3", "4", "5", "6"]:
        # TODO 新增学生
        if action_str == "1":
            student_methods.add_student()
        # TODO 查询学生
        elif action_str == "2":
            student_methods.search_info()
        # TODO 修改学生
        elif action_str == "3":
            student_methods.student_revise()
        # TODO 删除学生
        elif action_str == "4":
            student_methods.student_del()
        # TODO 遍历(排序)学生
        elif action_str == "5":
            student_methods.show_student()
        # TODO 查询修改删除整合
        elif action_str == "6":
            student_methods.search_pro()
    elif action_str == "0":
        print("欢迎再来哦~")
        break

    else:
        print("输入错误,请重新输入:")
