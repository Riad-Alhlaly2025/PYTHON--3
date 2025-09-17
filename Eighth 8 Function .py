
#* (فونكتشن لتخزين البيانات الشخصيه ) *

def information (name, age, city):
# خاصة لمتغيرات الاسم والعمر والجنسية
    print(f"My name is {name}.")
    print(f"I was born in {2025-age}. ")
    print(f"I live in {city}.")
    
# طلب من المستخدم ادخال البيانات الخاصة
# ويتم تخزين المدخل في الفونكتشن مباشره
name = input("what is your name: ")    
age = int(input("What is your age: "))
city = input("What is your city: ")

# طلب استدعاء الفونكتشن للطباعة
information(name, age, city)
