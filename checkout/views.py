from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import CheckoutForm

import stripe

# Add check for patron status
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    patron_status = False
    if patron_status:
        messages.error(request, "Your account is already patron status")
        return redirect(reverse('home'))
    
    # unauthenticated users wont be able to see the form, so any users without accounts that access this page
    # will get an error message in html
    # Patron upgrade cost listed in cents 
    patron_upgrade_cost = 2500
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=patron_upgrade_cost,
        currency=settings.STRIPE_CURRENCY,
    )

    checkout_form = CheckoutForm()
    template = 'upgrade.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }   

    return render(request, template, context)


    #user = get_bjector4040
    #user.patron_status = True
    #user.save