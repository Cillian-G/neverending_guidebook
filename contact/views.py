from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from .forms import ContactForm

def contact(request):

    if request.method == 'POST':

        form_data = {
            'email': request.POST['email'],
            'name': request.POST['name'],
            'subject': request.POST['subject'],
            'message': request.POST['message']
            }
        
        contact_form = ContactForm(form_data)
        if contact_form.is_valid():
            contact_form.save()
            return render(
                request,
                "contact_success.html",)

    contact_form = ContactForm()
    template = 'contact.html'
    context = {
        'contact_form': contact_form,
    }
    return render(request, template, context)