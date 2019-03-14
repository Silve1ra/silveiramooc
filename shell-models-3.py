#!/usr/bin/env python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'silveiramooc.settings')

import django
django.setup()

from courses.models import Course 

print(type(Course.objects))
print(type(Course.objects.all()))

Course.objects.create(name='Python mais uma vez', slug='django')
Course.objects.create(name='VisualStudio', slug='python')
Course.objects.create(name='Algoritmos', slug='portunhol')

print(Course.objects.search('python'))
