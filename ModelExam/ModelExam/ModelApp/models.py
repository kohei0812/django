from django.db import models

# Create your models here.

class Tests(models.Model):
    name = models.CharField(max_length=50)
      
    class Meta:
        db_table = 'tests'
        
class Tests_results(models.Model):
    score = models.IntegerField()
    student = models.ForeignKey(
        'Students', on_delete=models.CASCADE
    )
    test = models.ForeignKey(
        'Tests', on_delete=models.CASCADE
    )
    class Meta:
        db_table = 'tests_results'
        
class Students(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField()
    this_class = models.ForeignKey(
        'Classes', on_delete=models.CASCADE
    )
    class Meta:
        db_table = 'students'
        
class Classes(models.Model):
    name = models.CharField(max_length=50)
   
    class Meta:
        db_table = 'classes'