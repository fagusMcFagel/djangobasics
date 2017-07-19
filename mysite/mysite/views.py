from django.http import HttpResponse
from django.http.response import Http404
from django.http.request import HttpRequest

def hello(request):
    return HttpResponse("Hello World!")

### example with shortcut and explanations for current_datetime
#imports for process in separate steps
#from django.http import HttpResponse
#from django.http.response import Http404
#from django.template.loader import get_template
#import datetime

#imports needed with shortcut
from django.shortcuts import render
import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    
    #whole process in detail
    #t = get_template('current_datetime.html')
    #html = t.render({'current_date':now})
    #return HttpResponse(html)
    
    #shortcut with render(Request, Template, Context)
    #possible use of subdirectories, e.g. 'subdirectory/current_datetime.html'
    return render(request, 'current_datetime.html', {'current_date':now})
### end of example

def hours_ahead(request, offset):
    
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    
    return render(request, 'hours_ahead.html', {'offset': offset,'next_time':dt})
    #html = "<html><body> In %s hour(s), it will be %s </body></html>" % (offset, dt) 
    #return HttpResponse(html)