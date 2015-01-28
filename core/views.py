from django.shortcuts import render, HttpResponseRedirect, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from core.decorators import render_to
from django.conf import settings
from social.backends.oauth import BaseOAuth1, BaseOAuth2
from social.backends.google import GooglePlusAuth
from social.backends.utils import load_backends
from social.apps.django_app.utils import psa



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
        print request.session.get('email')

    # print request.user['image']['url']
    return render(request, 'index.html', context_instance=userContext)

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



@login_required
def tarefas(request):
    context = RequestContext(request, {
        'user': request.user
    })
    return render(request, 'tarefas.html', context_instance=context)