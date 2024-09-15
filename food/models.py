from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_boy=models.BooleanField(default=False,blank=False)
    username = models.CharField(max_length=150, unique=True, primary_key=True)
    USERNAME_FIELD = 'username'
    noLogin=models.PositiveIntegerField(default=0)
    
class BusyTracking(models.Model):

    date=models.DateField(blank=False)
    is_day=models.BooleanField(default=True)
    for_boy=models.BooleanField(default=True)
    rate= models.DecimalField(max_digits=5, decimal_places=2,default=50.0)
    noPeople=models.PositiveIntegerField(default=1)

    adminOp=models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f'date: {self.date}| AdminOp: {self.adminOp} | Stu rate: {self.rate/self.noPeople} | number of pepole: {self.noPeople} |is day? : {self.is_day} | for boy? | {self.for_boy}'

# User Rated
class UserVote(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    busy_tracking = models.ForeignKey(BusyTracking, related_name='votes', on_delete=models.CASCADE)
    vote = models.FloatField(default=0.0)
    def __str__(self) -> str:
        dayOrnight='day' if self.busy_tracking.is_day else 'night'
        return f'{self.user.username} ---> vote({self.vote}) to ---> {self.busy_tracking.date} {dayOrnight}'
        # return str(self.vote)


class Menu(models.Model):
    date = models.DateField(primary_key=True)
    def __str__(self):
        return f'Date: {self.date}'

class Food(models.Model):

    FoodType_CHOICES = [
        ('sobhaneh', 'Sobhaneh'),
        ('nahar', 'Nahar'),
        ('sham', 'Sham'),
    ]
    food_type = models.CharField(max_length=16, choices=FoodType_CHOICES,blank=False)
    date = models.DateField(blank=False)
    foodname = models.CharField(max_length=128, blank=False)
    menu = models.ForeignKey(Menu, related_name='foods', on_delete=models.CASCADE)
    awli_vote = models.PositiveIntegerField(default=0)
    khob_vote = models.PositiveIntegerField(default=0)
    bad_vote = models.PositiveIntegerField(default=0)
    eftezah_vote = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'name : {self.foodname} |type: {self.food_type} |date : {self.date}'
    
    class Meta:
        unique_together = ('date', 'foodname')

class Comment(models.Model):
    food = models.ForeignKey(Food, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='comments', on_delete=models.CASCADE)  # Use CustomUser
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.comment_text} -> Comment by {self.user.username} on {self.food.foodname}'

class UserLikedComment(models.Model):
    VOTE_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'DisLike'),
    ]
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='comment_votes')
    vote_type = models.CharField(max_length=8, choices=VOTE_CHOICES)
    class Meta:
        unique_together=('user','comment')
    def __str__(self) -> str:
        return f'{self.user.username} vote on {self.comment.comment_text}'
    

class Vote(models.Model):
    VOTE_CHOICES = [
        ('awli', 'Awli'),
        ('khob', 'Khob'),
        ('bad', 'Bad'),
        ('eftezah', 'Eftezah'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='votes')
    vote_type = models.CharField(max_length=8, choices=VOTE_CHOICES)

    class Meta:
        unique_together = ('user', 'food')

    def __str__(self):
        return f"{self.user.username} ---voted---> {self.vote_type} ---on---> {self.food.foodname}"
