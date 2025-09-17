#********* تحدي ل الفونكتشين *******

# المشروع التالي عباره عن
# 1 دالة لضرب عددين
# 2 طلب من المستخدم ادخال الرقم الذي يريد رويئة جدول الضرب له
# 3 التحقق هل المدخل من المستخدم رقم او لا
# 4 طلب منه معرفة هل يريد اضهار الزيد او لا
# 5 التحقق مما ادخل المستخدم 
def multiply (numper):
    for num in range(1,11):
        print(f"{numper} * {num} = {numper * num}")
        
        
for num in range(11):
    numper = int(input("Enter a number to multiply: "))
    if numper not in range(1, 11):
        print("Sorry, the input is wrong or not a number")
    else:
        multiply(numper)

    inquiry = input("Do you want to show a second table number Yas or not?").lower()
    if inquiry =="not":
        break
    else:
        
        numper = int(input("Enter a number to multiply: "))
        multiply(numper)
        
