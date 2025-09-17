
#************ (برنامج تشفير جملة ) *************
#*********************************************

#******<باستخدام الخاصية الحسابية >******

import string
# تخزين جميع الحروف بالسمول
alphabet = string.ascii_lowercase
# طلب من المستخدم ادخال جمله
word = input("Pleasse type a word: ").lower()
   
# متغير اخزن فيه الجملة بعد التشفير
encrypted = "" 
# عدد الحروف في الجملة
words=len(word)  

# لووب يتكرر بعدد الخانات في الجمله
for letter in range(words):
    # شرط التحقق من الووب
    if word[letter] in alphabet:
        # موضع الحرف المدخل 
        original_position = alphabet.index(word[letter])
        # تغيير موضع الحرف المدخل بحرف اخر 
        new_position = (original_position + 2) % 26
        # طباعة الحرف الذي يوجد في خانة الحروف 
        encrypted += alphabet[new_position]
        
    # اذا كان احد الخانات في الجمله ليست من قائمة الحروف ينفذ التالي:    
    else:
        # اضف الشكل كما هو مكتوب بدون تغيير
        encrypted += word[letter]
        
# طباعة الجملة بعد تشفيرها
print(f"Here is the encrypted word: {encrypted}")    








    
#*****************************************************
#******************************************************

#**********( برنامج تشفير جملة \ باستخدام الطريقة البديهية البسيطة ) ***********
#************************************************************************

# # دالة الحروف النصية
# import string

# # نستخدم اللوب لاضافة قائمة الحروف مرتين 
# for number in range(2):
#     alphabet = string.ascii_lowercase
# alphabet += alphabet

# # طلب من المستخدم ادخال ما يريد تشفيرة
# word = input("Pleasse type a word: ").lower()

# # متغير نخزن فيه ما يتم تشفيرة
# encrypted = ""  
 
# for loeer in word:
#     # التحقق: هل المدخل حرف
#     if loeer in alphabet:
#         # موضع الحرف المدخل 
#         original_position = alphabet.index(loeer)
#             # تغيير موضع الحرف المدخل بحرف اخر 
#         new_position = original_position +2
#             # طباعة الحرف الذي يوجد في خانة الحروف 
#         encrypted += alphabet[new_position]
        
#     # تخزين جميع الاشكال غير الحروف    
#     else:
#         if loeer not in alphabet:
#             encrypted += loeer
            
# # طباعة المدخل بعد التشفير ا               
# print(f"Here is the encrypted word: {encrypted}")    
    
        
