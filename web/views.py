from django.http import JsonResponse
from django.shortcuts import render

from web.models import Data


# Create your views here.
def read(request):
    datas = Data.objects.all().values()

    data_list = []
    for data in datas:
        print(data)
        data_list.append(data)

    context = {"result": data_list}
    return JsonResponse(context)
