from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """ Add fields to be rendered on the checkout form """

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """ Override default init method. Add placeholders/classes,
        remove auto-generated labels """

        # override default init method
        super().__init__(*args, **kwargs)

        # set placeholders for input fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postcode',
            'street_address1': 'Street Address Line 1',
            'street_address2': 'Street Address Line 2',
            'town_or_city': 'Town or City',
            'county': 'County, State or Locality',
        }

        # set autofocus on first field of form
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:

            # iterate through each field other than country
            if field != 'country':
                # add asterisk to show required fields to user
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # add placeholder values from placeholders dict
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # remove field labels as placeholders are present
            self.fields[field].label = False
