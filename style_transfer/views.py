
# import os
# import time
# from PIL import Image

# from django.core.files.images import ImageFile
# from django.shortcuts import render, get_object_or_404, redirect
# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# from django.http import HttpResponse

# from stylize.stylize import style
# from stylize import stylize
# from style_transfer.forms import UploadContentForm
# from style_transfer.models import Style


# # 追加
# from .forms import LoginForm, SignUpForm
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, authenticate


# # @login_required
# def home(request):
#     content = None
#     styles = Style.objects.all()
#     if request.method == 'POST' and request.FILES['content']:
#         content = request.FILES['content']
#         fs = FileSystemStorage(location=os.path.join(
#             settings.MEDIA_ROOT, 'content'))
#         filename = fs.save(content.name, content)
#         img_path = os.path.join(fs.location, filename)
#     return render(request, 'style_transfer/index.html', {'content': content, 'styles': styles})


# def apply_style_transfer(request):
#     if (request.method == 'GET' and request.GET['style_id']
#             and request.GET['img_name']):
#         style = get_object_or_404(Style, pk=request.GET['style_id'])
#         model_path = os.path.join(settings.MEDIA_ROOT, style.model.name)
#         img_path = os.path.join(settings.MEDIA_ROOT,
#                                 'content', request.GET['img_name'])
#         fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT,
#                                                      'results'))
#         result = stylize.style(img_path, model_path)
#         filename = 'result_' + str(int(time.time())) + '.jpg'
#         result.save(os.path.join(settings.MEDIA_ROOT, 'results', filename))
#         print('just made '+filename)
#         return HttpResponse('/media/results/' + filename)

# # 追加


# class Login(LoginView):
#     form_class = LoginForm
#     template_name = 'style_transfer/login.html'


# class Logout(LogoutView):
#     template_name = 'style_transfer/index.html'


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(to='index')
#     else:
#         form = SignUpForm()
#     return render(request, 'style_transfer/signup.html', {'form': form})


import os
import time
from PIL import Image

from django.core.files.images import ImageFile
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponse

from .forms import UploadContentForm
from .models import Style

from stylize import stylize


# 追加
from .forms import LoginForm, SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


@login_required
def home(request):
    content = None
    styles = Style.objects.all()
    if request.method == 'POST' and request.FILES['content']:
        content = request.FILES['content']
        fs = FileSystemStorage(location=os.path.join(
            settings.MEDIA_ROOT, 'content'))
        filename = fs.save(content.name, content)
        img_path = os.path.join(fs.location, filename)
    return render(request, 'style_transfer/index.html', {'content': content, 'styles': styles})


def apply_style_transfer(request):

    if (request.method == 'GET' and request.GET['style_id']
            and request.GET['img_name']):
        style = get_object_or_404(Style, pk=request.GET['style_id'])
        # model_path = os.path.join(settings.MEDIA_ROOT, style.model.name)
        model_path = os.path.join(settings.MEDIA_ROOT, style.model.name)
        print("確認_modelpath", model_path)
        img_path = os.path.join(settings.MEDIA_ROOT,
                                'content', request.GET['img_name'])
        print("確認_imgpath", img_path)
        fs = FileSystemStorage(location=os.path.join(
            settings.MEDIA_ROOT, 'results'))
        print("確認_fs", fs)
        result = stylize.style(img_path, model_path)
        filename = 'result_' + str(int(time.time())) + '.jpg'
        result.save(os.path.join(settings.MEDIA_ROOT, 'results', filename))
        print('just made '+filename)
        return HttpResponse('/media/results/' + filename)

# 追加


class Login(LoginView):
    form_class = LoginForm
    template_name = 'style_transfer/login.html'


class Logout(LogoutView):
    template_name = 'style_transfer/login.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='index')
    else:
        form = SignUpForm()
    return render(request, 'style_transfer/signup.html', {'form': form})
