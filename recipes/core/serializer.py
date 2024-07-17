from rest_framework import serializers 
from . models import *
  
class RecipeSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Recipe 
        fields = ['dish_name', 'description', 'image']

class ArticleSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Article 
        fields = ['title', 'content'] 