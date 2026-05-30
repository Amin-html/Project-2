from django.shortcuts import render, get_object_or_404
from .models import Computer

def computer_list(request):
    zone = request.GET.get('zone', '')
    if zone:
        computers = Computer.objects.filter(zone=zone)
    else:
        computers = Computer.objects.all()
    return render(request, 'computers/computer_list.html', {
        'computers': computers,
        'zone': zone,
    })

def computer_detail(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    return render(request, 'computers/computer_detail.html', {'computer': computer})
# Create your views here.
