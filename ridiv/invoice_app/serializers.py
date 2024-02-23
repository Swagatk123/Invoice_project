from rest_framework import serializers
from .models import Invoice,Invoice_detail


        
class InvoiceDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = Invoice_detail
       fields =  '__all__'
       
class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Invoice
        fields = '__all__'

        

   
    

