minute = 60
hour = 60 * minute
day = 24 * hour
week = 7 * day
month = 30 * day
year = 12 * month
duration: int = int(input('Введите число в секундах: '))
if duration < minute:
    print(duration, 'секунд')
if minute <= duration < hour:
    print(duration // minute, 'минут', duration % minute, 'секунд')
if hour <= duration < day:
    print(duration // hour, 'часов', duration % hour // minute, 'минут', duration % hour % minute, 'секунд')
if day <= duration < week:
    print(duration // day, 'дней', duration % day // hour, 'часов', duration % day % hour // minute, 'минут',
          duration % day % hour % minute, 'секунд')
if week <= duration < month:
    print(duration // week, 'недель', duration % week // day, 'дней', duration % week % day // hour, 'часов',
          duration % week % day % hour // minute, 'минут', duration % week % day % hour % minute, 'секунд')
if month <= duration < year:
    print(duration // month, 'месяцев', duration % month // week, 'недель', duration % month % week // day, 'дней',
          duration % month % week % day // hour, 'часов', duration % month % week % day % hour // minute, 'минут',
          duration % month % week % day % hour % minute, 'секунд')
if duration > year:
    print(duration // year, 'лет', duration % year // month, 'месяцев', duration % year % month // week, 'недель',
          duration % year % month % week // day, 'дней', duration % year % month % week % day // hour, 'часов',
          duration % year % month % week % hour // minute, 'минут', duration % year % month % week % day // hour,
          'часов', duration % year % month % week % hour % minute, 'секунд')