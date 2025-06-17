from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
from .models import Resource, User
from .forms import ResourceForm

class ResourceView(generic.ListView):
    context_object_name = 'resource_data'
    template_name = 'training/index.html'

    def get_queryset(self):
        return Resource.objects.all()

class UserView(generic.ListView):
    context_object_name = 'resource_data'
    template_name = 'training/personal.html'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return  Resource.objects.filter(user_id=pk)
    
def add(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    # if request.method == "POST":
        #try:
    form = ResourceForm(request.POST) 
    if form.is_valid():
        resource = Resource(
            title=form.cleaned_data['title'],
            notion_link=form.cleaned_data['notion_link'],
            training_date=form.cleaned_data['training_date'],
            user=user,
            team=form.cleaned_data['team']
        ) 
        resource.save()

        return HttpResponseRedirect("/thanks")

    return render(request, "training/add.html", {"form": form, "user": user})

