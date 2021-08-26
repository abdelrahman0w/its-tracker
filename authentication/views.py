from django.core.checks import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth, messages


class loginView(View):
    def get(self, request):
        return render(request=request, template_name='auth/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('index')

                return render(request=request, template_name='auth/login.html')

            messages.error(request, 'Invalid username or password.')
            return render(request=request, template_name='auth/login.html')

        messages.error(request, 'Please fill all fields!')
        return render(request=request, template_name='auth/login.html')


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out!')
        return redirect('login')
