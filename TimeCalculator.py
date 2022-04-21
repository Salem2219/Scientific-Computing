from datetime import datetime, timedelta


def get_next_day(weekday):
    weekday = weekday.lower()
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'monday']
    next_day = weekdays.index(weekday) + 1
    return weekdays[next_day].capitalize()


def convert_to_datetime(start):
    ex = start
    y = ex.split()
    x = y[0].split(':')
    hour, minute = int(x[0]), int(x[1])
    if y[1] == 'PM':
        hour = hour + 12
    return datetime(1, 1, 1, hour, minute, 0)


def convert_to_string(new_time, weekday):
    hour = new_time.hour
    minute = new_time.minute
    if minute < 10:
        minute = '0' + str(minute)
    M = 'AM'
    day_diff = ''
    if new_time.day == 2:
        day_diff = ' (next day)'
    if new_time.day > 2:
        day_diff = f' ({new_time.day - 1} days later)'
    if hour >= 12:
        M = 'PM'
        if hour > 12:
            hour = hour - 12
    if hour == 0:
        hour = 12
    if weekday != '':
        for i in range(new_time.day - 1):
            weekday = get_next_day(weekday)
        weekday = ', ' + weekday
    return str(hour) + ':' + str(minute) + ' ' + M + weekday + day_diff


def add_time(start, duration, weekday=''):
    # Convert start to datetime class, with year = 1, month = 1, day = 1
    start = convert_to_datetime(start)

    # Split duration to list [hours, minutes]
    duration = duration.split(':')
    hour_duration = int(duration[0])
    min_duration = int(duration[1])

    # Compute the addition of the start and duration given if the day has been incremented compute the days_difference
    time_calculated = start + timedelta(hours=hour_duration, minutes=min_duration)
    # Convert the new_time to string given if there is a day_difference print it.
    new_time = convert_to_string(time_calculated, weekday)
    return new_time


