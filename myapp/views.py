from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.signing import Signer
from .models import SignedDataObject

def set_cookie(request):
    response = render(request, 'myapp/set_cookie.html')
    response.set_cookie('my_cookie', 'Hello, this is a cookie!')
    return response

def set_session(request):
    request.session['my_session'] = 'Hello, this is a session!'
    return render(request, 'myapp/set_session.html')

def show_message(request):
    messages.success(request, 'This is a success message!')
    return render(request, 'myapp/show_message.html')

def sign_data(request):
    signer = Signer()
    data_to_sign = 'This is signed data.'
    signed_data = signer.sign(data_to_sign)

    signed_data_object = SignedDataObject(data=data_to_sign, signature=signed_data)
    signed_data_object.save()

    signed_data_objects = SignedDataObject.objects.all()

    return render(request, 'myapp/sign_data.html', {'signed_data': signed_data})

