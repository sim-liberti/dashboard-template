from django.shortcuts import render

def booklet(request):
    user = request.user
    context = {'user': user}
    return render(request, 'booklet/booklet.html', context=context)