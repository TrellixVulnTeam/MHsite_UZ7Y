from django.shortcuts import render, redirect
from django.views.generic import TemplateView,  CreateView, DetailView, UpdateView
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.template import loader

from datetime import datetime
from string import ascii_uppercase
from random import randint

from users.models import Cart
from catalog.models import Item
from .models import Order, Profile


import stripe

date = str(datetime.now())[:10].split('-')
hour = str(datetime.now())[11:16].split(':')
order_id = ''.join(date)+''.join(hour)+ascii_uppercase[randint(0,20)]+ascii_uppercase[randint(0,20)]+str(randint(0,100))+str(randint(0,100))+'Order'	

stripe.api_key = settings.STRIPE_SECRET_KEY

class OrderCreateView(CreateView):

	model = Order
	fields = ['nome_completo', 'email', 'rua', 'numero', 'andar', 'localidade', 'distrito', 'codigo_postal_1', 'codigo_postal_2']

	def form_valid(self, form):

		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		
		self.object = form.save(commit=False)
		if self.request.user.is_authenticated:
			self.object.user = self.request.user
		else:
			self.object.user= User.objects.get(username='DummyUser')
		self.object.cart = cart_obj
		self.object.order_id = order_id
		self.object.total = cart_obj.subtotal	
		self.object.save()

		
		return HttpResponseRedirect(self.get_success_url())

class OrdereditView(UpdateView):
	model = Order
	fields = ['nome_completo', 'rua', 'numero', 'andar', 'localidade', 'distrito', 'codigo_postal_1', 'codigo_postal_2']
	template_name_suffix = '_update_form'

def OrderDetailView(request, slug):
	
	order = get_object_or_404(Order, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	template = 'payments/orderdetail.html'

	context = {'order': order}

	return render(request, template, context)

def OrderFinal(request, slug):
	order = get_object_or_404(Order, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	template = 'payments/orderfinish.html'

	if 'Online' in request.POST:
		order.ordered_through = 'online'
		order.is_ordered = True
		product_list = list(cart_obj.products.all()) #This does return the reference.
		order.items = product_list
		order_total = order.total*100

		order.save()

	context = {'order': order, 'key': settings.STRIPE_PUBLISHABLE_KEY, "total": order_total}

	return render(request, template, context)

def charge(request, slug):
	order = get_object_or_404(Order, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	template = 'payments/charge.html'
	if request.method == 'POST':
		charge = stripe.Charge.create(
        	amount= order.total*100,
        	currency='eur',
			description=f'order.id',
			source=request.POST['stripeToken']
		)

	for obj in cart_obj.products.all():
		cart_obj.products.remove(obj)

	return render(request, template, {"order":order})


def OrderConfirmed(request, slug):
	order = get_object_or_404(Order, slug=slug)
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	template = 'payments/orderfinal.html'

	if 'CTT' in request.POST:
		order.ordered_through = 'ctt'
		order.is_ordered = True
		product_list = list(cart_obj.products.all()) #This does return the reference.
		order.items = product_list
		
		order.save()

		for obj in cart_obj.products.all():
			cart_obj.products.remove(obj)

	def email(request):
		subject = 'Confirmação da sua encomenda'
		message = 'teste'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = list(order.email)
		html_message = loader.render_to_string(
			'user/password_reset_complete.html',{
			'username': User.username,
			'order' : order.items,
			'total' : order.total,
				}
			)
		print('working')
		send_mail( subject, 
			message, 
			email_from, 
			recipient_list, 
			fail_silently=True, 
			html_message=html_message)
	
	#Add email function somewhere around here.

	context = {'order': order}

	return render(request, template, context)

def ProfileView(request):
	user = request.user
	order = Order.objects.all().filter(user=user)[0:].order_by('-timestamp')
	context = {
		'user':user,
		'order':order,
	}
	template = 'payments/profile.html'
	return render(request, template, context)

def ProfileOrderView(request, slug):
	order = get_object_or_404(Order, slug=slug)
	template = "payments/profile_order.html"
	context = {'order':order}
	return render(request, template, context)
