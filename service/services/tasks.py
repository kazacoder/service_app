from django.db.models import F
from celery import shared_task


@shared_task
def set_price(subs_id):
    from services.models import Subscription
    subcription = Subscription.objects.filter(id=subs_id).annotate(
        annotated_price=F('service__full_price') * (1 - F('plan__discount_percent') / 100.00)).first()
    subcription.price = subcription.annotated_price
    subcription.save()  # (save_model=False)
