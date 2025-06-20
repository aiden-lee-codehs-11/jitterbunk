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
        return Resource.objects.filter(user_id=pk)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        user = User.objects.get(pk=pk)
        context['username'] = user.username
        return context

class TeamView(generic.ListView):
    context_object_name = 'resource_data'
    template_name = 'training/team.html'

    def get_queryset(self):
        return Resource.objects.filter(team=self.kwargs.get('team'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = self.kwargs.get('team')  
        return context


def thanks_view(request):
    return render(request, "training/thanks.html")
    
def add(request, user_id):
    user = get_object_or_404(User, pk=user_id)

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

        return HttpResponseRedirect("/training/thanks")

    return render(request, "training/add.html", {"form": form, "user": user})

