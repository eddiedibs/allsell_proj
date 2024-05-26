from django import forms
from products.models import Address as AddressModel

class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = AddressModel
        fields = ['first_name', 'last_name', 'email', 'address', 'phone_number']
        labels = {
            'first_name': "First name",
            'last_name': "Last name",
            'email': "Select a email",
            'address': "Select an address.",
            'phone_number': "Select a phone number.",
        }
        widgets = {
            'first_name': forms.DateInput(attrs={
                'type': 'date',
                'class': "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            }),
            'last_name': forms.DateInput(attrs={
                'type': 'date',
                'class': "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            }),
            'email': forms.Select(attrs={
                'type': 'text',
                'class': "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            }),
            'address': forms.SelectMultiple(attrs={
                'type': 'text',
                'class': "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            }),
            'phone_number': forms.SelectMultiple(attrs={
                'type': 'text',
                'class': "form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
            }),
        }