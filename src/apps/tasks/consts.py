import enum


@enum.unique
class ReminderStatus(enum.Enum):
    CREATED = "Новая"
    ENQUEUED = "Запланированная"
    IN_PROGRESS = "в Работе"
    DONE = "Завершённая"

    @classmethod
    def to_choices(cls):
        return sorted((status.name, status.value) for status in cls)


from functools import singledispatch
from typing import Text

import django
from django.db.models.base import ModelBase
from django.db.models.fields.related_descriptors import (
    ForwardManyToOneDescriptor,
    ManyToManyDescriptor,
)
from django.db.models.query_utils import DeferredAttribute


@singledispatch
def a(obj) -> Text:
    return str(obj)


@a.register
def _(obj: DeferredAttribute) -> Text:
    if django.VERSION[0] < 3:  # pragma: nocover
        return obj.field_name
    return obj.field.get_attname()


@a.register
def _(obj: ForwardManyToOneDescriptor) -> Text:
    return obj.field.name


@a.register
def _(obj: ManyToManyDescriptor) -> Text:
    return obj.field.name


@a.register
def _(obj: ModelBase) -> Text:
    return obj._meta.db_table
