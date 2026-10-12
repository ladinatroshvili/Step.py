import re
text = "ჩვენი გუნდის წევრები არიან: saba.ananidze@itstep.com, მეგობარი დიმა dima123@gmail.com და კიდევ ერთი ტესტური მისამართი test_user@yahoo.com"
#refindall ის კონკრეტულ ჩანაწერში ჯემინი დავიხმარე,ამ კონკრეტულ დავალებას თუ გადავივლით ერთხელ კარგი იქნება.
emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)
sep="+"
emails_result=sep.join(emails)
print(emails_result)

