import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students

# 全件取得
print(Students.objects.all())

# 頭5件取得
print(Students.objects.all()[:5])

#5件目より後
print(Students.objects.all()[5:])

# 5〜7件目
print(Students.objects.all()[5:8])

# １番最初の1件
print(Students.objects.first())

# 等価の物だけに絞り込む
print(Students.objects.filter(name='太郎').all())

# AND条件
print(Students.objects.filter(name='太郎',pk=13).all())

# 前方一致、後方一致
print(Students.objects.all())
print(Students.objects.filter(name__startswith='太').all())
print(Students.objects.filter(name__endswith='郎').all())

# or
from django.db.models import Q
print(Students.objects.filter(Q(name='太郎')| Q(pk_gt=19)).all())