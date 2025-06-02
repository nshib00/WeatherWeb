from django import forms


class CityForm(forms.Form):
    city = forms.CharField(
        max_length=100,
        label='Город',
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите город',
            'class': 'w-full rounded-xl border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
        })
    )