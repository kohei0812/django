import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

p = Person(
    first_name='Taro',last_name='Sato',
    birthday='2001-01-01',email='aa@mail.com',
    salary=10000,memo='memo taro',web_site='https://www.google.com'
)
p = Person(
    first_name='Taro',last_name='Sato',
    birthday='2001-01-01',email='aa@mail.com',
    salary=None,memo='memo taro',web_site='https://www.google.com'
)
p = Person(
    first_name='Taro',last_name='Sato',
    birthday='2001-01-01',email='aa@mail.com',
    salary=None,memo='memo taro',web_site=''
)

# p.save()

# classmethod create

# Person.objects.create(
#     first_name='Jiro',last_name='Yamada',
#     birthday='2001-01-01',email='aa@mail.com',
#     salary=300000,memo='memo jiro',web_site=None
# )

# get_or_create(取得　or 作成)
obj, created = Person.objects.get_or_create(
    first_name='Saburo',last_name='Yamada',
    birthday='2001-01-01',email='aa@mail.com',
    salary=400000,memo='memo jiro',web_site=None
)

print(obj)
print(created)
