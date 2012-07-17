"""
Code that should be copy and pasted in to
reg/views.py to as a skeleton for creating
the authentication views
"""
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def do_login(request):
    if request.method == 'POST':
        #YOUR CODE HERE
        uname = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=uname, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #Redirect to a success page
            else:
                print "Inactive user"#Return a 'disabled account' error message
        else:
            print "Invalide Login"#Return an 'invalid login' error message
    
    form = LoginForm()
    return render_to_response('login.html', {
        'form': form,
        'logged_in': request.user.is_authenticated()
    })

@csrf_exempt
def do_logout(request):
    logout(request)
    return render_to_response('reg/logout.html')
