from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag
def word_card(word):
    pass


@register.simple_tag
def teach_me(url):
    return mark_safe("<a type='button' class='btn u' href='{0}'>教我</a>".format(url))
