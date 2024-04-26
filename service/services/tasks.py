import datetime
import time

from celery_singleton import Singleton
from django.db import transaction
from django.db.models import F
from django.core.cache import cache
from django.conf import settings
from celery import shared_task


@shared_task(base=Singleton)
def set_price(subs_id):
    from services.models import Subscription

    with transaction.atomic():
        # time.sleep(5)

        subscription = Subscription.objects.select_for_update().filter(id=subs_id).annotate(
            annotated_price=F('service__full_price') * (1 - F('plan__discount_percent') / 100.00)).first()

        # time.sleep(20)

        subscription.price = subscription.annotated_price
        subscription.save()  # (save_model=False)
    cache.delete(settings.PRICE_CACHE_NAME)


@shared_task(base=Singleton)
def set_comment(subs_id):
    from services.models import Subscription

    with transaction.atomic():
        subscription = Subscription.objects.select_for_update().get(id=subs_id)

        # time.sleep(27)

        subscription.comment = str(datetime.datetime.now())
        subscription.save()
    cache.delete(settings.PRICE_CACHE_NAME)