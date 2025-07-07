from django.shortcuts import render

# Create your views here.
def render_upload(request):
    return render(request, 'render/render_upload.html')