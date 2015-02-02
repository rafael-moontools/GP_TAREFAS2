from django.shortcuts import render, HttpResponseRedirect, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from core.decorators import render_to_response
from django.conf import settings
from social.backends.oauth import BaseOAuth1, BaseOAuth2
from social.backends.google import GooglePlusAuth
from social.backends.utils import load_backends
from social.apps.django_app.utils import psa
from profiles.models import UserProfile
from django.contrib.auth import authenticate, login



def context(**extra):
    return dict({
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': ' '.join(GooglePlusAuth.DEFAULT_SCOPE),
        'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
    }, **extra)


def home(request):
    '''
    HOME PAGE
    :param request:
    :return:
    '''
    userContext = RequestContext(request, {
        'user': request.user
    })

    if request.user.is_authenticated():
        return render(request, 'index.html', context_instance=userContext)

    return render(request, 'login.html')


def login_user(request):
    state = "Please log in below..."
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Autenticando....")

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print("user active")
                return render_to_response('index.html', user)
            else:
                print("user NOT active")
                state = "Your username/password is incorrect"
    return render_to_response('login.html', state)


# @login_required(login_url='/login/google-oauth2/')
# @render_to('index.html')
# def done(request):
#     """Login complete view, displays user data"""
#     return context()

@login_required(login_url='/login/google-oauth2/')
def login(request):
    # print context()
    return HttpResponseRedirect('/')

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')

def file_upload(request):
    return render(request, 'test.html')



@login_required(login_url='/login/google-oauth2/')
def tarefas(request):
    context = RequestContext(request, {
        'user': request.user
    })
    return render(request, 'tarefas.html', context_instance=context)


@login_required(login_url='/login/google-oauth2/')
def dashboard(request):
    userContext = RequestContext(request, {
        'user': request.user
    })
    return render(request, 'dashboard.html',context_instance=userContext)


@login_required(login_url='/login/google-oauth2/')
def inbox(request):
    userContext = RequestContext(request, {
        'user': request.user
    })
    return render(request, 'inbox.html',context_instance=userContext)

@login_required(login_url='/login/google-oauth2/')
def table(request):
    userContext = RequestContext(request, {
        'user': request.user
    })
    return render(request, 'table.html',context_instance=userContext)