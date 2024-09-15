from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
    )
from .models import Food,Vote,BusyTracking,CustomUser,UserVote, Comment,UserLikedComment

from .serializers import (
    FoodSerializer,
    VoteSerializers,
    BusyTrackingSerializers,
    RegisterSerializer,
    UserVoteSerializers,
    CustomUserSerializers,
    CommentSerializer,
    LikeOrDislikeSerializer
    )




from rest_framework.response import Response
from rest_framework import status



from rest_framework.views import APIView
from rest_framework import permissions,status
from rest_framework.response import Response




class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)



class UserRatedListCreatedView(ListCreateAPIView):
    queryset=UserVote.objects.all()
    serializer_class=UserVoteSerializers



class FoodListCreateView(ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request  # Pass the request to the serializer context
        return context
    
class FoodRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset=Food.objects.all()
    serializer_class=FoodSerializer


class VoteCreateListView(ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializers

class BusyListCreateView(ListCreateAPIView):
    queryset=BusyTracking.objects.all()
    serializer_class=BusyTrackingSerializers
    def get_serializer_context(self):
        """Ensure the context includes the request."""
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class BusyRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset=BusyTracking.objects.all()
    serializer_class=BusyTrackingSerializers


class VoteUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializers






# from django.contrib.auth.models import User

class CustomUserUpdate(RetrieveUpdateAPIView):
    permission_classes=[permissions.IsAuthenticated,]

    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSerializers
    lookup_field='username'

class MyProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = CustomUser.objects.get(username=request.user)
        # print(user.email)
        return Response({
            'username':user.username,
            'password':user.password,
            'email':user.email,
            'is_staff':user.is_staff,
            'is_superuser':user.is_superuser,
            'is_active':user.is_active,
            'is_boy':user.is_boy,
            'noLogin':user.noLogin,
        })
    def post(self, request):
        user = CustomUser.objects.get(username=request.user)

        # Get the old and new passwords from the request
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        # Validate that the old password is correct
        if not user.check_password(old_password):
            return Response({'error': 'Old password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

        # Set the new password
        user.set_password(new_password)
        user.save()

        return Response({'success': 'Password changed successfully.'})




from django.utils import timezone
class TimeView(APIView):

    def get(self,req):
        current_time = timezone.localtime(timezone.now())
        return Response({'current_time': current_time.strftime('%Y-%m-%d %H:%M:%S')})


class CommentView(ListCreateAPIView):
    serializer_class=CommentSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        foodId = self.kwargs['foodId']
        return Comment.objects.filter(food=foodId)

class CommentUpdateView(RetrieveUpdateAPIView):
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()

class LikeOrDislikeView(ListCreateAPIView):
    serializer_class=LikeOrDislikeSerializer
    queryset=UserLikedComment.objects.all()