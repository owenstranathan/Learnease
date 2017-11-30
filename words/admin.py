from django.contrib import admin

from .models import Word


class WordAdmin(admin.ModelAdmin):
    list_display = ('simplified_chinese', 'tonal_pinyin', 'definition')
    search_fields = ('id', 'simplified_chinese', 'tonal_pinyin', 'numbered_pinyin', 'definition')


# Register your models here.
admin.site.register(Word, WordAdmin)
