from django.shortcuts import render, HttpResponse
from carga.models import carga
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
	busqueda=request.GET.get("prd")
	cargasss=carga.objects.all()
	if busqueda:
		cargasss=carga.objects.filter(Q(nombre__icontains=busqueda)).distinct()
	return render(request, "paginaCovid/home.html", {"cargasss": cargasss})

def perfil(request):
	return render(request, "paginaCovid/perfil.html")

def cargas(request):
	if request.method=="POST":
		subject="envio de usuario y contraseña"
		message="usuario:fabripasinato. contraseña:420823fabri"
		email_from=settings.EMAIL_HOST_USER
		recipient_list=["juegosfabri@outlook.com"]
		send_mail(subject, message, email_from, recipient_list)
		return render(request, "paginaCovid/cargass.html")	
	return render(request,"paginaCovid/cargass.html")

def contacto(request):
	if request.method=="POST":
		subject=request.POST["asunto"]
		message=request.POST["mensaje"] + "" + request.POST["email"]
		email_from=settings.EMAIL_HOST_USER
		recipient_list=["juegosfabri@outlook.com"]
		send_mail(subject, message, email_from, recipient_list)
		return render(request, "paginaCovid/contacto.html")
	return render(request, "paginaCovid/contacto.html")


	