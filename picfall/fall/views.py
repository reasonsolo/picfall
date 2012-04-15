from django.shortcuts import render_to_response
from django.template import RequestContext

from picfall.fall.models import Picture, Category


def home(request):
    pics = Picture.objects.all()
    cats = Category.objects.all()
    return render_to_response('fall/home.html', {
        'pics': pics,
        'cats': cats,
        }, context_instance = RequestContext(request))

