from django.template import Library
from freelance_django.settings import *
register = Library()


@register.simple_tag(takes_context=True)
def static(context, file_path):
    print STATIC_ROOT
    r = context['request']
    git = r.git_revision[:6]
    return STATIC_URL + file_path + '?v=' + git