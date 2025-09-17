

#****( برنامج فك الرسائل المشفرة )****
#* استيراد مكتبة string
#*  لتخزين الحروف الانجليزية
#*  لتسهيل عملية فك رسالة التشفير
#*******************************
# *** الخطوات ***
# 1- طلب من المستخدم  ادخال الرسالة المشفره
# 2- طلب من المستخدم ادخال مفتاح التي تم التشفير بها
# 3- انشاء دالة خاصة بي لفك التشفير
# 4- استدعاء الدالة مع تمرير القيم المدخلة
# 5- طباعة الرسالة بعد فك التشفير
#*******************************    
import string

    #حروف انجليزي سمول
alphabet_lower = string.ascii_lowercase.lower()
    # حروف انجليزي كابتل
alphabet_upper = string.ascii_lowercase.upper()

#* ناخذ الرسالة من المستخدم وعدد حروف الانتقال
user_message = input("Enter a massage: ")
user_shift = int(input("Enter a shift number: "))

#* الخاصة بي Function  ال 
def decrypt(message, shift):
    
    # متغير التشفير \ لتخزين فية ما تم تشفيرة
    decrypted_message =""
    
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
            new_position = (original_position - user_shift)% 26
            # اضف الحرف الى متغير التشفير
            decrypted_message += message[new_position]

        # هل الحرف موجود في قائمة الحروف الكابتل
        elif letter in shift:
            # الدخول الى موضع الحرف
            original_position = shift.index(letter)
            # تغيير موقع الحرف على حسب الرقم الذي ادخله المستخدم
            new_position = (original_position - user_shift)% 26
            # اضف الحرف الى متغير التشفير
            decrypted_message += shift[new_position]
            
        # اذا كان الى شكل في اللوب ليس حرف ينفذ التالي    
        else:
            # اضافة في متغير التشفير بدون تغيير
            decrypted_message += letter
    
    
    # طباعة السطر التالي قبل رسالة التشفير
    print("\nHere is the original message\n******\n")
    
    # طباعة متغير التشفير        
    print(f"{decrypted_message}\n\n******")
# الخاصة بي (Function)استدعاء ال
decrypt(alphabet_lower, alphabet_upper)
