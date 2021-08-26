from django.shortcuts import render
from .models import Animal
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.


def home(request):
    animals = Animal.objects.all()
    return render(request, "animals/index.html", {'animals': animals})


def detail(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    animals = Animal.objects.all()

    return render(request, 'animals/detail.html', {'animal': animal, 'animals': animals})


def acercaNosotros(request):
    return render(request, "animals/acercaNosotros.html")


def contacto(request):
    return render(request, "animals/contacto.html")


def adopciones(request):
    animals = Animal.objects.all()
    cats = Animal.objects.filter(animal='Gato')
    dogs = Animal.objects.filter(animal='Perro')

    no_of_animals = len(Animal.objects.all())
    no_of_cats = len(cats)
    no_of_dogs = len(dogs)
    return render(request, "animals/adopciones.html", {'animals': animals, 'cats': cats, 'dogs': dogs, 'no_of_animals': no_of_animals, 'no_of_cats': no_of_cats, 'no_of_dogs': no_of_dogs})


def buscar(request):
    animals = Animal.objects.all()
    search_query = request.GET.get('q')

    if search_query:
        animals = animals.filter(
            Q(name__icontains=search_query) |
            Q(animal__icontains=search_query) |
            Q(gender__iexact=search_query) |
            Q(city__icontains=search_query)
        )
    return render(request, "animals/search.html", {'animals': animals, 'search_query': search_query})
