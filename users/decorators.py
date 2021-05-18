from django.shortcuts import redirect

def unathenticated_user(func):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('books:index')
        else:
             return func(request,*args,**kwargs)
    return wrapper_function
