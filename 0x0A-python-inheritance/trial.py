#!/usr/bin/python3
class student:
   st_name ='Amit'
   st_age ='18'
   st_marks = '99'
   def demo(self):
      print(self.st_name)
      print(self.st_age)
      print(self.st_marks)

# Create objects
st1 = student()
st2 = student()

# The getattr() is used here
print ("Name = ",getattr(st1, 'st_marks'))
print ("Age = ",getattr(st2,'st_age'))
