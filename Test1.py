# 第一个python文件

"""
input()默认输入值是string类型
不用写分号
"""
money = 5000000
name = None


name = input("请输入姓名:")
print("新添加这一行")
#添加注释


def chaxun():
    print(f"你还有{money}元")

def cunkuan(mon):
    global  money
    money = money+mon
    print(f"你还有{money}元")

def qukuan(mon):
    global  money
    money = money-mon
    print(f"你还有{money}元")

def main():

    input(f"{name}你好，请选择你要办理的业务")
    print("查询余额\t,请输入1")
    print("取款\t\t,请输入2")
    print("存款\t\t,请输入3")
    return input("亲输入您的选择")

while True:
    key=main()
    if key == "1":
        chaxun()
        continue
    elif key == "2":
        num = int(input("请输入取款金额"))
        qukuan(num)
        continue

    elif key == "3":
        num = int(input("请输入存款金额"))
        cunkuan(num)
        continue

    else:
        print("程序退出")
        break