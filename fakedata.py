import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','assignment.settings')
import django
django.setup()


import random
from custom.models import User,Activity
from faker import Faker
#instance for the Faker object
fakegen = Faker()

def dummy(N=5):
    for entry in range(N):

        fake_id    = fakegen.bothify(text='??#?##?##')
        fake_name  = fakegen.name()
        fake_tz    = fakegen.timezone()
        fake_start_date = fakegen.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
        fake_end_date = fakegen.date_time_this_month(before_now=False, after_now=True, tzinfo=None)

        usr  = User.objects.get_or_create(id=fake_id,real_name=fake_name,tz=fake_tz)[0]
        acty = Activity.objects.get_or_create(user=usr,start_time=fake_start_date,end_time=fake_end_date)[0]


if __name__ == '__main__':
    print("Creating dummy data...Please Wait")
    dummy(10)
    print('dummy data successfully added')


