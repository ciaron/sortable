#from django.template import Context, loader
from django.shortcuts import render
from django.http import Http404

from djsortable.models import Entry

def index(request):
    entry_list = Entry.objects.order_by('order')
    context = {'entry_list': entry_list}
    return render(request, 'entry/index.html', context)

def detail(request, entry_id):
    try:
        entry = Entry.objects.get(pk=entry_id)
    except Entry.DoesNotExist:
        raise Http404
    return render(request, 'entry/detail.html', {'entry': entry})
