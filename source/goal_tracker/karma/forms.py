
# accounts.forms.py
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import *

from django.contrib.auth import authenticate

from django import forms

from models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )



class CommentOnGoalForm(forms.ModelForm):

    class Meta:
        model = CommentOnGoal
        fields = ('content',)


class CommentOnProjectForm(forms.ModelForm):

    class Meta:
        model = CommentOnProject
        fields = ('content',)


class CommentOnProgressForm(forms.ModelForm):

    class Meta:
        model = CommentOnProgress
        fields = ('content',)


class CreateProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('goal', 'project_title', 'project_description', 'isPublic')

    def clean_goal_title(self):
        title = self.cleaned_data.get('goal_title')
        if title == '':
            raise ValidationError('Empty title error message')
        return title

class EditProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('goal', 'project_title', 'project_description', 'isPublic')

    def clean_goal_title(self):
        title = self.cleaned_data.get('goal_title')
        if title == '':
            raise ValidationError('Empty title error message')
        return title


class CreateGoalForm(forms.ModelForm):

    taglist = forms.CharField(label='Tags of Goal', max_length=100)

    class Meta:
        model = Goal
        fields = ('goal_title', 'goal_description', )

    def clean_goal_title(self):
        title = self.cleaned_data.get('goal_title')
        if title == '':
            raise ValidationError('Empty title error message')
        qs = Goal.objects.filter(goal_title=title)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return title

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('user_name', 'bio', 'gender')

class AddProgressForm(forms.ModelForm):

    class Meta:
        model = Progress
        fields = ('progress_description',)

class EditProgressForm(forms.ModelForm):

    class Meta:
        model = Progress
        fields = ('progress_description',)


class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField()

    def clean_password(self):
        username = self.data['email']
        password = self.data['password']
        user = authenticate(email=username, password=password)
        if user is None:
            raise forms.ValidationError('Incorrect password')
        return password

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'user_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]