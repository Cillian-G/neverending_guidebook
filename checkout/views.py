from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import CheckoutForm

# Add check for patron status
def checkout(request):
    patron_status = False
    if patron_status:
        messages.error(request, "Your account is already patron status")
        return redirect(reverse('home'))
    
    #unauthenticated users wont be able to see the form, so any users without accounts that access this page
    #will get an error message in html

    checkout_form = CheckoutForm()
    template = 'upgrade.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': 'pk_test_51Li1KkBsxJQ4yPXp9RXMBfi2sDkcB9QujqRKv7ldCCvWxtVtC5caguO9WeEL5Gj8OEV4NugbASdrr4NYDSNRSOlf007uvO8Ydn',
        'client_secret': 'test_client_secret'
    }   

    return render(request, template, context)