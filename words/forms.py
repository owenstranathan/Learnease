from django import forms

class LookupForm(forms.Form):
    LOOKUP_CHOICES = (
        (1, "Traditional"),
        (2, "Simplified"),
        (3, "Numbered Pinyin"),
        (4, "Tonal Pinyin"),
        (5, "English"),
    )

    searchTerm = forms.CharField(max_length=200, label="", widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Search Learnease'}))
    lookupChoice = forms.ChoiceField(choices=LOOKUP_CHOICES, label="", initial="Simplified", widget=forms.Select(), required=True)
