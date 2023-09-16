from django.shortcuts import render, redirect
from .forms import SignupForm


def welcome(request):
    return render(request, 'welcome.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # 'login'は遷移先のビュー名に置き換えてください。
    else:
        form = SignupForm()
        
    return render(request, 'signup.html', {'form': form})
