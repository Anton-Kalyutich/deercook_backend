from django.shortcuts import render
from rest_framework.views import APIView 
from . models import *
from rest_framework.response import Response 
from . serializer import * 
  
class RecipeView(APIView):

    serializer_class = RecipeSerializer 
  
    def get(self, request): 
        output = [ {"dish_name": recipe.dish_name,
            "description": recipe.description,
            "image": recipe.image.url if recipe.image else None}  
            for recipe in Recipe.objects.all()] 
        return Response(output) 
  
    def post(self, request):
        serializer = RecipeSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return Response(serializer.data) 

class ArticleView(APIView):

    serializer_class = ArticleSerializer 
  
    def get(self, request): 
        output = [ {"title": output.title,
            "content": output.content}  
            for output in Article.objects.all()] 
        return Response(output) 
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return Response(serializer.data)