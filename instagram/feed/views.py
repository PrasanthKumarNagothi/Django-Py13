from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.


def homepage(request):
    posts = Post.objects.all()
    return render(request, 'feed/home.html', {"posts" : posts})

@login_required(login_url='login')
def upload(request):
    if request.method == 'POST':
        image = request.FILES['image']
        caption = request.POST['caption']
        Post.objects.create(
            image=image,
            caption=caption,
            userid_id = request.user.id
        )
        return redirect('upload')
    return render(request, 'feed/upload.html')