from django.shortcuts import render
from .models import IceCreamKiosk, IceCream


def home(request):
    kiosks = IceCreamKiosk.objects.all()
    context = {
        'kiosks': kiosks
    }
    return render(request, 'home.html', context)

def about(request, kiosk_id):
    kiosk = IceCreamKiosk.objects.get(id=kiosk_id)
    icecreams = kiosk.icecream_set.all()
    context = {
        'kiosk': kiosk,
        'icecreams': icecreams
    }
    return render(request, 'about.html',  context)