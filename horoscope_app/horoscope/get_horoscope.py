import pyaztro
from datetime import datetime

def return_horoscope(sign, timeframe="today"):
    sign = sign.lower()
    print(f'aztro sign: {sign}')
    horoscope = pyaztro.Aztro(sign=sign, day=timeframe)
    lucky_color = horoscope.color
    content = {
        'sign': sign.capitalize(),
        'mood': horoscope.mood,
        'lucky_time': horoscope.lucky_time,
        'description': horoscope.description,
        'date_range': horoscope.date_range,
        'lucky_color': lucky_color,
        'compatibility': horoscope.compatibility,
        'current_date': horoscope.current_date,
        'lucky_number': horoscope.lucky_number,
        'timeframe': timeframe
    }
    content['date_range'] = content['date_range'][0].strftime("%B %d") + " - " + content['date_range'][1].strftime("%B %d")
    return content