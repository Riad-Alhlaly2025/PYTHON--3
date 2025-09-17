
#*** Function to greet the user **********
# عمل فونكتشن ابتدائية بسيطة خاصه
#         وتخزين فيها رسائل ترحيب وتهنئة 

# اكتب برنامج يطلب من المستخدم ادخال اسمة
# اذا كان الاسم المدخل هو "رياض استدع الفونكتشن الخاصة بامر طباعة
# واذا الاسم المدخل ليس "رياض"
# اطبع له رسالة اعتذار 

def greet():
    print("Hello there!")
    print("Long time no see! ")
    
name = input("What is your name : ").lower()
if name == "riad":
    greet()
else:

    print("Sorry, I can't assist with that.")    
