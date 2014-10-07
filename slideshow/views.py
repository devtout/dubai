# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import SlideHome
from dubai import settings

def slide_home():
    return SlideHome.objects.all()

