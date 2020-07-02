from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import RestaurantReview, Restaurant, Dish
from .forms import RestaurantForm, DishForm
from django.views.generic import TemplateView

#pour affichage de detail d'un restaurant
class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'myrestaurants/restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context
#pour generer des formulaire
class RestaurantCreate(CreateView):
    model = Restaurant
    template_name = 'myrestaurants/form.html'
    form_class = RestaurantForm
    
    #pour montrer ce qui est dans navbar
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Create Restaurant"
        context['latest_restaurant_list'] = Restaurant.objects.all().order_by('date')[:5]
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)

# creation des plats
class DishCreate(CreateView):
    model = Dish
    template_name = 'myrestaurants/form.html'
    form_class = DishForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Create Dish"
        context['latest_restaurant_list'] = Restaurant.objects.all().order_by('date')[:5]
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        return super(DishCreate, self).form_valid(form)

# Modification de restaurant
class UpdateRestaurant(UpdateView):
    model = Dish,
    template_name = 'myrestaurants/form.html',
    form_class = DishForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Edit Restaurant"
        context['latest_restaurant_list'] = Restaurant.objects.all().order_by('date')[:5]
        return context

def review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    review = RestaurantReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        restaurant=restaurant)
    review.save()
    return HttpResponseRedirect(reverse('myrestaurants:restaurant_detail', args=(restaurant.id,)))
