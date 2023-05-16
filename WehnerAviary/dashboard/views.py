from django.shortcuts import render
from .models import CircuitEntry
from django.http import HttpResponse, JsonResponse

# Create your views here.
def dashboard(request):
    return render(request, "dashboard/problem.html")

def submit_entry(request):
    if request.method == "POST":
        name = request.POST["name"]
        period = request.POST["period"]
        circuit = request.POST["circuit"]
        c = CircuitEntry.objects.create(name=name, period=period, circuit_completed=circuit)
        return HttpResponse(f"{name} (Period {period}), your successful completion of circuit {circuit} has been saved. Your confirmation number is {c.id}")

def teacher(request):
    return render(request, "dashboard/teacher.html", {
        "entries": CircuitEntry.objects.all()
    })