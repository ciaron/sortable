#from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.forms.models import modelformset_factory
from django.template import RequestContext
from django.contrib import messages

from djsortable.models import Entry, EntryForm

def index(request):

    EntryFormSet = modelformset_factory(Entry, extra=0)

    if request.method == 'POST':
        formset = EntryFormSet(request.POST)

        if formset.is_valid():
            formset.save()
            messages.info(request, "Changes saved!")
        else:
            pass

    entry_list = Entry.objects.order_by('order')
    formset = EntryFormSet()

    context = {'entry_list': entry_list, 'formset': formset}

    return render_to_response('entry/index.html', context, context_instance=RequestContext(request))

def detail(request, entry_id):
    try:
        entry = Entry.objects.get(pk=entry_id)
    except Entry.DoesNotExist:
        raise Http404
    return render_to_response('entry/detail.html', {'entry': entry})
