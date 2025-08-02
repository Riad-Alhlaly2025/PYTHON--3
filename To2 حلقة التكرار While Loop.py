
#************** While Loops ************
# برنامج يطلب من المستخدم ادخال كلمة السر
# ويستمر في طلبها حتى يتم ادخال الكلمة الصحيحة
# يطبع رسالة "Access Granted" عند ادخال الكلمة الصحيحة


correct_password="a1b2c3"
entered_password=input("Enter the password: ")
while entered_password != correct_password:
    print("Incorrect password. Try again.")
    entered_password=input("\nEnter the password: ")
    
print("Access Granted")
    
