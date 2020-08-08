import random
def game():
    #设置初始血量
    my_hp=1000
    your_hp=1000
    #定义100~200的随机攻击力
    my_power=random.randint(100,200)
    your_power=random.randint(100,200)
    while True:
        my_hp=my_hp-your_power
        #我的剩余血量
        print(my_hp)
        your_hp=your_hp-my_power
        #你的剩余血量
        print(your_hp)
        #谁的血量先为0或负值，就跳出循环，游戏结束
        if my_hp<=0:
            print("我输了")
            break
        elif your_hp<=0:
            print("你输了")
            break
#调用函数执行游戏
game()