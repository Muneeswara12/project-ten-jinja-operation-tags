from django.shortcuts import render

# Create your views here.
def lion(request):
    d={'a':101,'b':50,'c':10}
    return render(request,'forest.html',context=d )