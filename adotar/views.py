from django.shortcuts import render
from divulgar.models import Pet, Raca

def listar_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(status="P")
        racas = Raca.objects.all()
        return render(request, 'listar_pets.html', {'pets': pets})