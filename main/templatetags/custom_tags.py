__author__ = 'wanglei02'

from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='join_link', needs_autoescape=True)
def join_link(value, arg, autoescape=True):
    arr = []
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    for i in value:
        arr.append('<a href="%s">%s</a>' % (
            i.get_absolute_url(), esc(i)
        ))

    return mark_safe(arg.join(arr))
