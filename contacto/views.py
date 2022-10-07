
from django.shortcuts import render,redirect
from .forms import FormularioContacto
from  django.core.mail import send_mail,  EmailMessage

# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContacto()
    
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")


            email=EmailMessage(
                    subject = 'Realizando pruebas',
                    body = (contenido),
                    from_email = 'anuelmiguel8@gmail.com',
                    to =[email],
                    reply_to = [email],
)
            #un try catch para control de errores
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request,"contacto/contacto.html",{'miFormulario':formulario_contacto})