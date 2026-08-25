"""
این فایل برای اینکه هر دانشجویی که از کاربر گرفته شده و ذخیره شده
میاد جدا جدا برای هر شی  یکسری عملیاتی انجام میده
که البته اینجا فقط اطلاعاتشونو چاپ میکنه
# در حالت کلی این قطعه کد شی میسازه و روش کار انجام میده
"""
class Student:
    def __init__(self, name , grade:float):
        self.name = name
        self.grade = grade

    def info(self):
        return f"Student : {self.name} - Grade: {self.grade}"
