from django import forms
from django.forms import ModelForm, Textarea

from .models import Food


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'desc', 'ingredients', 'image']
        fields = ['name', 'desc', 'image']
        widgets = {
            'desc': Textarea(),
            #'ingredients': Textarea({"placeholder": "chicken breast, string beans, 1 cup white rice"}),
        }
        labels = {
            'desc': f'Descriptions: '
            f'카카오톡 아이디나 문자받을 전화번호를 꼭 남겨주세요'
    
        }
        
        '''labels = {
            'ingredients': f'Enter a list of ingredients that were part'
                           f' of your meal, separated by commas.'
        }'''

class LogSearchForm(forms.Form):
    query = forms.CharField(label='고수의 이름이나 주제를 입력해주세요', required=False)
