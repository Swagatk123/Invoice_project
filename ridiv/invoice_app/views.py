from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import InvoiceDetailSerializer,InvoiceSerializer
from .models import Invoice,Invoice_detail
# Create your views here.

class APIRoot(APIView):
    def get(self, request):
        return Response({
            'invoices': 'http://127.0.0.1:8000/api/invoices/',
            'invoice-details': 'http://127.0.0.1:8000/api/invoice-details/'
        })

class InvoiceListCreateAPIView(APIView):
    def get(self):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            invoice = Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            invoice = Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InvoiceSerializer(invoice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, pk):
        try:
            invoice = Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InvoiceDetailListCreateAPIView(APIView):
    def get(self):
        invoice_details = Invoice_detail.objects.all()
        serializer = InvoiceDetailSerializer(invoice_details, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvoiceDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            invoice_detail = Invoice_detail.objects.get(pk=pk)
        except Invoice_detail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InvoiceDetailSerializer(invoice_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            invoice_detail = Invoice_detail.objects.get(pk=pk)
        except Invoice_detail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InvoiceDetailSerializer(invoice_detail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        try:
            invoice_detail = Invoice_detail.objects.get(pk=pk)
        except Invoice_detail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        invoice_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
