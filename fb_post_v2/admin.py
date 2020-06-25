# your django admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from fb_post_v2.models import User
from fb_post_v2.models import Post
from fb_post_v2.models import Comment
from fb_post_v2.models import Reaction


class UserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name','profile_pic')}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reaction)