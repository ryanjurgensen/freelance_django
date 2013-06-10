from django.template import Library
register = Library()


@register.simple_tag(takes_context=True)
def static(context, file):
    r = context['request']
    print r.git_revision
    return file