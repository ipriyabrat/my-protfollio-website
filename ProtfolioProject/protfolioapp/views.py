from django.shortcuts import render,get_object_or_404
from protfolioapp.models import Post    
from django.core.mail import send_mail
from protfolioapp.forms import MailSendForm

# Create your views here.
 
def home_view(request):
    post_list=Post.objects.all()
    return render(request,'testapp/home.html',{'post_list':post_list})


def about_view(request):
    return render(request,'testapp/about.html')


def post_detail_view(request,year,month,day,post):
    post= get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)

    return render(request,'testapp/post_details.html',{'post':post})


# def mail_send_view(request):
#      post = get_object_or_404(Post,status='published')
#      sent = False

#      if request.method == 'POST':
#         form = MailSendForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             #.....send email
#             post_url = request.build_absolute_uri(post.get_absolute_url())
#             subject = f"{cd['name']} recommends you read" f"{post.title}"
#             message = f"Read {post.title} at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
#             send_mail(subject,message,'pythonbubu21@gmail.com', [cd['to']])
#             sent = True
#      else:
#         form = MailSendForm()
#      return render(request,'blog/post/mail.html',{'post':post,
#                                                   'form':form,
#                                                   'sent':sent}) 