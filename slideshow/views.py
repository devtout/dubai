# -*- coding: utf-8 -*
from models import SlideHome


def slide_home():
    return SlideHome.objects.all()

