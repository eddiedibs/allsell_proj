from django import forms
from products.models import Address as AddressModel

class AddressForm(forms.ModelForm):
    
    
    class Meta:
        model = AddressModel
        fields = ['user_first_name','user_last_name','address_line_1', 'address_line_2', 'city', 'zip_code']
        labels = {
            'user_first_name': "First name",
            'user_last_name': "Last name",
            'address_line_1': "First Address",
            'address_line_2': "Second Address",
            'city': "City",
            'zip_code': "Zip code",
        }
        widgets = {
             'user_first_name': forms.TextInput(attrs={
                'type': 'text',
                'disabled': 'true',
                'class': "form-control block w-full px-3 my-3"
            }),
            'user_last_name': forms.TextInput(attrs={
                'type': 'text',
                'disabled': 'true',
                'class': "form-control block w-full px-3 my-3"
            }),           
            'address_line_1': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control block w-full px-3 my-3"
            }),
            'address_line_2': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control block w-full px-3 my-3"
            }),
            'city': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control block w-full px-3 my-3"
            }),
            'zip_code': forms.TextInput(attrs={
                'type': 'text',
                'class': "form-control block w-full px-3 my-3"
            }),
        }

    def save(self, commit=True):
        address = super(AddressForm, self).save(commit=False)
        address.address_line_1 = self.cleaned_data['address_line_1']
        address.address_line_2 = self.cleaned_data['address_line_2']
        address.city = self.cleaned_data['city']
        address.zip_code = self.cleaned_data['zip_code']

        if commit:
                address.save()
                return address