from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import Contact_Us


def get_form(request):

    if request.method == 'POST':
        form = Contact_Us(request.POST)
        if form.is_valid():
            your_email = form.cleaned_data['email']
            # return HttpResponse(your_email)
            message = "You're email submited"
            return HttpResponseRedirect(reverse('contact'))

    else:
        form = Contact_Us()
        message = ''

    return render(request, 'form_test/contact.html', {'form': form, 'message': message})
