from django.db import models
from .user import User
from datetime import datetime, date, timedelta

import factory
from factory import fuzzy

class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%d' % n)
    @factory.lazy_attribute
    def email(self):
        return '%s@example.com' % self.username
    begin = factory.fuzzy.FuzzyDate(start_date=date(2000, 1, 1))
    end = factory.LazyAttribute(lambda o: o.begin + timedelta(days=o.duration))

    name = "John"
    profile_pic = "Doe"

    class Params:
        duration = 12

class AdminFactory(UserFactory):
    is_admin = True
    name = "ravi"


class Log(models.Model):
    timestamp = models.DateTimeField()

    def __repr__(self):
        return f'{self.timestamp}'


class LogFactory(factory.Factory):
    class Meta:
        model = Log

    timestamp = datetime.now()


class EnglishUserFactory(factory.Factory):
    class Meta:
        model = User

    name = "English John"
    profile_pic = "Doe"


class FrenchUserFactory(factory.Factory):
    class Meta:
        model = User

    name = "French John"
    profile_pic = "Doe"
