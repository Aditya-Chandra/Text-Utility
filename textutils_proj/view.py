from django.http import HttpResponse
import os
from django.conf import settings
from django.shortcuts import render



# Opening a text file from local drive
# def read_file(request):
#     with open('/Users/adityachandra/Desktop/Django/textutils/textutils_proj/textutils_proj/fun.txt', 'r') as f:
#         file_content=f.read()
#     return HttpResponse(file_content, content_type="text/plain")

# def neuraldata(request):
#     return HttpResponse('''This link is for Neuraldata website <a href="https://www.neuraldata.info"> Neuraldata </a> <a href="/">Back</a> <a href="\">Forward</a>''')

# def google(request):
#     return HttpResponse('''This link is for google search <a href="https://google.com"> google </a> </a> <a href="/">Back</a> <a href="\">Forward</a> ''')

def index(request):
    return render(request,'index.html')


def text_analyzer(request):
    djtext=request.GET.get("text_hai","default")
    removepunc=request.GET.get('removepunc','off')
    capitalize=request.GET.get('capitalize','off')
    newlineremover=request.GET.get('newlineremover','off')
    spaceremover=request.GET.get('spaceremover','off')
    charcounter=request.GET.get('charcounter','off')
    punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    # for removing punctuation
    if removepunc=='on':
        analyzed =  ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose': 'Status','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
        # for converting to upper case (capitalize)
    if capitalize=='on':
        analyzed=djtext.upper()
        params={'purpose': 'Status','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
        djtext=analyzed
        #for removing new line character
    if newlineremover=='on':
        analyzed =  ""
        for char in djtext:
            if char not in '\n' and char not in '\r':
                analyzed=analyzed+char
        params={'purpose': 'Status','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
        djtext=analyzed
        # for removing space from text
    if spaceremover == 'on':
        analyzed =  ""
        for i,char in enumerate(djtext):
            if not (djtext[i] == ' ' and djtext[i+1] ==' '):
                analyzed=analyzed+char
        params={'purpose': 'Status','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
        djtext=analyzed
        # for counting character in a text
    if charcounter == 'on':
        analyzed = 0
        for char in djtext:
            analyzed=analyzed+1
        params={'purpose': 'Status','analyzed_text':f'Total number of characers in the text: {analyzed}'}
    if removepunc!='on' and capitalize!='on' and newlineremover!='on' and spaceremover != 'on' and charcounter != 'on':
        return HttpResponse("Select atleast one operation")
        
    return render(request,'analyze.html',params)
       







