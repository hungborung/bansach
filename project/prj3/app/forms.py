from django import forms
from .models import Category, Product, TermOfUse
from tinymce import TinyMCEWidget

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class TermOfUseForm(forms.ModelForm):
    content = forms.CharField( 
        widget=TinyMCEWidget( 
            attrs={'required': False, 'cols': 30, 'rows': 10} 
        ) 
    ) 
    class Meta: 
        model = TermOfUse
        fields = '__all__'