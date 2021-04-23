from django import forms
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from .models import CustomUser
from django.forms import ModelForm
from msys.models import DataEntrycc1
from msys.models import DataEntrycc2
from msys.models import DataEntryacl
#from msys.models import Delete

from django.core.validators import MinValueValidator, MaxValueValidator

class EnterFormcc1(forms.ModelForm):
        class Meta:
          model = DataEntrycc1
          fields = '__all__'

class EnterFormcc2(forms.ModelForm):
        class Meta:
          model = DataEntrycc2
          fields = '__all__'

class EnterFormacl(forms.ModelForm):
        class Meta:
          model = DataEntryacl
          fields = '__all__'
          
        # def clean(self):
        #     super().clean()
        #     System_No       = self.cleaned_data.get['System_No']
        #     Date            = self.cleaned_data.get['Date']
        #     Make            = self.cleaned_data.get['Make']
        #     Model_No        = self.cleaned_data.get['Model_No']
        #     Quantity        = self.cleaned_data.get['Quantity']
        #     Particulars     = self.cleaned_data.get['Particulars']
        #     Remarks         = self.cleaned_data.get['Remarks']



'''class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


            


class DateForm(ModelForm):
    class Meta:
        model = Dates
        fields = '__all__'

        def clean(self):
            super().clean()
            Date        = self.cleaned_data.get['Date']


class DeleteForm(ModelForm):
    class Meta:
        model = Delete
        fields = '__all__'

        def clean(self):
            super().clean()
            Rollno = self.cleaned_data.get['Rollno']
            Pin   = self.cleaned_data.get['Pin']
'''
form = EnterFormcc1()
form2 = EnterFormcc2()
form3 = EnterFormacl()
