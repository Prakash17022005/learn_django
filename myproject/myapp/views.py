from django.shortcuts import render

def home(request):
    
    context={
        'title':'welcome django',
        'message':"Hello",
        'items':['python','dijango','webdev']
    }
    return render(request,'myapp/home.html',context)

def about(request):
    return render(request,'myapp/about.html')