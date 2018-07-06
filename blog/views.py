from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post

# Create your views here.
def index (request):
    #all_posts = Post.objects.all()
    all_posts = get_list_or_404(Post.objects.all())
    context={'all_posts': all_posts}
    return render(request, 'blog/index.html',
                context,
                content_type=None,
                status=None,
                using=None)
    
def blogdetail (request, idpost):
    print("Method: " + request.method)
    print("Value: " + request.content_type)
    print("Path: " + request.path)
    print("IdPost: " + idpost)
    #post = Post.objects.get(pk=idpost)
    post = get_object_or_404(Post, pk = idpost)
    return render(request, 'blog/blogdetail.html', 
                context={'Post': post}, 
                content_type=None, 
                status=None, 
                using=None)

def save (request, idpost):
    try:
        post = Post.objects.get(pk=request.POST['idpost'])
    except (KeyError, Post.DoesNotExist):
        return render( request, 'blog/blogdetail.html', {
            'Post': post,
            'error_message': "You didn't save a Valid Post",
            })
    else:
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.date = request.POST['date']
        post.save()
        return render(request, 'blog/blogdetail.html', {'Post': post})
        