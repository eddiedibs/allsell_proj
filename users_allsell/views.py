from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from allsellapp.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required







def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has successfuly been created! Now you can log in!')
            return redirect('login_view')


    else: 
        form = UserRegistrationForm()


    context = {'form': form}

    return render(request, 'users_allsell/register.html', context)


@login_required
def profile(request):
    return render(request, 'users_allsell/profile.html')