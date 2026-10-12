name=input('შეიყვანეთ თქვენი სახელი\n')
name1=name.strip().title()
surname=input('შეიყვანეთ თქვენი გვარი\n')
surname1=surname.strip().title()

list=['@gmail.com', '@itstep.ge', '@yahoo.com']
print(list)
domein=input('აირჩიეთ სასურველი დომეინი\n')
#[ამ ფუნქციით ვიყენებ რომ გამომიტანოს მხოლოდ 0 და 1 ასო]
name3=(name1[:2])
#ფორმატირებით გამომაქვს ცვლადები
print(f'{name3}{surname1}{domein}')
print()
print()
print('თქვენი ელფოსტა წარმატებით შეიქმნა')



