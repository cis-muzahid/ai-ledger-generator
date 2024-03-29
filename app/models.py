from django.db import models

class ubereatsDailyEntry(models.Model):
    hash_id = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    accounts_receivable = models.FloatField()
    revenue = models.FloatField()
    revenue_marketing_adjustment = models.FloatField()
    discounts_and_comps = models.FloatField()
    commission = models.FloatField()
    promotions_on_items = models.FloatField()
    sales_tax = models.FloatField()
    tax_on_refunds = models.FloatField()
    tax_on_promotions = models.FloatField()
    debit = models.FloatField()
    credit = models.FloatField()
    discrepancy = models.FloatField()
    total_revenue = models.FloatField()
    ad_marketing = models.FloatField()
    total_ad_and_marketing = models.FloatField()
    total_tax_sales = models.FloatField()
    total_discrepancy = models.FloatField()

    class Meta:
        db_table = 'ubereats_daily_entry'

class ubereatsWeeklyEntry(models.Model):
    hash_id = models.CharField(max_length=255)
    week = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    accounts_receivable = models.FloatField()
    revenue = models.FloatField()
    revenue_marketing_adj = models.FloatField()
    discounts_comps = models.FloatField()
    ad_marketing = models.FloatField()
    commission = models.FloatField()
    promotions_on_items = models.FloatField()
    sales_tax = models.FloatField()
    tax_on_refunds = models.FloatField()
    tax_on_promotions = models.FloatField()
    debit = models.FloatField()
    credit = models.FloatField()
    discrepancy = models.FloatField()
    total_revenue = models.FloatField()
    total_ad_marketing = models.FloatField()
    total_sales_tax = models.FloatField()
    total_discrepancy = models.FloatField()
    location = models.CharField(max_length=255)

    class Meta:
        db_table = 'ubereats_weekly_entry'


class UbereatsDailyJE(models.Model):
    hash_id = models.CharField(max_length=255)
    date = models.DateField()
    name_match = models.CharField(max_length=255)
    locations = models.CharField(max_length=255)
    account = models.CharField(max_length=255)
    debit = models.FloatField()
    credit = models.FloatField()
    debit_balance = models.FloatField()
    credit_balance = models.FloatField()
    discrepancy = models.FloatField()

    class Meta:
        db_table = 'ubereats_daily_je'
