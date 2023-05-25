from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from profiles.models import Profile
from .models import UserQuizModel, QuizModel
from .serializers import UserQuizSerializer, UserQuizAnsweredSerializer


class UserQuizViewSet(GenericViewSet, RetrieveModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = UserQuizModel.objects.filter(quiz__active=True)
    http_method_names = ['get', 'patch']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserQuizSerializer
        return UserQuizSerializer

    def retrieve(self, request, *args, **kwargs):
        # Try to get a created user_quiz by an authenticated user
        quiz_id = kwargs.get('pk')
        user_quiz = get_user_quiz_by_quiz_id(
            quiz_id=quiz_id, user_id=request.user.id)

        if user_quiz:
            serializer = self.get_serializer(user_quiz)
            return Response(serializer.data, status.HTTP_200_OK)

        # Else, create a new user_quiz instance
        quiz = QuizModel.objects.filter(id=quiz_id)

        if not quiz:
            return Response("Quiz with id: '" + quiz_id + "' not found", status.HTTP_404_NOT_FOUND)

        quiz = quiz.first()

        user_quiz = UserQuizModel.objects.create(quiz=quiz, user=request.user)
        serializer = self.get_serializer(user_quiz)
        return Response(serializer.data, status.HTTP_201_CREATED)

    @action(detail=True, methods=['patch'])
    def startAttempt(self, request, *args, **kwargs):
        # Try to get a created user_quiz by an authenticated user
        quiz_id = kwargs.get('pk')
        user_quiz = get_user_quiz_by_quiz_id(
            quiz_id=quiz_id, user_id=request.user.id)

        if not user_quiz:
            return Response("Quiz with id: '" + quiz_id + "' not found", status.HTTP_404_NOT_FOUND)

        if user_quiz.tries >= user_quiz.quiz.max_tries:
            return Response("Max tries reached for this quizz", status.HTTP_400_BAD_REQUEST)

        # Add a 'try' to the user_quiz instance
        user_quiz.tries += 1
        user_quiz.save()
        return Response("Starting quiz...", status.HTTP_200_OK)

    @action(detail=True, methods=['patch'])
    def finishAttempt(self, request, *args, **kwargs):
        # Try to get a created user_quiz by an authenticated user
        quiz_id = kwargs.get('pk')
        user_quiz = get_user_quiz_by_quiz_id(
            quiz_id=quiz_id, user_id=request.user.id)

        if not user_quiz:
            return Response("Quiz with id: '" + quiz_id + "' not found", status.HTTP_404_NOT_FOUND)

        # Correct the quiz made by the user
        userResponses = request.data['userResponses']
        questions = user_quiz.quiz.questions.values('id', 'correct_option')

        correctOptions = 0

        for i in userResponses:
            if i in questions:
                correctOptions += 1

        if correctOptions <= user_quiz.correct_answers:
            answeredQuiz = {"correct_answers": correctOptions, "points": 0}
            serializer = UserQuizAnsweredSerializer(answeredQuiz)
            return Response(serializer.data, status.HTTP_200_OK)

        obtained_points = correctOptions - user_quiz.correct_answers
        user_quiz.correct_answers = correctOptions
        user_quiz.save()

        add_points(user_id=request.user.id, obtained_points=obtained_points)

        answeredQuiz = {"correct_answers": correctOptions,
                        "points": obtained_points}
        serializer = UserQuizAnsweredSerializer(answeredQuiz)
        return Response(serializer.data, status.HTTP_200_OK)


def get_user_quiz_by_quiz_id(quiz_id, user_id):
    # Try to get a created user_quiz by an authenticated user and a quiz identificator
    user_quiz = UserQuizModel.objects.filter(
        quiz__id=quiz_id, user__id=user_id)

    if not user_quiz:
        return None

    return user_quiz.first()


def add_points(user_id, obtained_points):
    profile = Profile.objects.get(user__id=user_id)
    profile.points += obtained_points
    profile.obtained_points += obtained_points
    profile.save()
