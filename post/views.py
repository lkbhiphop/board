from django.shortcuts import render, redirect, resolve_url
from .forms import PostForm
# .forms.py가 가지고 있는 PostForm
from .models import Post
from html.parser import HTMLParser

# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request,'post/list.html',{'posts':posts})
    
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        #저장로직
        # HTML코드로 바꿔주는 코드가 PostForm
        # request.POST -- 이 안에 들어가 있다. 에러를 보면 확인할 수 있다.
        # 이정보를 PostForm에 넣었따.
        if form.is_valid():
        # 제대로된 정보를 입력했는지를 위한 것(컬럼마다 규칙을 맞춰입력했는지 확인하는 것이 validation작업이다)
            # title = form.POST.get이었따
            title = form.cleaned_data['title']
            # or title = form.cleand_data.get('title')
            content = form.cleaned_data.get('content')
            
            # Post 모델의 객체를 생성하는 단계
            Post.objects.create(title = title , content = content)
            
            return redirect(resolve_url('post:list'))
            #만들고 싶은 url에 대한 경로를 넣어준다.
    else :
        #입력할 수 있는 form 리턴
        form = PostForm()
    return render(request,'post/create.html',{'form':form})
    
def detail(request,id):
    post = Post.objects.get(id = id)
    return render(request, 'post/detail.html', {'post':post})
    