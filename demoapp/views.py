
from django.shortcuts import render
from.models import mytable
# Create your views here.
def demo1(request):
    obj=mytable.objects.all()
    return render(request,'index.html',{"result":obj})





