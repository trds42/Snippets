from django import template
register = template.Library()


def new_line(value):
    value.replace('\n', '<br>')
    return value


register.filter('new_line', new_line)
