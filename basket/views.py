from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

def index(request):
	return render(request, 'basket/index.html', {'STRIPE_PUBLIC_KEY':settings.STRIPE_PUBLIC_KEY})


def charge(request):


	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='gbp',
			description="Donation"
			)

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'basket/success.html', {'amount':amount})