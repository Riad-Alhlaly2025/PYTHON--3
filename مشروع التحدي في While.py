
# خمن رقم مابين 1 الى 10
# اذا كان الرقم المخمن اعلى من الرقم المحدد له تطبع لا الرقم اعلى 
# واذا كان الرقم اقل من الرقم المخمن اطبع له لا الرقم منخفض جدا
# اذا ادخل رقم مطابق للرقم اطبع له مبروك الرقم صحيح

import random
password=random.randint(1,10)
enter=int(input("Guess a number 1 and 10:"))
while enter != password:
    if enter > password:
        enter=int(input("Too high! Guess again: "))
    else:
        
        enter=int(input("Too Low! Guess again: "))
        
print("Congratulations! You guess the number!")        