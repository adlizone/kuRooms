from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from listings.models import Property

class MainView(LoginRequiredMixin, ListView):
    template_name = "user/dashboard.html"
    model = Property

    def get_queryset(self):
        qs = super(MainView, self).get_queryset()
        return qs.filter(owner=self.request.user)        

class SignUp(View):
    
    template_name = "user/signup_form.html"
    success_url = reverse_lazy("user:all")

    def get(self, request):
        form = SignUpForm()
        ctx = {'form': form}

        return render(request, self.template_name, ctx)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(self.success_url)

        else:
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
