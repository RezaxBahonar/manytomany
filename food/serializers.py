from rest_framework import serializers
from .models import Food, Vote,BusyTracking,CustomUser,UserVote,Comment,UserLikedComment



# from rest_framework import serializers
# from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'


class RegisterSerializer(serializers.ModelSerializer):

    # email = serializers.EmailField(
    #     required=False,
    #     validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    # )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name','is_boy')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email', '') ,
            is_boy=validated_data.get('is_boy',False),
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


# User Rated?
class UserVoteSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserVote
        fields='__all__'

class BusyTrackingSerializers(serializers.ModelSerializer):
    user_rated = serializers.SerializerMethodField()

    class Meta:
        model = BusyTracking
        fields = '__all__'

    def get_user_rated(self, obj):
        """Check if the currently authenticated user has voted on this BusyTracking instance."""
        user = self.context.get('request').user
        if user.is_authenticated:
            return obj.votes.filter(user=user).exists()
        return False

class FoodSerializer(serializers.ModelSerializer):
    has_voted = serializers.SerializerMethodField()

    class Meta:
        model = Food
        # fields = ['id', 'date', 'foodname', 'awli_vote', 'khob_vote', 'bad_vote', 'eftezah_vote', 'has_voted']
        fields = '__all__'

    def get_has_voted(self, obj):
        """Check if the user has already voted on this food item."""
        user = self.context.get('request').user
        # print("User is : ",user.noLogin)
        # print("obg : ",obj.votes.filter(user='saman'))
        if user.is_authenticated:
            return obj.votes.filter(user=user).exists()
        return False

class VoteSerializers(serializers.ModelSerializer):
    class Meta:
        model=Vote
        fields='__all__'


class CommentSerializer(serializers.ModelSerializer):
    has_voted = serializers.SerializerMethodField()
    class Meta:
        model=Comment
        fields='__all__'
    def get_has_voted(self, obj):
        """Check if the user has already voted on this food item."""
        user = self.context.get('request').user
        # print("User is : ",user.noLogin)
        # print("obg : ",obj.votes.filter(user='saman'))
        if user.is_authenticated:
            return obj.comment_votes.filter(user=user).exists()
        return False
    
class LikeOrDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserLikedComment
        fields='__all__'