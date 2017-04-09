# coding=utf-8
import datetime
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts import render
from mysite.forms import ContactForm
from django.core.mail import send_mail


def hello(request):
    return HttpResponse("Hello, world")


def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It's now {{ current_time }}</body></html>")
    html = t.render(Context({'current_time': now}))
    return HttpResponse(html)


def hours_head(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    now = datetime.datetime.now() + datetime.timedelta(hours=offset)
    assert False
    html = "It is {} hour(s), it will be {}".format(offset, now)
    return HttpResponse(html)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'bond010418@gmail.com'),
                ['wanghao010418@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})
