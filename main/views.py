from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275405',
        'name': 'Aliyah Nahisa Sugiana',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)