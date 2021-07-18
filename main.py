import win32gui

def findcloudmusictext():
    hwnd = win32gui.FindWindow('OrpheusBrowserHost', None)
    if(hwnd != 0):
        return win32gui.GetWindowText(hwnd)
    else:
        return '未找到网易云窗口'

print(findcloudmusictext())