print("********** Continue **********")

#* نستخدم الكونتينيو اذا كان معانا قائمة او لوب ونريد تجاهل شي معين مثل\(continue)

for numper in range(5):
# اذا وصل عند رقم 2 يتخطاه
    if numper == 2:
        continue
    print(numper)    
    
    
print("********* Break ***********")

#* نستخدم البرييك اذا كان معانا مجموعة اشياء او لووب ونريد الطباعه والى مكان معين والتوقف مثل \(break)
    
#* مثال على اللووب
for numprs in range(6):
#* اذا وصل الووب عند الرقم 4 يطبع النص ويتوقف    
    if numprs ==4:
        print("I have to exit now ...")
        break
    print(numprs)        
    
