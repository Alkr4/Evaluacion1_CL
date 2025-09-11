from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user and user.organization:
            request.session['organization_id'] = user.organization.id
            return redirect('dashboard')
        else:
            return render(request, 'usuarios/login.html', {'error': 'Credenciales incorrectas'})
    else:
        return render(request, 'usuarios/login.html')
    
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = f"Gracias por registrar la empresa!!"
        return render(request, 'usuarios/register_done.html', {'message': message, 'email': email})

    return render(request, 'usuarios/register.html')

def logout(request):
    request.session.flush()
    return redirect('login')