from django.conf.urls import patterns, include, url
from django.contrib import admin

'''
start of the rest_framework imports and code
'''
from django.contrib.auth.models import User
from rest_framework import routers,serializers,viewsets
#serializers define the api representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=User 
		fields=('url','username','email','is_staff')

#ViewSets define the view behaviour
class UserViewSet(viewsets.ModelViewSet):
	queryset=User.objects.all()
	serializer_class=UserSerializer

#Routers provide an easy way of automatically determining the URL conf.
router=routers.DefaultRouter()
router.register(r'users',UserViewSet)

#wire up our API using automatic URL routing
#additionally,we include login URLS for the browsable API




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skeleton.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
