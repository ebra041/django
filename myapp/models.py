from django.db import models

# Create your models here.

class Student(models.Model):
      fname = models.CharField( max_length = 200)
      sname = models.CharField( max_length = 200)
      join_date = models.DateTimeField(auto_now_add=True)
      def __str__(self):
            return self.fname + self.sname

class Course(models.Model):
      cname = models.CharField ( max_length = 200)
      cduration = models.IntegerField ()
      def __str__(self):
            return self.cname

class Course_Join(models.Model):
      sid = models.ForeignKey(Student,null=True,on_delete=models.CASCADE)
      cid = models.ForeignKey(Course,null=True,on_delete=models.CASCADE)
      def __str__(self):
            return self.sid.fname + self.sid.sname + self.cid.cname
