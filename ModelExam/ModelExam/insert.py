import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelExam.settings')
from django import setup
setup()

from ModelApp.models import Tests,Tests_results,Students,Classes
import random

tests = ['数学','英語','国語']
classes = ['A','B','C','D','E','F','G','H','I','J']
students = ['A','B','C','D','E','F','G','H','I','J']
inserted_tests=[]


Tests.objects.all().delete()
Tests_results.objects.all().delete()
Students.objects.all().delete()
Classes.objects.all().delete()

for test in tests:
    test_object = Tests(name=test)
    test_object.save()
    inserted_tests.append(test_object)

for one_class in classes:
    class_object = Classes(name=one_class)
    class_object.save()
    for student in students:
        student_object = Students(name=student,grade=1,this_class = class_object)
        student_object.save()
        for test in inserted_tests:
            test_result_object = Tests_results(score=random.randint(50, 100),student = student_object,test=test)
            test_result_object.save()
            