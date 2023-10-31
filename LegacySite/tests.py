from shlex import quote
from models import User 
from django.test import TestCase, Client
import json
import os
from django.http import HttpRequest
from os import system
from LegacySite.models import User, Product, Card
from . import extras
from .views import *
from django.urls import reverse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GiftcardSite.settings')
import django

django.setup()
CARD_PARSER = 'giftcardreader'

# Create your tests here.

class MyTest(TestCase):

    def test_1(self):
        pass