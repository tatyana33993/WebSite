from django.core.exceptions import ValidationError
import datetime


def validate_date(value):
    now = datetime.datetime.now()
    if value < now.date():
        raise ValidationError('You booked a day in the past.')


def validate_time(value):
    start = datetime.time(9, 0, 0)
    end = datetime.time(20, 0, 0)
    if start <= value <= end:
        pass
    else:
        raise ValidationError('You can only book a table between 9:00 and 20:00')
