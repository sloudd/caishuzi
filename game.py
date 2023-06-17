import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("欢迎参加猜数字游戏！")
    print("我已经想好了一个1到100之间的秘密数字。")

    while True:
        guess = int(input("请猜一个数字："))
        attempts += 1

        if guess < secret_number:
            print("太小了，请再试一次！")
        elif guess > secret_number:
            print("太大了，请再试一次！")
        else:
            print("恭喜你！你猜对了！")
            print("你猜了", attempts, "次。")
            break

guess_number()
