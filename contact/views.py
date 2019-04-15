from django.shortcuts import render, redirect
from .contactform import ContactForm
from django.contrib import messages


# Create your views here.
def ContactView(request):

	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			messages.success(request, 'Recebemos a sua mensagem. Entraremos em contacto assim que possível!')
			form.save()
			return redirect('contact')
	else:
		form = ContactForm()

	context = {
		'form': form,
	}

	return render(request, 'contact/contact.html', context)