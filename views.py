from rest_framework import viewsets
from rest_framework.response import Response
from generators import OssPolicyAuth
from django.conf import settings


class PolicyAuthViewSet(viewsets.ViewSet):
    def create(self, request):
        access_key_id = settings.get('OSS_ACCESS_KEY')
        access_key_secret = settings.get('OSS_ACCESS_SECRET')
        timeout = settings.get('OSS_TIMOUT', 60)
        max_size = settings.get('OSS_MAXSIZE', 10)

        oss_policy_auth = OssPolicyAuth(access_key_id,
                                        access_key_secret,
                                        timeout,
                                        max_size)

        return Response(data=oss_policy_auth)
