from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import FeedbackData
from .forms import FeedbackForms
import datetime as dt
date1=dt.datetime.now()

def Feedback_view(request):
    if request.method=="POST":
        fform=FeedbackForms(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feedback=request.POST.get('feedback')

            data=FeedbackData(
                name=name,
                rating=rating,
                date=date1,
                feedback=feedback
            )
            data.save()
            fform=FeedbackForms()
            fdata=FeedbackData.objects.all()
            return render(request,'feedback.html',{'fform':fform,'fdata':fdata})
        else:
            return HttpResponse('User Invalid data')


    else:
        fform=FeedbackForms()
        fdata = FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform':fform,'fdata':fdata})