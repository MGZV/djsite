from django import template
from player.models import *

register = template.Library()

def get_categories():
    return Category.objects.all()