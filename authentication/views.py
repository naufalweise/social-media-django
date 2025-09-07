from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
# Create your views here.

def view_sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            # return form with error message
            return render(request, 'registration/sign-up.html', {'form': form})
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/sign-up.html', context)

class SignUpView(CreateView):
    template_name = "registration/sign-up.html"
    form_class = UserCreationForm
