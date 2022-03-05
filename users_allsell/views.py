from multiprocessing import context
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from allsellapp.forms import UserRegistrationForm
from django.contrib import messages







def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            firstName = form.cleaned_data.get('firstName')
            messages.success(request, f'Account created for {firstName}!')
            return redirect('register_success_view')


    else: 
        form = UserRegistrationForm()


    context = {'form': form}

    return render(request, 'users_allsell/register.html', context)



def register_success_view(request):
    return render(request, 'users_allsell/register_success.html')