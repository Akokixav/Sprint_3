# from django import settings
from django.conf import settings
from django import forms
# from django import settings
from django.http import HttpResponseRedirect, HttpResponse
from .. import dmp_render, dmp_render_to_string
from django_mako_plus import view_function
from formlib.form import FormMixIn
from django.contrib.auth import authenticate, login

@view_function
def process_request(request):

    #process the form
    form = LoginForm(request)
    if form.is_valid():
        #log the user in
        login(request, form.user)
        form.commit()
        #redirect to my account page
        return HttpResponseRedirect('/account/index/')

        #if not authenticated
    return dmp_render(request, 'login_class.html', {'form' :form, })


    #Authenticate in the self clean method

class LoginForm(FormMixIn, forms.Form):

    def init(self):
        self.form_action = '/account/login_class.modal'
        self.fields['username'] = forms.CharField(label='Username', max_length=100)
        self.fields['password'] = forms.CharField(max_length=32, widget=forms.PasswordInput)
        # self.fields['birthday'] = forms.DateField(label='Birthday')

    # def clean_username():
    #     username = self.cleaned_data.get('username')
    #
    #     return username


    def clean(self):
        #authenticate user
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        print(username)
        print(password)

        print()
        self.user = authenticate(username = self.cleaned_data.get('username'), password = self.cleaned_data.get('password'))
        if self.user is None:
            raise forms.ValidationError('Invalid username or password')

        #always return cleaned data
        return self.cleaned_data


##############AJAX VERSION ################

@view_function
def modal(request):

    #process the form
    form = LoginForm(request)
    if form.is_valid():
        #log the user in
        login(request, form.user)
        form.commit()
        #redirect to my account page
        return HttpResponse('''
                <script>
                    window.location.href = '/homepage/index';
                </script>
            ''')

        #if not authenticated
    return dmp_render(request, 'login.modal.html', {'form' :form, })
