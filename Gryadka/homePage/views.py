from django.shortcuts import render
from datetime import datetime
from .forms import *


# Create your views here.
def homePage(request):
    current_day = datetime.now()
    current_day = current_day.date
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        print(data['name'])
        new_form = form.save()

    return render(request, 'homePage\homePage.html', locals())
