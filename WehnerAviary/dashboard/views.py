from django.shortcuts import render
from .models import CircuitEntry
from django.http import JsonResponse

# Create your views here.
def dashboard(request):
    return render(request, "dashboard/problem.html")

def submit_entry(request):
    if request.method == "POST":
        name = request.POST["name"]
        period = request.POST["period"]
        circuit = request.POST["circuit"]
        CircuitEntry.objects.create(name=name, period=period, circuit_completed=circuit)
        return JsonResponse({"success": True})

def teacher(request):
    return render(request, "dashboard/teacher.html", {
        "entries": CircuitEntry.objects.all()
    })