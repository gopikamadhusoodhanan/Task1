
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import BlogPost, CATEGORY_CHOICES
from .forms import BlogPostForm
from .serializers import BlogPostSerializer
def homepage(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:login')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Attempting to authenticate: username={username}, password={password}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(f"Authentication successful: user={user}")
            if user.user_type == 'patient':
                return redirect('accounts:patient_dashboard')
            else:
                return redirect('accounts:doctor_dashboard')
        else:
            print(f"Authentication failed for username: {username}")
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html', {'user': request.user})

@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author_id = request.user.id
            blog_post.save()
            return redirect('accounts:my_posts')
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def my_posts(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'my_posts.html', {'posts': posts})
def public_posts(request):
    categories = CATEGORY_CHOICES
    posts_by_category = {category[0]: BlogPost.objects.filter(category=category[0], is_draft=False) for category in categories}
    return render(request, 'public_posts.html', {'posts_by_category': posts_by_category})

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer