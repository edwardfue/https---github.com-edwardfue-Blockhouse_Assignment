from rest_framework import serializers
from .models import CandleStickchart,Linechart,Barchart,Piechart

class CandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandleStickchart
        fields = '__all__'

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linechart
        fields = '__all__'

class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barchart
        fields = '__all__'

class PieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piechart
        fields = '__all__'