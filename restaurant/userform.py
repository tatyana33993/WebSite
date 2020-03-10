from django import forms
from django.core.validators import RegexValidator

from restaurant.validators import validate_date, validate_time


class UserForm(forms.Form):
    name = forms.CharField(label="𝓝𝓪𝓶𝓮", max_length=15, help_text="Введите ваше имя",
                           validators=[RegexValidator('[А-Яа-яA-Za-z]+', message='Invalid name, write only letters')])
    number = forms.CharField(label="𝓟𝓱𝓸𝓷𝓮 𝓷𝓾𝓶𝓫𝓮𝓻", help_text="Введите ваш номер телефона",
                             validators=[RegexValidator(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
                                                        message='Invalid number')])
    date = forms.DateField(label="𝓓𝓪𝓽𝓮", widget=forms.DateInput(attrs={'type': 'date'}),
                           help_text="Выберете желаемую дату", validators=[validate_date])
    time = forms.TimeField(label="𝓣𝓲𝓶𝓮", widget=forms.TimeInput(attrs={'type': 'time'}),
                           help_text="Выберете желаемое время", validators=[validate_time])
    peoples = forms.DecimalField(label="𝓝𝓾𝓶𝓫𝓮𝓻 𝓸𝓯 𝓼𝓮𝓪𝓽𝓼", help_text="Введите на сколько человек вам нужен столик",
                                 min_value=1, max_value=10)
    comment = forms.CharField(label="𝓒𝓸𝓶𝓶𝓮𝓷𝓽", widget=forms.Textarea,
                              help_text="Введите свои пожелания", max_length=150, required=False)
