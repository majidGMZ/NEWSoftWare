from . import jalali


def jalali_converter(time):
    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    output = jalali.Gregorian(time_to_str).persian_tuple()
    return output
