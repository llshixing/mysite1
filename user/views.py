from django.http import HttpResponse,JsonResponse
from user import models
import json
import pymysql

def userLogin(request):
    login_msg = request.GET
    user = getUser(login_msg['username'])
    if user:
        if user.password == login_msg['password']:
            login_msg = {'code': 0, 'status':0, 'msg':'OK', 'data': login_msg}
            response = HttpResponse(json.dumps(login_msg), content_type='application/json')
            print(json.dumps(login_msg))
            response["Access-Control-Allow-Origin"] = "*"
            return response
        else:
            return HttpResponse('密码不正确')
    return HttpResponse('用户不存在')


def getUser(login_username):
    try:
        user = models.User.objects.get(userName=login_username)
    except:
        return ""
    return user
