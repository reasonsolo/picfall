from django.shortcuts import render_to_response
from django.template import RequestContext

from picfall.fall.models import Picture


def home(request):
    pics = Picture.objects.all()
    return render_to_response("home.html", {
        "pics": pics,
        }, context_instance = RequestContext(request))

