Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def register():
     username = input ("create username:")
     password = input ("create password")
     password1 = input ("confirm passwor")
     if password != password1:
        print("passwords don't mactch,restart")
        register()
     else:
        if len(password)<=6:
           print("password too short restart:")
           register()
        else:
           print("ss")
           register()