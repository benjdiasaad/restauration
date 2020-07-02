from django.conf.urls import url
from django.urls import path
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from .models import Restaurant,Dish,RestaurantReview
from .forms import RestaurantForm, DishForm
from .views import RestaurantCreate, DishCreate, RestaurantDetail, review, UpdateRestaurant

app_name = 'myrestaurants'

urlpatterns = [
    # List latest 5 restaurants: /myrestaurants/
    url(r'^$',
        ListView.as_view(
            queryset=Restaurant.objects.all().order_by('date')[:5],
            context_object_name='latest_restaurant_list',
            template_name='myrestaurants/restaurant_list.html'),
        name='restaurant_list'),

    # Restaurant details, ex.: /myrestaurants/restaurants/1/
    url(r'^restaurants/(?P<pk>\d+)/$',
        RestaurantDetail.as_view(),
        name='restaurant_detail'),

    # Restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Dish,
            template_name='myrestaurants/dish_detail.html'),
        name='dish_detail'),

    # Create a restaurant, /myrestaurants/restaurants/create/
    url(r'^restaurants/create/$',
        RestaurantCreate.as_view(),
        name='restaurant_create'),

    # Edit restaurant details, ex.: /myrestaurants/restaurants/1/edit/
    url(r'^restaurants/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Restaurant,
            template_name='myrestaurants/form.html',
            form_class=RestaurantForm),
        name='restaurant_edit'),

    # Create a restaurant dish, ex.: /myrestaurants/restaurants/1/dishes/create/
    url(r'^restaurants/(?P<pk>\d+)/dishes/create/$',
        DishCreate.as_view(),
        name='dish_create'),

    # Edit restaurant dish details, ex.: /myrestaurants/restaurants/1/dishes/1/edit/
    # url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/edit/$',
    #     UpdateView.as_view(
    #         ),
    #     name='dish_edit'),
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/edit/$', UpdateRestaurant.as_view(), name='dish_edit'),

    # Create a restaurant review, ex.: /myrestaurants/restaurants/1/reviews/create/
    url(r'^restaurants/(?P<pk>\d+)/reviews/create/$',
        review,
        name='review_create'),
]
