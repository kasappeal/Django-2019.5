import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View


class UsersAPI(View):

    def get(self, request):
        users = User.objects.all()
        user_list = []
        for user in users:
            user_list.append({
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name
            })
        users_json = json.dumps(user_list)
        return HttpResponse(users_json, content_type='application/json')
