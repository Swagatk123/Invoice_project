from django.urls import path

from .views import InvoiceListCreateAPIView,InvoiceDetailListCreateAPIView,APIRoot




urlpatterns = [
    path('', APIRoot.as_view(), name='api-root'),
    path('invoices/', InvoiceListCreateAPIView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceListCreateAPIView.as_view(), name='invoice-detail'),
    path('invoice-details/', InvoiceDetailListCreateAPIView.as_view(), name='invoice-detail-list-create'),
    path('invoice-details/<int:pk>/', InvoiceDetailListCreateAPIView.as_view(), name='invoice-detail-detail'),
]
