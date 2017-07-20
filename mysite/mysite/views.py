from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
from mysite.forms import ContactForm
from django.core.mail import send_mail, get_connection

def hello(request):
    return HttpResponse("Hello World!")

### example with shortcut and explanations for current_datetime
#imports for process in separate steps
#from django.http import HttpResponse
#from django.http.response import Http404
#from django.template.loader import get_template
#import datetime

#imports needed with shortcut
#from django.shortcuts import render
#import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    
    #whole process in detail
    #t = get_template('current_datetime.djhtml')
    #html = t.render({'current_date':now})
    #return HttpResponse(html)
    
    #shortcut with render(Request, Template, Context)
    #possible use of subdirectories, e.g. 'subdirectory/current_datetime.djhtml'
    return render(request, 'current_datetime.djhtml', {'current_date':now})
### end of example

def hours_ahead(request, offset):
    
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    
    return render(request, 'hours_ahead.djhtml', {'offset': offset,'next_time':dt})
    #html = "<html><body> In %s hour(s), it will be %s </body></html>" % (offset, dt) 
    #return HttpResponse(html)

#view function to display all request meta data keys and values in a table
def display_meta(request):
    metadata = request.META
    html = []
    for k in metadata:
        html.append("<tr><td>%s</td><td>%s</td></tr>" % (k, metadata[k]))
    return HttpResponse("<table>%s</table>" % "\n".join(html))

#function to handle (contact) form submissions (Chapter "Tying Forms to Views")
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection = con
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.djhtml', {'form':form})

def contact_ty(request):
    return render(request, 'contact_ty.djhtml')
    