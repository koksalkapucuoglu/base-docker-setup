from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .models import NumberPair

@shared_task
def add(number_pair_id):
    number_pair = NumberPair.objects.get(id=number_pair_id)
    number_pair.result = number_pair.number1 + number_pair.number2
    number_pair.save()