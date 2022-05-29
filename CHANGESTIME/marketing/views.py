from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EmailSignupForm
from .models import Signup

import json
import requests




