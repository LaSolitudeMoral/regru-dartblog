from django import template
from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('dartblog/templatetags/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {'tags': tags}
