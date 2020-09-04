from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def analyze(request):
    inputtext=request.POST.get('name','default')

    removePunc=request.POST.get('removePunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newLineremover=request.POST.get('newLineremover','off')
    charCount=request.POST.get('charCount','off')
    firstCase=request.POST.get('firstCase','off')
    tolower=request.POST.get('tolower','off')
    numRemover=request.POST.get('numRemover','off')

    str=inputtext
    purpose=""
    count=0

    if removePunc=='on':
        temp=""
        punc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in str:
            if char not in punc:
                temp+=char
        purpose+="-RemovePunctuation-"
        str=temp
    if numRemover=='on':
        temp=""
        punc='1 2 3 4 5 6 7 8 9 0'
        for char in str:
            if char not in punc:
                temp+=char
        purpose+="-numRemover-"
        str=temp

    if fullcaps=='on':
        str=str.upper()
        purpose+="-fullcaps-"

    if tolower=='on':
        str=str.lower()
        purpose+="-lowercase-"

    if newLineremover=='on':
        temp=""
        for char in str:
            if char !="\n" and char!="\r":
                temp+=char
        purpose+="-newLineremover-"
        str=temp

    if firstCase=='on':
        temp=str.title()
        purpose+="-firstCase-"
        str=temp


    if charCount=='on':
        count=len(inputtext)
        purpose+="-charCount-"



    para={'purpose':purpose,'analyzed_text':str,'count':count}
    if removePunc=="on" or fullcaps=="on" or numRemover=="on" or tolower=="on" or newLineremover=="on" or charCount=="on" or firstCase=="on":
        return render(request,'analyze.html',para)
    else:
        return HttpResponse("no function is selected")




# def capFirst(request):
#     return HttpResponse("capFirst")
#
# def newLineremover(request):
#     return HttpResponse("newLineremover")
#
# def spaceRemover(request):
#     return HttpResponse("spaceRemover")
#
# def charCount(request):
#     return HttpResponse("charCount")
