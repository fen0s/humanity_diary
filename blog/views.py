from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Post, Ip
from django.views import generic


# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail_post.html'

class PostListView(generic.ListView):

    model = Post
    paginate_by = 10

    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-date')

def submit_view(request):
    from .forms import PostForm
    ip = get_ip(request)
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if Ip.objects.filter(ip__contains=ip):
            return render(request, 'blog/submit.html', {'form': form, 'error': "You've posted to diary already!"})
        
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            Ip(ip=ip).save()
            return redirect('detail_post', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/submit.html', {'form': form})

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip