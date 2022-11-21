from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import CheckoutForm
from guide.models import Patron
from django.contrib.auth.models import User

import stripe


# Add check for patron status
def checkout(request):
    patron = get_object_or_404(Patron, pk=request.user.id)
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if patron.patron_status is True:
        messages.error(request, "Your account is already patron status")
        return redirect(reverse('home'))

    if request.method == 'POST':

        form_data = {
            'email': request.POST['email']
            }

        checkout_form = CheckoutForm(form_data)
        if checkout_form.is_valid():
            checkout_form.save()
            patron.patron_status = True
            patron.save()
            return render(
                request,
                "upgrade_success.html",)

    # unauthenticated users wont be able to see the form,
    # so any users without accounts that access this page
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
