
import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)                      # أقصى سرعة للرسم
turtle.bgcolor("black")         # خلفية سوداء
h = 0                           # بداية درجة اللون hue

for i in range(16):             # عدد الأنماط أو الزهور الجزئية
    for j in range(18):         # عدد المنحنيات داخل كل نمط
        c = colorsys.hsv_to_rgb(h, 1, 1)   # تحويل من HSV إلى RGB
        t.color(c)              # تعيين اللون الحالي
        h += 0.005              # تغيير تدريجي في درجة اللون

        t.right(90)
        t.circle(150 - j * 6, 90)
        t.left(90)
        t.circle(150 - j * 6, 90)
        t.right(180)

    t.circle(40, 24)            # تدوير لتغيير موقع النمط التالي

turtle.done()                   # إنهاء الرسم