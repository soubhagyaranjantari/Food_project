from django import forms

from accounts.models import User,userProfile

class userFormm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'username','confirm_password')

    def clean(self):
        all_cleaned_data = super().clean()
        password = all_cleaned_data['password']
        confirm_password = all_cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("password  dosen't match")

        
# class user_pro(forms.ModelForm):
#     class Meta:
#         model = userProfile
#         fields = '__all__'
