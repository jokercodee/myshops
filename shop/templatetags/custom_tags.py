from django import template
from shop.models import Category
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.inclusion_tag('shop/product/detail.html')
def show_nav():
    category = Category.objects.all().order_by('name')
    return {'category':category}

@register.filter(name='markdown')
def markdown_format(text):
	return mark_safe(markdown.markdown(text))
