from django.http import HttpResponse

from django.shortcuts import render


def home(request):

    # in case you have to return current string in form of a html response
    #  return HttpResponse('this is first website of sharad for Django')


    # return render(request,'homepage.html',{'getinfo' : 'this is a way to send info in form of dictonary to html'})

    return render(request,'homepage.html')


def count(request):

    d  = request.GET['textentered']

    print (d)

    c =  d.split()

    return render (request,'count.html',{'data':d,'count':len(c)})
