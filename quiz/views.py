import random

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random

@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")
#개수만큼 랜덤한 퀴즈를 반환하는 api
@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True) # 다수의 데이터에 대해서도 직렬화 가능
    return Response(serializer.data)