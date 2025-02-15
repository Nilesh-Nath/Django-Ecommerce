from django import forms

from .models import items

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = items
        fields = ('category','name','description','price','image')
        
        widgets = {
            'category':forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            })
        }
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model = items
        fields = ('name','description','price','image','is_sold')
        
        widgets = {
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            })
        }