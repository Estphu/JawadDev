from django.shortcuts import render

# Create your views here.
def custom_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)

def custom_500_view(request):
    return render(request, 'errors/500.html', status=500)
