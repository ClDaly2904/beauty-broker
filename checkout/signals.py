from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ Update order total after line item
    is updated or created """
    # find order the line item is related to
    # and call update total method on it
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """ Update order total after line item
    is deleted """
    instance.order.update_total()
