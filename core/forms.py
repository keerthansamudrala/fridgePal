from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    """
    Custom user registration form extending Django's default UserCreationForm.
    Adds an email field and validates uniqueness.
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]  # ✅ Corrected field names

    def clean_email(self):
        """
        Ensure the email address is unique across users.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email
