from django.contrib import admin

from about.models import About, Advisory_board, Founders, Our_campaigns, Our_initiatives, Senior_management_committee, Senior_technical_committee, Team
from about.views import Advisorapi

# Register your models here.
admin.site.register(About)
admin.site.register(Founders)
admin.site.register(Advisory_board)
admin.site.register(Senior_management_committee)
admin.site.register(Senior_technical_committee)
admin.site.register(Team)
admin.site.register(Our_initiatives)
admin.site.register(Our_campaigns)