from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Datos
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = User
        fields = ('username', 'password')


class PForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mentee', 'mentor']

    def __init__(self, *args, **kwargs):
        super(PForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UserForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'ranking']
#        fields = ('location', 'facebook', 'mentee', 'mentor')
'''
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
'''
#    def save(self):
#        data = self.cleaned_data


class Prof1Form(forms.Form):
    mentee = forms.BooleanField()
    mentor = forms.BooleanField()
    location= forms.CharField()
#    location = forms.CharField()
#    facebook = forms.Textarea()


class NoFormTagCrispyFormMixin(object):
    @property
    def helper(self):
        if not hasattr(self, '_helper'):
            self._helper = FormHelper()
            self._helper.form_tag = False
        return self._helper


class Profile1Form(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        TabHolder(
            Tab(
                'Basic Information',
                'avatar',
                'bio',
                'birth_date',
                'location'
            ),
            Tab(
                'Contact',
                'phone',
                'facebook',
                'twitter',
                'github',
                'linkedin',
                'google'
            ),
            Tab(
                'Mentor',
                'mentor',
                'interest_in_technology',
                'interest_in_marketing',
                'interest_in_legal',
                'interest_in_leadership',
                'interest_in_business',
                'interest_in_operations',
                'interest_in_investments',
                'interest_in_professional_development'
            ),
            Tab(
                'Mentee',
                'mentee',
                'learn_technology',
                'learn_marketing',
                'learn_legal',
                'learn_leadership',
                'learn_business',
                'learn_operations',
                'learn_investments',
                'learn_professional_development'
            )
        )
    )

    class Meta:
        model = Profile  # Your User model
        fields = [
          'avatar',
          'bio',
          'birth_date',
          'location',
          'phone',
          'facebook',
          'twitter',
          'github',
          'linkedin',
          'google',
          'mentor',
          'interest_in_technology',
          'interest_in_marketing',
          'interest_in_legal',
          'interest_in_leadership',
          'interest_in_business',
          'interest_in_operations',
          'interest_in_investments',
          'interest_in_professional_development',
          'mentee',
          'learn_technology',
          'learn_marketing',
          'learn_legal',
          'learn_leadership',
          'learn_business',
          'learn_operations',
          'learn_investments',
          'learn_professional_development'
        ]


class DatosForm(forms.ModelForm):
    helper = FormHelper()

    class Meta:
        model = Datos
        fields = ['phone', 'facebook' ]