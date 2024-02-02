import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students,Schools

# 外部テーブルでフィルター
for student in Students.object.filter(school__name='南高校').all():
    print(student.name,student.school.name,student.school.prefecture.name)

# 外部テーブルでexclude
for student in Students.object.exclude(school__name='南高校').all():
    print(student.name,student.school.name,student.school.prefecture.name)
# 外部キーで逆紐付け
print(Schools.objects.filter(students__name='太郎').all())

# 外部キーで並び替え
for student in Students.objects.order_by('-school__name').all():
    print(student.name,student.school.name)

#GROUP BY
from django.db.models import Count,Max
print(Students.objects.values('school__name').annotate(Count(id),Max(id)))
