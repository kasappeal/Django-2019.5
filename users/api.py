from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView


class UsersAPI(APIView):

    def get(self, request):
        users = User.objects.all()
        user_list = []
        for user in users:
            user_list.append({
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name
            })
        return Response(user_list)
