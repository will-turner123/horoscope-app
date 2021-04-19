from datetime import datetime


def clean_date(date):
    print(date)
    # should probs catch this
    if date is None:
        return None, None
    try:
        dob = str(date).split('-')
        month = int(dob[1])
        day = int(dob[2])
    except:
        day, month = None
    return day, month


def return_sign(date):
    day, month = clean_date(date)
    if day is None:
        return "Invalid Sign"
    print(f'day: {day} month: {month}')
 
    if month == 12:
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month == 1:
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
    elif month == 2:
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
    elif month == 3:
        astro_sign = 'Pisces' if (day < 21) else 'aries'
    elif month == 4:
        astro_sign = 'Aries' if (day < 20) else 'taurus'
    elif month == 5:
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
    elif month == 6:
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
    elif month == 7:
        astro_sign = 'Cancer' if (day < 23) else 'leo'
    elif month == 8:
        astro_sign = 'Leo' if (day < 23) else 'virgo'
    elif month == 9:
        astro_sign = 'Virgo' if (day < 23) else 'libra'
    elif month == 10:
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
    elif month == 11:
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
    else:
        return "No Sign"
    print(astro_sign)
    return astro_sign
