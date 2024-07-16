from django.shortcuts import render
from rest_framework.views import APIView 
from . models import *
from rest_framework.response import Response 
from . serializer import * 
  
class RecipeView(APIView):

    serializer_class = RecipeSerializer 
  
    def get(self, request): 
        output = [ {"dish_name": output.dish_name,
            "description": output.description}  
            for output in Recipe.objects.all()] 
        return Response(output) 
  
    def post(self, request):
        serializer = RecipeSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return Response(serializer.data) 

