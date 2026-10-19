
while True:
    try:
        height=int(input(('შეიყვანეთ რიცხვი 1 დან 10 ის ჩათვლით')))
        if 1<=height<=10:
            break
        else:
            print('სიმაღლე უნდა იყოს 1 დან 10 ის ჩათვლით')
    except ValueError:
        print('გთხოვთ შეიყვანოთ მთელი რიცხვი')

print('ახლა აიგება შენი პირამიდა')

for row in range(1,height+1):
    for space in range(height - row):
        print(' ', end='')
    for i in range(row):
        print('#',end='')
    print()
    





