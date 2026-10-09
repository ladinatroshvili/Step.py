name= input('what is your name?\n')
surname=input('what is your surname?\n')
print('Hello',name,surname,)
language=input('Which programming language is your favorite?')



now=2026
question1=input('what is your name and surname?\n')
print("hello",question1.upper())
question2=input('what is your age?\n')
birth_year= now- int(question2)
print("your birth year is",birth_year)
print('you are adult, it is',int(question2)>18)
print(name,"|", surname, "|",birth_year,"|" ,language,'|', int(question2)>18) 


# if ,და else ფუნქცია გამოვიყენე  რომ გამეკეთებინა ზღვარი 20 ქულაზე.
grade=int(input("რა ქულა მიიღე გამოცდაში"))
if grade <= 20:
    print(grade)// 2
else:
    print('მაქსიმალური ქულა არის 20')
     #ეს პატარა იმპროვიზაცია:D 
    question_2=(int(input(" ჰე ეხლა,  თქვიი რა ქულა მიიღე გამოცდაში")))
    print(int(question_2)//2)
