from django import forms
from django.contrib.auth.forms import UserCreationForm


from personal_task_manager.dashboard.models import CustomUser
from personal_task_manager.users.models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2',]


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def save(self, commit=True):
        custom_user = super().save(commit=False)
        if commit:
            custom_user.save()
        if not hasattr(custom_user, 'profile'):
            Profile.objects.create(custom_user=custom_user)

        return custom_user


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude= ['custom_user']
