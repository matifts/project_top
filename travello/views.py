from django.shortcuts import render
from .models import destition
# Create your views here.
def index(request):
    dest1 = destition()
    dest1.name = 'Mumbai'
    dest1.desc = 'the city is beautiful'
    dest1.imge = 'destination_1.jpg'
    dest1.price =700
    dest1.offer = False

    dest2 = destition()
    dest2.name = 'Izmir'
    dest2.desc = 'Green the city is beautiful'
    dest2.imge = 'destination_2.jpg'
    dest2.price =30
    dest2.offer = True

    dest3 = destition()
    dest3.name = 'Ankara'
    dest3.desc = 'Blue the city is beautiful'
    dest3.imge = 'destination_3.jpg'
    dest3.price =744
    dest3.offer=False
    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})
