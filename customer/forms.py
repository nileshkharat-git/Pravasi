from django import forms
from main.models import accounts
class updateProfile(forms.ModelForm):
    profilePic=forms.FileInput(attrs={'class':'custom-file-input'})
    class Meta:
        model=accounts
        fields=['username','profilePic']