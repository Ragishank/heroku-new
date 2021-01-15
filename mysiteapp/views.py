from django.shortcuts import render

# Create your views here.
def fnSample(request):
    return render(request,'sample.html')