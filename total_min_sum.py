
total=0
count=0
max_num=None
min_num=None

while True:
    user_print=input('gtxovt chawerot sasurveli ricxvi\n')
    if user_print== 'stop':
        break
    else:
        try:
            num=int(user_print)
            total+=num
            count+=1
            if max_num is None:
                max_num=num
                min_num=num
            else:
                if num >=max_num:
                     max_num=num
                if num <= min_num:
                    min_num=num
                
        except ValueError:
            print('გთხოვთ შეიყვანოთ მხოლოდ რიცხვი ან ჩაწეროთ stop')
print('რიცხვების ჯამი არის ',total)
print('რიცხვების რაოდენობა არის',count)
print('მაქსიმალური რიცხვი არის',max_num)
print('მინიმალური რიცხვი არის',min_num)


