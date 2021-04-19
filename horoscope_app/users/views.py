from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserBirthdayForm
from .get_sign import return_sign
from .get_horoscope import return_horoscope
from .models import Profile


# Create your views here.
def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        b_form = UserBirthdayForm(request.POST)
        if u_form.is_valid() and b_form.is_valid():
            user = u_form.save()
            birthday = b_form.cleaned_data.get('birthday')
            user.profile.birthday = birthday
            user.profile.sign = return_sign(birthday)
            user.profile.save()
            messages.success(request, f'Your account has been created!')
            return redirect('profile')
    else:
        u_form = UserRegisterForm()
        b_form = UserBirthdayForm()
    return render(request, 'users/register.html', {'u_form': u_form, 'b_form': b_form})

 

@login_required
def profile_page(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        b_form = UserBirthdayForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid() and b_form.is_valid():
            b_form.save()
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            email = u_form.cleaned_data.get('email')
            birthday = b_form.cleaned_data.get('birthday')
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        b_form = UserBirthdayForm(instance=request.user)
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)       
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'b_form': b_form,
        'horoscope': return_horoscope(request.user.profile.sign),
        'signs': ["aries", "taurus", "gemini", "cancer", "leo", 'virgo', 'libra', 'scorpio', 'sagittarius', 
                'capricorn', 'aquarius', 'pisces']
    }
    return render(request, 'users/profile.html', context)

