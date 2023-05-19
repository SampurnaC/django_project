from django.shortcuts import render
from .models import Post

# Create your views here.

# posts = [
#     {
#         'author': 'Sam',
#         'title': 'Blog Post 1',
#         'content': 'First Post',
#         'date_posted': 'August 27, 2020'
#     }, 
#     {
#         'author': 'Santosh',
#         'title': 'Blog Post 2',
#         'content': 'Second Post',
#         'date_posted': 'August 27, 2022'
#     }
# ]
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
 