from django.conf.urls import include, url, patterns
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from board.urls import router
import acescrum.common

urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
    url(r'^$', TemplateView.as_view(template_name='board/index.html')),
]

urlpatterns += patterns('',
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': acescrum.common.STATIC_ROOT}),
                        )
