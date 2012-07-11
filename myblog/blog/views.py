# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""
'''
<fieldset>
    <legend>Personalia:</legend>
    Name: <input type="text" /><br />
    Email: <input type="text" /><br />
    Date of birth: <input type="text" />
  </fieldset>
'''
from django.template import Context, loader
from django.http import HttpResponse
from models import Post, Comment
from django.shortcuts import render_to_response

def post_list(request):
    post_list = Post.objects.all()
    my_temp = loader.get_template('post_list.html')
    my_context = Context({
        'post': post_list,
        })
        
    return HttpResponse(my_temp.render(my_context))

def post_detail(request, id, showComments=False):
    post_list = Post.objects.filter(id = id)

    my_temp = loader.get_template('post_detail.html')
    if(showComments==u'True'):
        comments_list = Comment.objects.filter(post = id)
        my_context = Context({
            'post': post_list,
            'comments': comments_list,
            })
        return HttpResponse(my_temp.render(my_context))
    else:
        my_context = Context({
            'post': post_list,
            })
        return HttpResponse(my_temp.render(my_context))
    
def post_search(request, term):
    search_list = Post.objects.filter(post__icontains=term)

    my_temp = loader.get_template('post_search.html')
    my_context = Context({
        'term': term,
        'search': search_list,
        })
    return HttpResponse(my_temp.render(my_context))

def home(request):
    return render_to_response('base/base.html',{})
