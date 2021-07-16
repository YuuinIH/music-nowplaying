from django.shortcuts import render
from django.http import HttpResponse
import win32gui

def index(request):
    return render(request,'index.html')

def nowplaying(request):
    hwnd = win32gui.FindWindow('OrpheusBrowserHost', None)
    title = '0'
    if(hwnd != 0):
        title = win32gui.GetWindowText(hwnd)
    else:
        title = '未找到网易云窗口'
    return HttpResponse(title)