
from django.shortcuts import render

def homepage(request):
    return render (request,'home.html')

def count(request):
    data = request.GET['fulltext']
    list = data.split()
    length = len(list)
    worddictionary1 = {}
    for word in list:
        if word in worddictionary1:
            worddictionary1[word] +=1
        else:
            worddictionary1[word] = 1

    return render(request,'count.html',{'fulltext':data , 'words':length,'worddictionary':worddictionary1.items()})