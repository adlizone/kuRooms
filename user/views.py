from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import SignUpForm

class SignUp(View):
    
    template_name = "user/signup_form.html"
    success_url = reverse_lazy("listings:all")

    def get(self, request):
        form = SignUpForm()
        ctx = {'form': form}

        return render(request, self.template_name, ctx)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(success_url)

        else:
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
