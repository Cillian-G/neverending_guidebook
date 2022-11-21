from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from .forms import ContactForm
from django.contrib import messages


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
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your message has been sent, we'll respond as soon as we can!"
                )
            return render(
                request,
                "index.html",)

    contact_form = ContactForm()
    template = 'contact.html'
    context = {
        'contact_form': contact_form,
    }
    return render(request, template, context)
