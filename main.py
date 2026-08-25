"""
توی خط تقربا 27 جایی که except اجرا میشه
اول با isdigit نوشتم
ولی وقتی بار اول کاراکتر میدادی و میرفت که مجدد دریافت کنه باید حتما اینت میدادی و فلوت قبول نمیکرد 
درحالی که اگه همون بار اول فلوت میدای قبول میکرد
پس با for نوشتم
البته اینجا داره همچنان مقادیر غیر معتبر رو ذخیره میکنه
و این باعث شد وقتی کد درست ر نوشتم چون همچنان مقادیر غیر مرتبط ذخیره شده بود از اجرای قبلی وقتی داشت میخوند
اررو میداد و پیغام خطا میداد و همچان مقادیر قبلی رو نشون میداد با اینکه این سری مقادیر درست دادم
پس یا باید تابع ی جوری باشه که append نشه
یا باید فایل تکست رو پاک کنی که کل مقادیر قبلی حذف شه
که من این کارو کردم و الان از اول تمام مقادیر درست ذخیره میشه و مشکلی نیست

"""

from models.student import Student
from utils import file_manager

def student_manager():
    student_number = 0
    student_info = []
    while student_number < 3:
        try:
            student_name = input("Enter  name of student: ").strip()
            student_grade = float(input("Enter the grade of student: "))
        except:
            while True:
                user_input = input("Enter correct number for grade of student: ")
                try:
                    student_grade = float(user_input)
                    break
                except ValueError:
                    print("Enter corrent number!!!!")


            
        student_object  = Student(student_name , student_grade)  #هر ورودی رو یک شی میکنه و میریزه توی لیست
        student_info.append(student_object)
        student_number += 1
    # print(student_info)

    file_manager.save_students("student.txt" , student_info)  #چون خروجی نمیخوایی و فقط مینویسی نیازی به ریختن توی متغییر نداری
    load_info_student = file_manager.load_students("student.txt")
    if not  load_info_student:
        print("هیچ دانشجویی یافت نشد.")
    else:
        for s in  load_info_student:
            print(s.info())



student_manager()