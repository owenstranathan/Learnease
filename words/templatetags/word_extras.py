from django import template
from django.utils.html import mark_safe

from words.models import Word

register = template.Library()


@register.simple_tag
def word_card(simplified):
    word = Word.objects.filter(simplified_chinese=simplified)
    word = word.first()
    if not word:
        return mark_safe(("<div class='doc doc-red-head'>" +
                    "<h3>''{0}'' isn't in the HSK and thus not in my database, hur-dur!!!</h6>".format(simplified) +
                "</div>"
                ))
    return mark_safe(
        ("<div class='doc doc-red-head'>" +
                "<div class='doc-title'>" +
                    "<h2>{0}</h2>".format(word.simplified_chinese) +
                "</div>" +
                "<div class='doc-content'>" +
                    "<article>" +
                        "<p>simplified: {0}</p>".format(word.simplified_chinese) +
                        "<p>traditional: {0}</p>".format(word.traditional_chinese) +
                        "<p>pinyin: {0}</p>".format(word.tonal_pinyin) +
                        "<p>what mean: {0}</p>".format(word.definition) +
                    "</article>" +
                "</div>" +
            "</div>")
    )


@register.simple_tag
def teach_me(url):
    return mark_safe("<a type='button' class='btn u' href='{0}'>教我</a>".format(url))
