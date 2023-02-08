from django import forms
from django.core.exceptions import ValidationError


class UserPhoneForm(forms.Form):

    phone = forms.CharField(

        label='Введите пожалуйста Ваш номер',
        min_length=17,

        widget=forms.TextInput(

            attrs={
                'type': 'tel',
                'name': 'phone',
                'id': 'user_phone',
                'class': 'form-control',
                'placeholder': '+7(999)-999-99-99'
            }

        ),

        error_messages={

            'required': ValidationError(
                'Пожалуйста введите актуальный номер'
            ),

            'min_length': 'Номер должен содержать минимум 17 цифр'
        },

        required=True,

    )
