from django.http import HttpResponse,JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from budget import models
import json
import datetime



def budgetlist(request):
    search_msg = request.GET
    search_dict = dict()
    if search_msg.get('line'):
         search_dict['line'] = search_msg.get('line')
    if search_msg.get('itemname'):
         search_dict['itemname'] = search_msg.get('itemname')
    if search_msg.get('operator'):
         search_dict['operator'] = search_msg.get('operator')
    if search_msg.get('room'):
         search_dict['room'] = search_msg.get('room')
    if search_msg.get('planpaytime'):
         search_dict['planpaytime'] = search_msg.get('planpaytime')
    budgetlist = list(models.BudgetPaymentlist.objects.filter(**search_dict).values())
    # budgetlist = json.dumps(budgetlist, cls=DjangoJSONEncoder)
    if budgetlist:
        return_list = {
            'code': 0,
            'status': 1,
            'msg': 'OK',
            'count': 200,
            'data': budgetlist
        }
        print(return_list)
        response = JsonResponse(return_list, content_type='application/json')
        response["Access-Control-Allow-Origin"] = "*"
        return response


# class CJSONEncoder(self,o):
#     if isinstance(o,datetime.datetime):
#         return o.strftime("%Y-%m-%d %H-%M-%S")
#     if isinstance(o,datetime.date):
#         return o.strftime("%Y-%m-%d")
#     else:
#         reture json.JSONEncoder.default(self,o)