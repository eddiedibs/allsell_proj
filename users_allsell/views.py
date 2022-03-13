from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from allsellapp.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required







def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has successfully been created! Now you can log in!')
            return redirect('login_view')


    else: 
        form = UserRegistrationForm()


    context = {'form': form}

    return render(request, 'users_allsell/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            profile_update_form.save()
            user_update_form.save()
            messages.success(request, 'Your account has successfully been updated!')
            return redirect('profile_view')


    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }
    return render(request, 'users_allsell/profile.html', context)