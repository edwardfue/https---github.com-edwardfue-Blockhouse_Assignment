from django.http import JsonResponse, HttpResponse
from .models import CandleStickchart, Linechart, Barchart, Piechart
from .serializers import CandleSerializer, LineSerializer, BarSerializer, PieSerializer
from rest_framework.decorators import api_view


def candle_list(requst):
        candle = CandleStickchart.objects.all()
        candle_serial = CandleSerializer(candle,many=True)
        return JsonResponse(candle_serial.data, safe = False)
    


def line_list(request):
    line = Linechart.objects.all()
    line_serial = LineSerializer(line,many=True)
    return JsonResponse(line_serial.data, safe= False)

def bar_list(request):
    bar = Barchart.objects.all()
    bar_serial = BarSerializer(bar,many=True)
    return JsonResponse(bar_serial.data, safe=False)

def pie_list(request):
    pie = Piechart.objects.all()
    pie_serial = PieSerializer(pie, many=True)
    return JsonResponse(pie_serial.data, safe=False)

def home(request):
    return HttpResponse('Welcome to the homepage!')