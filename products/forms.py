from django import forms
from .models import Product, Product_Category, Skin_Concern, Brand
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """ Create instance of Product Form """

    class Meta:
        model = Product
        exclude = ('user_wishlist', 'brand')

    image = (forms.ImageField(label='Image', required=False,
             widget=CustomClearableFileInput))

    # override init method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Product_Category.objects.all()
        skin_types = Skin_Concern.objects.all()

        # get friendly name for each category
        prod_friendly_names = [(c.id, c.friendly_name) for c in categories]

        # get friendly name for each skin type
        skin_friendly_names = [(c.id, c.friendly_name) for c in skin_types]

        # set placeholders for input fields
        placeholders = {
            'product_type': 'Product Type',
            'skin_type': 'Skin Type',
            'line_number': 'Line Number',
            'name': 'Product Name',
            'description': 'Product Description',
            'ingredients_list': 'Ingredients List',
            'price': 'Price',
            'rating': 'Product Rating',
            'image_url': 'Image URL',
            'image': 'Image',
            'size': 'Product Size'
        }

        # render skincare categories based on friendly name
        self.fields['product_type'].choices = prod_friendly_names
        self.fields['skin_type'].choices = skin_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'

        # set autofocus on first field of form
        self.fields['product_type'].widget.attrs['autofocus'] = True
        for field in self.fields:

            # add asterisk to show required fields to user
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # add placeholder values from placeholders dict
            self.fields[field].widget.attrs['placeholder'] = placeholder

            # remove field labels as placeholders are present
            self.fields[field].label = False
