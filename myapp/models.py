from django.db import models  

class Airport(models.Model):
    name = models.CharField(max_length=100, db_column='airport_name')
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    code = models.CharField(max_length=10,db_column='iata_code')
    timezone = models.CharField(max_length=100)

    class Meta:
        db_table = 'airport_info'  
