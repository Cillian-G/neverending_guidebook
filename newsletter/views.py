from django.shortcuts import render

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from .forms import NewsletterForm
from django.contrib import messages


def newsletter(request):

    if request.method == 'POST':

        form_data = {
            'email': request.POST['email'],
            }
        
        newsletter_form = NewsletterForm(form_data)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'You have been added to our mailing list.'
                )
            return render(
                request,
                "index.html",)

    newsletter_form = NewsletterForm()
    template = 'newsletter.html'
    context = {
        'newsletter_form': newsletter_form,
    }
    return render(request, template, context)