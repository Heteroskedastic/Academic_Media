import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from app.models import User

log = logging.getLogger(__name__)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.GET.get('logout', None):
            username = request.user.username
            logout(request)
            return render(request, 'logout.html', context={'user': username})
        return super().get(request, *args, **kwargs)


class LoginView(TemplateView):
    template_name = "Login.html"
    error = None
    def post(self, request, *args, **kwargs):
        try:
            req = HttpResponseRedirect(reverse('app:home'))
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                 login(request, user)
                 req.set_cookie('login', True, max_age=None)
                 return req
            else:
                error = 'Username or Password Incorrect'
                log.error('Username or Password Incorrect')
        except Exception as e:
            log.error("Exception: {}".format(str(e)) )

        return render(request, self.template_name, context={'error': error})


class SignUp(TemplateView):
    template_name = "SignUp.html"


    def post(self, request, *args, **kwargs):
        error = None
        success = None
        try:
            if not User.objects.filter(email=request.POST.get('username')).exists():
                print(request.POST.get('usertype'))
                user = User.objects.create(email=request.POST.get('username'),type=request.POST.get('usertype'))
                user.set_password(request.POST.get('password'))
                user.save()
                if user is not None:
                    success = '{} account created'.format(request.POST.get('username'))
                else:
                    error = 'Username or Password Incorrect'
                    log.error('Username or Password Incorrect')
            else:
                error = "Email already exists"

        except Exception as e:
            log.error("Exception: {}".format(str(e)))

        return render(request, self.template_name, context={'error': error, 'success': success})




