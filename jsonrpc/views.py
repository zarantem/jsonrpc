from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import login
from django.template.loader import render_to_string


def tls_authentication(request):
    response = render_to_string('jsonrpc/index.html')
    if not request.is_secure():
        return HttpResponse("Для доступа к этому ресурсу необходимо использовать HTTPS", status=403)


    if 'X-Auth-User' not in request.headers:
        return HttpResponse("Пользователь не авторизован", status=403)


    username = request.headers['X-Auth-User']
    user = User.objects.filter(username=username).first()


    if not user:
        return HttpResponse("Пользователь не найден", status=404)


    if not user.is_active:
        return HttpResponse("Пользователь не активен", status=403)


    user.backend = settings.AUTHENTICATION_BACKENDS[0]
    login(request, user)

    return HttpResponse(response)

