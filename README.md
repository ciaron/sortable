sortable
========

Testbed for Django/jQueryUI.sortable integration.

I wanted to find out how to do drag-and-drop reordering of Django models. The ordering should be stored as a model field (i.e. in the database). It should also be asynchronous, so no need to click a "Save" button.

I also wanted CSRF protection and a pony.

Main bits:

1. A Django model called "Entry" which has a sort order field (err, called "order"), an IntegerField
2. `<UL class="sortable">` in the template djsortable/templates/entry/index.html which uses jQuery-UI's "sortable" widget, and can be dragged-and-dropped
3. Javascript in the template to make an AJAX POST when the items are dragged and dropped
3. A view function called "index" which will process the POST and save changes to the model

To use: 

It should work standalone:
git clone
python manage.py syncdb, runserver etc. 

If not, drop me line.

Links:
http://rstrobl.com/blog/2012/01/19/sorting-django-model-instances-jqueryui-sortable/
http://jqueryui.com/sortable/
https://github.com/ciaron/sortable
https://docs.djangoproject.com/en/dev/ref/request-response/#querydict-objects
