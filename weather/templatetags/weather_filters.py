from django import template

register = template.Library()


@register.filter
def short_time(value):
    if isinstance(value, str):
        parts = value.split(':')
    else:
        parts = [f"{value.hour:02d}", f"{value.minute:02d}", f"{value.second:02d}"]

    hour = str(int(parts[0])) # удаление ведущего нуля
    minute = parts[1]

    return f"{hour}:{minute}"


def math_round(value):
    if (value - int(value)) >= 0.5: # если дробная часть больше 0,5 - округляем, иначе - оставляем
        return int(value) + 1
    return int(value)


@register.filter
def round(value):
    if isinstance(value, str) and value.isnumeric():
        num = float(value)
        return math_round(num)
    elif isinstance(value, float):
        return math_round(value)
    return value

