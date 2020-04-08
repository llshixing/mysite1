from django.db import models

# 建设资金支付预算
class BudgetPaymentlist(models.Model):
    id = models.IntegerField(primary_key=True)
    line = models.CharField(max_length=11, blank=True, null=True)
    itemname = models.CharField(max_length=255, blank=True, null=True)
    period = models.CharField(max_length=255, blank=True, null=True)
    budgetamount = models.CharField(max_length=255, blank=True, null=True)
    planpaytime = models.DateTimeField(blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    room = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    actualpaytime = models.DateTimeField(blank=True, null=True)
    actualamount = models.CharField(max_length=255, blank=True, null=True)
    condition = models.CharField(max_length=1000, blank=True, null=True)
    ristrating = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_paymentlist'



