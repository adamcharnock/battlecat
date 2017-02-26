from __future__ import absolute_import

from django import template

from hordak.models import StatementLine

register = template.Library()


@register.simple_tag
def total_unreconciled():
    return StatementLine.objects.filter(transaction=None).count()
