from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class UserPhoneForm(forms.Form):

    phone = forms.CharField(

        label='Введите пожалуйста Ваш номер',

        min_length='17',

        max_length='17',

        required=True,

        widget=forms.TextInput(

            attrs={
                'type': 'tel',
                'name': 'phone',
                'id': 'user_phone',
                'class': 'form-control',
                'placeholder': '+7(999)-999-99-99',
                'autocomplete': 'off',
                'pattern': '\+[7][(]\d{3}[)]-\d{3}-\d{2}-\d{2}',
            },


        ),

        error_messages={

            'required': 'Пожалуйста введите актуальный номер',

            'min_length': 'Номер должен содержать 17 цифр'
        },
    )

    def clean_phone(self):

        data = self.cleaned_data.get('phone')

        if len(data) < 17:
            raise ValidationError(
                _('Номер телефона должен содержать не менее 17 символов'),
                code='invalid length',)
        return data


