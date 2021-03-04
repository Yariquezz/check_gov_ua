from django import forms


class SearchCheck(forms.Form):
    check_id = forms.CharField()
