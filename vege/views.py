from django.shortcuts import render,redirect
from .models import Recipe, User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_description,
        )

    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
    context = {
        'recipes':queryset
    }
    return render(request, "recipes.html", context)


def update_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    if request.method == "POST":
        data =request.POST
        
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name =recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipes/')
    
    context = {
        'recipes':queryset
    }
    return render(request, 'update_recipes.html', context)


def delete_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')



def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')
            return redirect('login')
        
        user = authenticate(username = username, password=password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('login')
        
        else:
            login(request,user)
            return redirect('recipes')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('login')


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")


        user = User.objects.filter(username = username)

        if user.exists():
            messages.warning(request, "Username Already Taken.")
            return redirect('sign_up')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username= username,
            password=password
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully!!!")
        
        return redirect('login')
    return render(request, 'register.html')