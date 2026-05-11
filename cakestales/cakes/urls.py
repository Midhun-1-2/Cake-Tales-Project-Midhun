from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.HomeView.as_view(),name='home'),

    path('add-a-cake/',views.AddACakeView.as_view(),name='add-a-cake'),

    path('cake-details/<str:uuid>/',views.CakeDetailsView.as_view(),name='cake-details'),

    path('cake-edit/<str:uuid>/',views.CakeEditView.as_view(),name='cake-edit'),

    path('cake-delete/<str:uuid>/',views.CakeDeleteView.as_view(),name='cake-delete'),

    path('add-to-whishlist/<str:uuid>/',views.AddtoWishlist.as_view(),name='add-to-whishlist'),

    path('remove-wishlist/<str:uuid>/',views.Removefromwishlist.as_view(),name='remove-wishlist'),

    path('wishlist/',views.WishListView.as_view(),name='wishlist'),

    path('add-to-cart/<str:uuid>/',views.AddtoCart.as_view(),name='add-to-cart'),

    path('remove-from-cart/<str:uuid>/',views.RemovefromCart.as_view(),name='remove-from-cart'),

    path('checkout/',views.CheckOutView.as_view(),name='checkout'),

    path('place-order/<str:uuid>/',views.OrderPlacedView.as_view(),name='place-order'),

    path('orders/',views.OrdersView.as_view(),name='orders'),

    path('orderdetails/<str:uuid>/',views.OrderDetailsView.as_view(),name='orderdetails'),
]


