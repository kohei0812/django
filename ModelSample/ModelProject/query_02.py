import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students,Person
print(Students.objects.all())

# IN
ids = [13,14,15]
print(Students.objects.filter(pk__in=ids).all())

# contain 部分一致
print(Students.objects.filter(name__contains='三').all())

# is null
print(Person.objects.filter(salary__isnull=True).all())

# レコードを取り除く（filter => exclude）
print(Person.objects.exclude(salary__isnull=True).all())

# 一部のカラムを取り除く
students = Students.objects.values('name','age').all()
for student in students:
    print(student['name'])
    
# 並び替え
print(Students.objects.order_by('name').all())
print(Students.objects.order_by('name','-id').all())