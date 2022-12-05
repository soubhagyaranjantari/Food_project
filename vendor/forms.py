from django import forms
from accounts.models import userProfile,User
from vendor.models import vendor_model
        
class vendor_form(forms.ModelForm):

    class Meta:
        model = vendor_model
        fields = ('vendor_name','vendor_license',)
    
    # def clean(self):
    #     all_cleaned_data = super().clean()
    #     password = all_cleaned_data['password']
    #     confirm_password = all_cleaned_data['confirm_password']
    #     if password != confirm_password:
    #         raise forms.ValidationError("password  dosen't match")


# class user_f(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = User
#         fields = '__all__'
