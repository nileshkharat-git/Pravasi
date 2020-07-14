from django import forms
from main.models import accounts
class updateProfile(forms.ModelForm):
    username=forms.CharField(max_length=255,label='',widget=forms.TextInput(attrs={'class':'form-control'}))
    profilePic=forms.FileField()
    class Meta:
        model=accounts
        fields=['username','profilePic']