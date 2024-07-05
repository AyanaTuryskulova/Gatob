from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Photo, Comment, Category, News
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    news_list = News.objects.all()
    context = {
        'categories': categories,
        'photos': photos,
        'news': news_list
    }
    return render(request, 'photos/gallery.html', context)

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    context = {'news_item': news_item}
    return render(request, 'photos/news_detail.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

def addPhoto(request):
    return render(request, 'photos/add.html')

def registration_view(request):
    return render(request, 'registration.html')

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    comments = photo.comments.all()
    return render(request, 'photo_detail.html', {'photo': photo, 'comments': comments})

@csrf_exempt
def like_photo(request, pk):
    if request.method == 'POST':
        photo = get_object_or_404(Photo, pk=pk)
        photo.likes += 1
        photo.save()
        return JsonResponse({'likes': photo.likes})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def like_news(request, pk):
    if request.method == 'POST':
        news_item = get_object_or_404(News, pk=pk)
        news_item.likes += 1
        news_item.save()
        return JsonResponse({'likes': news_item.likes})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def add_comment(request, pk):
    if request.method == 'POST':
        photo = Photo.objects.filter(pk=pk).first()
        news_item = News.objects.filter(pk=pk).first()
        comment_text = request.POST.get('text')
        if comment_text:
            if photo:
                Comment.objects.create(photo=photo, text=comment_text)
                comments = photo.comments.values('text', 'created_at')
            elif news_item:
                Comment.objects.create(news=news_item, text=comment_text)
                comments = news_item.comments.values('text', 'created_at')
            else:
                return JsonResponse({'error': 'Invalid request'}, status=400)
            return JsonResponse({'comments': list(comments)})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход
            return redirect('gallery')  # Перенаправление на главную страницу
    else:
        form = UserCreationForm()
    return render(request, 'photos/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('gallery')
    else:
        form = AuthenticationForm()
    return render(request, 'photos/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')