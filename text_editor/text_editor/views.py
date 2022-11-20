from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html') 
def edit(request):
    text = request.GET.get('text', 'default')
    puncrem = request.GET.get('puncrem', 'off')
    extraspcrem = request.GET.get('extraspcrem', 'off')
    upcrcase= request.GET.get('upcrconv' , 'off')
    newlinerem= request.GET.get('newlinerem', 'off')
    charcount= request.GET.get('charcount', 'off')
    edited = ""
    puctuations_list = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    if puncrem == "on":
        for x in text:
            if x not in puctuations_list:
                edited = edited + x
        params = {'head': 'Punctuations removed', 'edited_text': edited}
        return render(request, 'edited.html', params)

    elif upcrcase == "on":
        upc = text.upper()
        params = {'head': 'Converted to Uppercase', 'edited_text': upc}
        return render(request, 'edited.html', params)

    elif newlinerem == "on":  
        for x in text:
            if x !="\n":
                edited= edited + x
        params = {'head': 'Removed new lines', 'edited_text': edited}
        return render(request, 'edited.html', params)

    elif extraspcrem == "on":   
        for x in text:
            if x !="\t" :
                edited= edited + x
        params = {'head': 'Removed extra spaces', 'edited_text': edited}
        return render(request, 'edited.html', params)

    elif charcount== "on":   
        for x in text:
            if x !=" ":
               edited= edited+x
               text= edited
        params = {'head': 'Charecter count','edited_text': len(edited)}
        return render(request, 'edited.html', params)

    elif (puncrem!="on" and upcrcase!="on" and newlinerem!="on" and extraspcrem!="on" and charcount != "on" ):
       return HttpResponse("Error")