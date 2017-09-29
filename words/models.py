from django.db import models

# Create your models here.

# The maximum lengths are derived from data pulled from my words
# "database" (i.e. cedict) I determined the maximum sizes of each field there
# and decided that I would alow each field to be 50% larger in my databse
# the max lengths in cedict are:
# traditional:  20
# simplified:   20
# pinyin:       104
# definition:   496

# a 50% increase means that:
# traditional:  30
# simplified:   30
# pinyin:       156 ≈ 160
# definition:   744 ≈ 750

class Word(models.Model):
    traditional = models.CharField(max_length=30)
    simplified = models.CharField(max_length=30)
    pinyin = models.CharField(max_length=160)
    defintion = models.CharField(max_length=750)

    def __str__(self):
        return self.traditional + " " + self.simplified + "(" + self.pinyin + ")"
