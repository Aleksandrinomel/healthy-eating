import re

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ProfileForm, RegisterUserForm, LoginUserForm, ProfileUserForm
from .models import Food_rus, Profile, UserNeed, Need


def index_page(request):
    user_nutrients_dict = dict()
    user_nutrients_needs_dict = dict()
    # if request.user.is_authenticated:
    info = Profile.objects.filter(user=1).values('id', 'kfa', 'sex', 'age')

    user_nutrients = UserNeed.objects.filter(user=info[0]['id']).values('unit__title', 'nutrient_name__title', 'quantity')
    for row in user_nutrients:

        nutrient_title_list = re.split(r"-|,| ", row['nutrient_name__title'])
        user_nutrients_dict['_'.join(nutrient_title_list)] = [row['quantity'], row['unit__title']]

    user_nutrients_needs = Need.objects.filter(sex=info[0]['sex'], kfa=info[0]['kfa']).values('unit__title', 'nutrient_name__title', 'quantity', 'age')
    for row in user_nutrients_needs:
        if info[0]['age'] in range(int(row['age'].split('-')[0]), int(row['age'].split('-')[1])):
            nutrient_title_list = re.split(r"-|,| ", row['nutrient_name__title'])
            user_nutrients_needs_dict['_'.join(nutrient_title_list)] = [row['quantity'], row['unit__title']]
            # print(user_nutrients_needs_dict)
    print(user_nutrients_needs_dict)
    print(user_nutrients_dict)
    return render(request, 'healthapp/index.html', {'user_nutrients': user_nutrients_dict, 'user_nutrients_needs': user_nutrients_needs_dict})


@login_required
def profile(request):
    if request.method == "POST":
        user_profile_form = ProfileForm(request.POST, instance=request.user.profile)
        user_form = ProfileUserForm(request.POST, instance=request.user)
        if user_profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return redirect('profile')
    user_profile_form = ProfileForm(instance=request.user.profile)
    user_form = ProfileUserForm(instance=request.user)
    return render(request, 'healthapp/profile.html', {'user_profile_form': user_profile_form, 'user_form': user_form})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'healthapp/register.html'
    success_url = reverse_lazy('login')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'healthapp/login.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Авторизация")
    #     return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')

def logout_user(request):
    logout(request)
    return redirect('index')

# def login(request):
#     return render(request, 'healthapp/login.html')

# def register(request):
#     return render(request, 'healthapp/register.html')


def blank(request):
    return render(request, 'blank.html')

def buttons(request):
    return render(request, 'buttons.html')

def cards(request):
    return render(request, 'cards.html')

def charts(request):
    return render(request, 'charts.html')

def forgot_password(request):
    return render(request, 'forgot-password.html')



def tables(request):
    return render(request, 'tables.html')

def products(request):
    products_list = Food_rus.objects.all()
    return render(request, 'healthapp/products.html', {'products_list': products_list})

def utilities_animation(request):
    return render(request, 'utilities-animation.html')

def utilities_border(request):
    return render(request, 'utilities-border.html')

def utilities_color(request):
    return render(request, 'utilities-color.html')

def utilities_other(request):
    return render(request, 'utilities-other.html')

def index_page3(request):
    return render(request, 'healthapp/index3.html')


