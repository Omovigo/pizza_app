from django.shortcuts import render, redirect 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method != 'POST': 
        # for blank registration page
        form = UserCreationForm()
    else:
        # process the completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # to login the new user and redirect them to the index page
            login(request, new_user)
            return redirect('pizza_app:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
