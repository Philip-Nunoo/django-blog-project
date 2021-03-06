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
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

#####Class for Form Comments####
class CommentForm(ModelForm):
    class Meta:
        exclude=['post','author']
        model = Comment

####View to edit comment####
@csrf_exempt    #what is csrf_exempt if we don't Django gives us a security error
def edit_comment(request, id):
    comment_edit = Comment.objects.get(id = id)
    if request.method == "POST":
        form = CommentForm(request.POST,instance=comment_edit)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/blog/posts/"+str(comment_edit.post.id))
    else:
        form = CommentForm(instance = comment_edit)
        
    my_temp=loader.get_template('edit_comment.html')
    my_context=Context({
            'edit':comment_edit,
            'form':form,
        })
    return HttpResponse(my_temp.render(my_context))

####View to list All Posts#####
def post_list(request):
    post_list = Post.objects.all()
    my_temp = loader.get_template('post_list.html')
    my_context = Context({
        'post': post_list,
        })
        
    return HttpResponse(my_temp.render(my_context))

#####View for Details of post#####
@csrf_exempt    #what is csrf_exempt if we don't Django gives us a security error
def post_detail(request, id, showComments= False):
    post_list = Post.objects.get(id = id)
    comments_list = Comment.objects.filter(post = id)
    comment = Comment(post = post_list)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = CommentForm()
        
    my_context = Context({
        'post': post_list,
        'comments': comments_list,
        'form': form,
        'showComments': showComments,
        })
    return render_to_response('post_detail.html',my_context)

#####Searching Through Post#######
def post_search(request, term):
    search_list = Post.objects.filter(post__icontains=term)

    my_temp = loader.get_template('post_search.html')
    my_context = Context({
        'term': term,
        'search': search_list,
        })
    return HttpResponse(my_temp.render(my_context))

#####View for the Home url#####
def home(request):
    return render_to_response('base/base.html',{})
