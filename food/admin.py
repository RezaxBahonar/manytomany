from django.contrib import admin
from .models import Food,Vote,CustomUser,BusyTracking,UserVote,Menu,Comment,UserLikedComment

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.register(UserLikedComment)
# Register your models here.
admin.site.site_header = "مدیریت سلف دانشگاه جهرم"  # Change the site header
admin.site.site_title = "سلف دانشگاه جهرم"    # Change the browser tab title
admin.site.index_title = "به پنل مدیریت خوش آمدید"

# admin.site.register(Food)
admin.site.register(Vote)
# admin.site.register(CustomUser)
# admin.site.register(User)
# admin.site.register(BusyTracking)
admin.site.register(UserVote)
class CommentInline(admin.TabularInline):  # or admin.StackedInline
    model = Comment
    fields = ('comment_text', 'likes', 'dislikes','user')  # Include the like/dislike fields
    extra = 1  # This specifies how many extra forms you want to display




class UserAdmin(BaseUserAdmin):
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'last_login', 'date_joined', 'groups')
    list_display = ('username', 'is_boy', 'noLogin', 'last_login')
    list_editable=('is_boy',)
# Unregister the original User admin
# admin.site.unregister(CustomUser)

# Register the new User admin with the custom filter options
admin.site.register(CustomUser, UserAdmin)

#----------------------------------------------------------------------#

class BusyTrackingAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('date', 'is_day', 'for_boy', 'rate', 'noPeople', 'adminOp')
    list_editable=('is_day', 'for_boy', 'adminOp')
    
    # Fields to filter by in the admin panel
    list_filter = ('date', 'is_day', 'for_boy', 'rate', 'noPeople', 'adminOp')
    
    # Fields to include in the search functionality
    search_fields = ('date', 'rate', 'noPeople', 'adminOp')

# Register the BusyTracking model with the custom admin class
admin.site.register(BusyTracking, BusyTrackingAdmin)

#----------------------------------------------------------------------#

class FoodAdmin(admin.ModelAdmin):


    list_display=('date','foodname','food_type','awli_vote',)
    list_editable=('date','foodname','food_type')
    # list_filter=('date','foodname','food_type')
    list_display_links=('awli_vote',)
    inlines = [CommentInline]

    
admin.site.register(Food, FoodAdmin)
class FoodInline(admin.TabularInline):  # or admin.StackedInline
    model = Food
    extra = 1  # This specifies how many extra forms you want to display

class MenuAdmin(admin.ModelAdmin):
    list_display=('date',)
    inlines = [FoodInline]

admin.site.register(Menu, MenuAdmin)
#----------------------------------------------------------------------#


class CommentAdmin(admin.ModelAdmin):
    list_display = ('food', 'comment_text', 'likes', 'dislikes', 'created_at')
    list_editable = ('likes', 'dislikes') 

admin.site.register(Comment,CommentAdmin)



#----------------------------------------------------------------------#
# class BusyVoteAdmin(admin.ModelAdmin):
#     # Fields to display in the admin list view
#     list_display = ('user', 'busy_tracking', 'vote')
    
#     # Fields to filter by in the admin panel
#     list_filter = ('user', 'busy_tracking', 'vote')
    
#     # Fields to include in the search functionality
#     search_fields = ('user__username', 'busy_tracking__date', 'vote')

# # Register the UserVote model with the custom admin class
# admin.site.register(UserVote, BusyVoteAdmin)