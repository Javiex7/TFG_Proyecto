from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


from .models import Profile
from .serializers import ProfileSerializer, DetailedProfileSerializer


class ProfileViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    http_method_names = ['get', 'patch']

    @action(detail=False, methods=['get'])
    def getProfile(self, request, *args, **kwargs):
        # Get the associated profile of the authenticated user
        try:
            user_profile = Profile.objects.get(user__id=request.user.id)
            serializer = ProfileSerializer(user_profile)
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response("Error sending the profile information of the user: " + request.user.email, status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def getRanking(self, request, *args, **kwargs):
        # Get the ranked profiles that have the same group as the user
        try:
            group = Profile.objects.get(user__id=request.user.id).group
            ranking = Profile.objects.filter(
                group=group).order_by("-obtained_points")
            if not ranking or not group:
                return Response("Ranking of user/group not found", status.HTTP_404_NOT_FOUND)

            serializer = ProfileSerializer(ranking, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response("Error sending the user group ranking", status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def getDetailedProfile(self, request, *args, **kwargs):
        # Get the associated profile of the authenticated user with all the available fields
        try:
            user_profile = Profile.objects.get(user__id=request.user.id)
            serializer = DetailedProfileSerializer(user_profile)
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response("Error sending the detailed profile information of the user: " + request.user.email, status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['patch'])
    def updateProfile(self, request, *args, **kwargs):
        # Patch/Update the associated profile of the authenticated user
        try:
            user_profile = Profile.objects.get(user__id=request.user.id)
            sent_data = False

            if "email" in request.data:
                newEmail = request.data['email']
                if (Profile.objects.filter(user__username=newEmail)):
                    return Response("That user email has already been taken", status.HTTP_400_BAD_REQUEST)
                user_profile.user.email = newEmail
                user_profile.user.username = newEmail
                sent_data = True
            if "group" in request.data:
                user_profile.group = request.data['group']
                sent_data = True

            if not sent_data:
                return Response("No user info given to the user patch/update of the user" + request.user.email, status.HTTP_400_BAD_REQUEST)

            user_profile.user.save()
            serializer = DetailedProfileSerializer(user_profile)

            return Response(serializer.data, status.HTTP_200_OK)

        except:
            return Response("Error sending the updated information of the user: " + request.user.email, status.HTTP_400_BAD_REQUEST)
