from django.shortcuts import render
from mycv.core.models import Person

def index(request):
    person = Person.objects.prefetch_related(
            'description',
            'achievements',
            'skills',
            'experiences',
            'careerobjectives',
        ).first()
    return render(request, "index.html", {"person": person})
