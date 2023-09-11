from django.db import models
from core.models import BasicModelMixin


class Order(BasicModelMixin):
    class STATUS:
        PACKING = 'PACKING'
        ON_THE_MAY = 'ON_THE_MAY'
        READY_TO_TAKE = 'READY_TO_TAKE'

    STATUS_CHOICES = (
        (STATUS.PACKING, 'Пакуется'),
        (STATUS.ON_THE_MAY, 'В пути'),
        (STATUS.READY_TO_TAKE, 'Готов к выдаче')
    )

    receiver = models.CharField(max_length=128)
    sender = models.CharField(max_length=128)

    status = models.CharField(
        'Статус',
        choices=STATUS_CHOICES,
        max_length=16,
        null=False,
        default=STATUS.PACKING
    )
