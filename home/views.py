
from importlib.resources import contents
from django.shortcuts import render
from django.http import HttpResponse
import speedtest




def index(request):
    return render(request , 'home.html')

def About(request):
    test = speedtest.Speedtest()
    test.get_servers()
    best = test.get_best_server()
    host = best['host']
    city = best['name']
    return render(request , 'About.html', {'host':host, 'city':city})


def block(request):
    test = speedtest.Speedtest()
    downloadspeed = test.download()
    uploadspeed = test.upload()
    ping_result = test.results.ping

    down = downloadspeed/1024/1024
    uplo = uploadspeed/1024/1024

    d = float("{:.2f}".format(down))
    u = float("{:.2f}".format(uplo))
    return render(request , 'block.html', {'down':d, 'uplo':u, 'ping':ping_result})


