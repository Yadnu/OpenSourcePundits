from django.db import models

# Create your models here.

class Attendance_info(models.Model):
    date = models.CharField(max_length=50, null=True)
    time = models.CharField(max_length=50, null=True)
    student_id = models.IntegerField(null=True)
    student_name = models.CharField(max_length=150, null=True)
    body_temp = models.FloatField(null=True)
    attend_status = models.BooleanField(null=True)

    def __str__(self):
        return self.date

                    
    class Meta:
        db_table = 'attendance_info'



class StudentRecord(models.Model):
    student_firstName = models.CharField(max_length=50)
    student_LastName = models.CharField(max_length=50)
    student_id = models.IntegerField(null=True)


    def __str__(self):
        return str(self.student_id)


    class Meta:
        db_table = 'student_record'