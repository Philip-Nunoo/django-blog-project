# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse
from models import Post, Comment 

def post_list(request):
    post_list = Post.objects.all()
    
    response = "<table border=1><tr><th>Title</th><th>Author</th><th>Date Created</th><th>Date updated</th></tr>"
    for p in post_list:
        response +="<tr><td>"+str(p.title)+"</td><td>"+str(p.author)+"</td><td>"+str(p.date_created)+"</td><td>"+str(p.date_updated)+"</td></tr>"
    response +="</table>"
   # print type(post_list)
   # print post_list
    
    return HttpResponse(response)

def post_detail(request, id, showComments=False):
    post_list = Post.objects.filter(id = id)
    response = "<b>Post contains:</b> "
    if post_list:   #checks if the query returned a result
        for p in post_list:
            response+="<br/>Post with:<br/><b>Title:</b> "+str(p.title)
            response+="<br/><b>Author: </b>"+str(p.author)
            response+="<br/><b>Date Created: </b>"+str(p.date_created)
            response+="<br/><b>Post:</b><br/><textarea rows='2' cols='20' disabled style='color: black'>"+str(p.post)+"</textarea>"
            print type(showComments)
            if(showComments==u'True'):
                comments_list = Comment.objects.filter(post = id)
                for q in comments_list:
                    comments ="<br/><b>Comments:</b><br/><textarea rows='2' cols='20' disabled>"+str(q.comment)+"</textarea>"
                
                response+=comments
    else:
        response+="<br/>No post with id <b>"+str(id)+"</b>"
    return HttpResponse(response)
    
def post_search(request, term):
    response = "post_search"
    return HttpResponse(response)

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
