import random
r = random.randint(1, 100)
while True:
    g = input('請猜數字 1 ~ 100 (整數) :  ')
    g = int(g) 
    if g < 1 or g > 100:
        print('再來一次，只能輸入 1 ~ 100 整數')   
    elif g == r:
        print('答案為', r, '恭喜答對了')
        break
    else:
        print('可惜猜錯囉，再試一次吧!')
        if g > r:
            print('答案比', g, '還要小喔')
        else:
            print('答案比', g, '還要大喔')
            
