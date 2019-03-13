#!/usr/bin/env python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'silveiramooc.settings')

import django
django.setup()

from courses.models import Course 
