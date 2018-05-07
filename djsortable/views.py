#from django.template import Context, loader
from django.shortcuts import render
from django.http import Http404, HttpResponse, QueryDict
from django.template import RequestContext
from django.contrib import messages

from djsortable.models import Entry

def index(request):

    if request.method == 'POST':

        # request.POST['content'] is a query string like 'entry[]=3&entry[]=2&entry[]=1'
        # convert to a QueryDict so we can do things with it
        entries = QueryDict(request.POST['content'])

        for index, entry_id in enumerate(entries.getlist('entry[]')):
            # save index of entry_id as it's new order value
            entry = Entry.objects.get(id=entry_id)
            entry.order = index
            entry.save()

    # split our entries arbitrarily, so we can have two lists on the page...
    entry_list1 = Entry.objects.order_by('order')[:2]
    entry_list2 = Entry.objects.order_by('order')[2:]

    context = {'entry_list1': entry_list1, 'entry_list2': entry_list2}

    return render(request, 'entry/index.html', context)

def detail(request, entry_id):
    try:
        entry = Entry.objects.get(pk=entry_id)
    except Entry.DoesNotExist:
        raise Http404
    return render(request, 'entry/detail.html', {'entry': entry})
