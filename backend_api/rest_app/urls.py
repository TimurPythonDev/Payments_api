from django.urls import path

from django.views.decorators.csrf import csrf_exempt
# local
from .views import ProductPreview,CreateCheckOutSession,stripe_webhook_view



urlpatterns = [
    path('stripe-webhook/', stripe_webhook_view, name='stripe-webhook'),
    path('product/<int:pk>/', ProductPreview.as_view(), name="product"),
    path('create-checkout-session/<pk>/', csrf_exempt(CreateCheckOutSession.as_view()), name='checkout_session')
]
