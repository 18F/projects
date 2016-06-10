from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import View


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('web:home')
