from django.contrib import admin
from .models import *
from .forms import *

admin.site.register(Member, MemberAdminForm)
admin.site.register(Team, TeamAdminForm)
admin.site.register(TeamMember, TeamMemberAdminForm)
admin.site.register(TeamRole)
