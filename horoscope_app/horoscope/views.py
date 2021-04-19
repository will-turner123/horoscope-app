from django.shortcuts import render, redirect
from django.http import HttpResponse
from .get_horoscope import return_horoscope



# Create your views here.
def home(request):
    signs = {
        '1': {'sign': 'aries', 'symbol': '♈︎'},
        '2': {'sign': 'taurus', 'symbol': '♉︎'},
        '3': {'sign': 'gemini', 'symbol': '♊︎'},
        '4': {'sign': 'cancer', 'symbol': '♋︎'},
        '5': {'sign': 'leo', 'symbol': '♌︎'},
        '6': {'sign': 'virgo', 'symbol': '♍︎'},
        '7': {'sign': 'libra', 'symbol': '♎︎'},
        '8': {'sign': 'scorpio', 'symbol': '♏︎'},
        '9': {'sign': 'sagittarius', 'symbol': '♐︎'},
        '10': {'sign': 'capricorn', 'symbol': '♑︎'},
        '11': {'sign': 'aquarius', 'symbol': '♒︎'},
        '12': {'sign': 'pisces', 'symbol': '♓︎'},
    }
    signs = {'signs': ["aries", "taurus", "gemini", "cancer", "leo", 'virgo', 
            'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']}
    if request.user.is_authenticated:
        return redirect('profile/')
    return render(request, 'horoscope/land.html', signs)

def about(request):
    return render(request, 'horoscope/about.html')




# logged in user horoscope
def sign(request, sign, timeframe):
    context = return_horoscope(sign)
    return render(request, 'horoscope/sign.html', context)

def horoscope(request, sign, timeframe):
    horoscope = return_horoscope(sign, timeframe)
    horoscope['timeframe'] = horoscope['timeframe'].capitalize()
    return render(request, 'horoscope/horoscope.html', horoscope)
