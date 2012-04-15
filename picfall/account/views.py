from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.forms.util import ErrorList
#from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


@csrf_protect
def login_view(request):
    # FIXME
    """
    A login view: render a login-form page and then redirect user to destination
    """
    user = request.user
    next_url = request.REQUEST.get('next')

    if not next_url:
        next_url = '/'
    if user.is_authenticated():
        return redirect(next_url)

    form = AuthenticationForm()
    wrong_pswd = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next', next_url)
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect(next_url)
        else:
            wrong_pswd = 1
    return render_to_response('account/login_view.html', {
        'form': form,
        'wrong_pswd': wrong_pswd,
        }, context_instance = RequestContext(request))


def logout_view(request):
    """
    A logout view
    """
    logout(request)
    return redirect("/")

def profile(request, user_id = None):
    if user_id:
        pass
    else:
        pass


