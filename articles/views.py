from django.shortcuts import render
# render 와 redirect의 차이
# render : 어떤 요청이 왔을때 페이지를 띄워주겠다.

# Create your views here.

def index(request):
    # 로직
    return render(request, 'articles/index.html')