a=int(input("請輸入數學成績"))
b=int(input("請輸入英文成績"))
if a >=90: and b >=90: 
    print("有獎品")
elif a <60: and b <60:
    print("不及格有處罰")
elif a <60: or b <60:
    print("再加油")