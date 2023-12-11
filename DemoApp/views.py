from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home(request):
#     return render(request,'home.html')
# def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return HttpResponse('Ph:8637553742')
# def detail(request):
#     return HttpResponse("Here s a simplified example to explain the process. Say you ask friends to guess a number between 1 and 100. Your friends don’t have to guess the exact number; they just have to be the first to guess a number less than or equal to your number. If you are thinking of the number 19 and a friend comes up with 21, another 55, and yet another 83, they lose because they all guessed more than 19. But if you have three friends left, and the next one guesses 16, they win, and the others don't get a chance to guess. The one that guessed 16 was the first to guess a number less than or equal to 19.")
# def thanks(request):
#     return render(request,'thanks.html')
def index(request):
    return render(request,'index.html')
# def calculation(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     val1=x+y
#     val2=x-y
#     val3=x*y
#     val4=x/y
#     return render(request,'calculate.html',{'add':val1,'sub':val2,'mul':val3,'div':val4})