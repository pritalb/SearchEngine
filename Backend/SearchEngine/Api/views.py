from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from Search import utils

@api_view(['GET',])
def search(request, query):
    keywords = query.split(' ')
    results = utils.search(keywords)

    return Response(results)