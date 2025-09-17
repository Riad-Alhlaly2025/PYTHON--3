
#***********( تحدي التشفير )**********
#************************************

# عمل دالة خاصة بتاخذ التالي
#1) ادخل الرسالة التي تريد تشفيرها 
#2) ادخل رمز التشفير (رقم خطوات التغيير)
#3) اي حرف فيه حروف كبيره يجب تشفيرها وابقائها على ما هي علية كبيره

import string

    #حروف انجليزي سمول
alphabet_lower = string.ascii_lowercase.lower()
    # حروف انجليزي كابتل
alphabet_upper = string.ascii_lowercase.upper()

#* ناخذ الرسالة من المستخدم وعدد حروف الانتقال
user_message = input("Enter a massage: ")
user_shift = int(input("Enter a shift number: "))

#* الخاصة بي Function  ال 
def encrypt(message, shift):
    
    # متغير التشفير \ لتخزين فية ما تم تشفيرة
    encrypted_letter =""
    
    # تخزين بيانات لمتغيرين الفونكتشن الخاصة
    message +=alphabet_lower
    shift +=alphabet_upper
    
    # التحقق: فحص على حرف حرف 
    for letter in user_message:
        # هل الحرف موجود في قائمة حروف السمول
        if letter in message:
            # الدخول الى موضع الحرف
            original_position = message.index(letter)
            # تغيير موقع الحرف على حسب الرقم الذي ادخله المستخدم
            new_position = (original_position + user_shift)% 26
            # اضف الحرف الى متغير التشفير
            encrypted_letter += message[new_position]

        # هل الحرف موجود في قائمة الحروف الكابتل
        elif letter in shift:
            # الدخول الى موضع الحرف
            original_position = shift.index(letter)
            # تغيير موقع الحرف على حسب الرقم الذي ادخله المستخدم
            new_position = (original_position + user_shift)% 26
            # اضف الحرف الى متغير التشفير
            encrypted_letter += shift[new_position]
            
        # اذا كان الى شكل في اللوب ليس حرف ينفذ التالي    
        else:
            # اضافة في متغير التشفير بدون تغيير
            encrypted_letter += letter
            
    # طباعة متغير التشفير        
    print(encrypted_letter)
# الخاصة بي (Function)استدعاء ال
encrypt(alphabet_lower, alphabet_upper)





#*************************************************
# #**********(نفس الفكرة الكود السابق باختلاف بسيط)*****************
# import string

# def encrypt(message, shift):
#     alphabet = string.ascii_lowercase
    
#     encrypted_message = ""
    
#     # التحقق على حرف حرف 
#     for letter in message:
        
#         if letter.lower() in alphabet:
#             original_position = alphabet.index(letter.lower())
#             new_position = (original_position + shift) % 26
#             # اضف الحرف الى متغير التشفير
#             encrypted_letter = alphabet[new_position]
#             # لو كان المستخدم كاتب حرف كابتيل 
#             if letter.isupper():
#                 # نعود تحويله مثل ما ادخلة المستخدم
#                 encrypted_letter = encrypted_letter.upper()
#             # نضيفة الى الرسالة المشفرة    
#             encryptd_message += encrypted_letter    

#         # اذا كان الى شكل في اللوب ليس حرف ينفذ التالي    
#         else:
#             # اضافة في متغير التشفير بدون تغيير
#             encrypted_massage += letter
            
#     # طباعة متغير التشفير        
#     print(encrypted_message)
    
# #* ناخذ الرسالة من المستخدم وعدد حروف الانتقال
# user_message = input("Enter a massage: ")
# user_shift = int(input("Enter a shift number: "))

# # الخاصة بي (Function)استدعاء ال
# encrypt(message=user_message, shift=user_shift)
