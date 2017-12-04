from django import template
from django.utils.html import mark_safe
from django.urls import reverse

from words.models import Word

register = template.Library()


@register.simple_tag
def menu_block(positioning, title, content, dest_url, *args, **kwargs):
    html = (
        "<div class='row'>" +
            "<div class='col {positioning} span-tablet-vertical-1-1'>".format(positioning=positioning) +
                "<div class='doc'>" +
                    "<div class='doc-title'>" +
                        "<h2>{title}</h2>".format(title=title) +
                    "</div>" +
                    "<div class='doc-content'>" +
                        content +
                        teach_me(dest_url, *args, **kwargs) +
                    "</div>" +
                "</div>" +
            "</div>"
    )
    return mark_safe(html)


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
def teach_me(url_name, *args, **kwargs):
    if not kwargs.get("text", None):
        text = "教我"
    else:
        text = kwargs["text"]
    url = reverse(url_name, args=args)
    return mark_safe("<a type='button' class='btn r' href='{url}'>{text}</a>".format(url=url,
                                                                                     text=text))


@register.simple_tag
def bold(text, weight):
    return mark_safe("<span style='font-weight:{weight}'>{text}</span>".format(text=text,
                                                                               weight=weight))
