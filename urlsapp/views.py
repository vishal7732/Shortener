from django.shortcuts import render, redirect
from urlsapp.models import Url

# Create your views here.
def mainpage(request):
    if request.method == "POST":
        full_url = request.POST.get('Full URL')
        obj = Url.create(full_url)
        return render(request, 'index.html', {'full_url':obj.full_url,'short_url': request.get_host() + '/'+obj.short_url})
    return render(request, 'index.html')

def routetoURL(request, key):
    try:
        obj = Url.objects.get(short_url=key)
        return redirect(obj.full_url)
    except:
        return redirect(mainpage)