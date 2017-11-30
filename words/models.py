from django.db import models

# Create your models here.

# The maximum lengths are derived from data pulled from my words
# "database" (i.e. HSK lists) I determined the maximum sizes of each field there
# and decided that I would alow each field to be 50% larger in my database
# the max lengths in cedict are:
# traditional:  4
# simplified:   4
# pinyin:       27
# definition:   240

# a 50% increase means that:
# traditional:  6
# simplified:   6
# pinyin:       40.5 ≈ 40
# definition:   360

class Word(models.Model):
    HSK_LEVEL_CHOICES= (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
    )
    hsk_level = models.CharField(max_length=1, choices=HSK_LEVEL_CHOICES, default=1)

    traditional_chinese = models.CharField(max_length=6)
    simplified_chinese = models.CharField(max_length=6)
    numbered_pinyin = models.CharField(max_length=40)
    tonal_pinyin = models.CharField(max_length=40)
    definition = models.CharField(max_length=360)

    notes = models.TextField(null=True)


    def __str__(self):
        return  self.simplified_chinese + "(" + self.tonal_pinyin + ")"
