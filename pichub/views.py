from django.shortcuts import render


def pagedemo(request):
    return render(request, '../templates/index.html')
# Create your views here.
