from django.shortcuts import render, HttpResponse


# 首页
def index(request):
    return render(request, 'tools/index.html')


# 在线生成二维码
def qrcode(request):
    return render(request, 'tools/qrcode.html')


# 在线 base64 加密解密
def base64(request):
    return render(request, 'tools/base64.html')


def convertion(request):
    return render(request, 'tools/convertion.html')