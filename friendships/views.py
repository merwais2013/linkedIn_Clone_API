from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import FriendshipSerializer
from .models import Friendship


User = get_user_model()

class UserListView(APIView):
  # permission_classes = [IsAuthenticated]

  def get(self, request):
    users = User.objects.filter(is_staff=False, is_superuser=False, is_active=True)
    # users = User.objects.all()
    serializer = FriendshipSerializer(users, many=True)
    return Response(serializer.data)


class RequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
       try:
          user_id = request.data.get('user')
          user = User.objects.get(pk=user_id)
       except User.DoesNotExist:
          return Response(status=status.HTTP_400_BAD_REQUEST)

       Friendship.objects.get_or_create(request_from=request.user, request_to=user)

       return Response({'detail': 'Request sent.'})

class RequestListView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
     frienship = Friendship.objects.filter(request_to=request.user, is_accepted=False)
     users = [fr.request_from for fr in frienship]
     serializer = FriendshipSerializer(users, many=True)
     return Response(serializer.data)

class AcceptView(APIView):
   permission_classes = [IsAuthenticated]

   def post(self, request):
      user_id = request.data.get('user')
      try:
         user = User.objects.get(pk=user_id)
         friendship = Friendship.objects.get(request_from=user, request_to=request.user, is_accepted=False)
      except (User.DoesNotExist, Friendship.DoesNotExist):
         return Response(status=status.HTTP_400_BAD_REQUEST)

      friendship.is_accepted = True
      friendship.save()
      return Response({'detail': 'Friendship accepted😀'})

class FriendListView(APIView):
   permission_classes = [IsAuthenticated]

   def get(self, request):
      frienship = Friendship.objects.filter(
         Q(request_to=request.user) |
         Q(request_from=request.user),
         is_accepted=True)
      users = [fr.request_from for fr in frienship]
      serializer = FriendshipSerializer(users, many=True)
      return Response(serializer.data)