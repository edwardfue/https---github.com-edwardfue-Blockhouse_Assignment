from django.db import models

class CandleStickchart(models.Model):
    Candle_data = models.JSONField()
    def __str__(self):
        return "Candlestick data"

class Linechart(models.Model):
    Linechart_data = models.JSONField()

    def __str__(self):
        return "Line Chart data."
    
class Barchart(models.Model):
    Barchart_data = models.JSONField()
    def __str__(self):
        return "Bar chart data."

class Piechart(models.Model):
    Piechart_data = models.JSONField()
    def __str__(self):
        return "Pie chart data"
    