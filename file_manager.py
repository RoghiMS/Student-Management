from models import student

def save_students(path, students):
    """
    این تابع میاد اسم ادرس میگیره که کجا ذخیره کنه و همچنین ورودی اطلاعات
    دانشجوها رو میگیره یعنی چیزایی که باید ذخیره کنه رو
    
    """
    try:
        save_info = open(path , 'x')   #اگه فایل نبود میسازه
        for i in students:
            save_info.write(f" {i.name}, {i.grade} \n")
        save_info.close()

    except FileExistsError:  #اگه اررو داد که وجود داره میاد اینو اجرا میکنه
        save_info = open(path, 'a')
        for i in students:
            save_info.write(f"{i.name},{i.grade}\n")
        save_info.close()

    except PermissionError:
        print(f"شما اجازه نوشتن در مسیر '{path}' را ندارید")

    except Exception as e:
        print(f"خطای غیرمنتظره: {e}")
        




#تابعی که از فایل موجود اطلاعات رو میخونه-- خروجی این تابع لیستی از ابجکت ها است

def load_students(path):
    """
      این تابع میاد فایلی که توش اطلاعات ذخیره شده رو میخونه
      و خروجیش یک لیست از ابجکت است ینی رشته داخل فایل .txt 
      رو دوباره لیستی از ابجکتها میکنه
    """
    students_list = []
    try:

        read_info = open(path, 'r')
        for line in read_info:
            line = line.strip()
            if line:   # اگر خط خالی نبود
                name, grade = line.split(',')
                students_list.append(student.Student(name, float(grade)))

    except FileNotFoundError:
        # اگر فایل وجود نداشت، لیست خالی بده
        return []
    except PermissionError:
        print(f"you can not read '{path}' !")
    except Exception as e:
        print(f"the number is not int or float: {e}")
    return students_list

