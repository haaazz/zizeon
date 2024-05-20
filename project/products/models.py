from django.db import models
from django.conf import settings

# Create your models here.
class Deposit(models.Model):
    dcls_month = models.TextField()  # 공시제출월
    fin_co_no = models.TextField()  # 금융회사코드
    kor_co_nm = models.TextField()  # 금융회사명
    fin_prdt_cd = models.TextField(unique=True)  # 금융상품코드
    fin_prdt_nm = models.TextField()  # 금융상품명
    join_member = models.TextField()  # 가입대상
    join_way = models.TextField()  # 가입방법
    join_deny = models.IntegerField()  # 가입제한 (1: 제한없음, 2: 서민전용, 3: 일부제한)
    etc_note = models.TextField()  # 기타설명
    spcl_cnd = models.TextField()  # 우대조건
    mtrt_int = models.TextField()  # 만기후이자율

class DepositOption(models.Model):
    deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()  # 금융상품코드
    intr_rate_type_nm = models.TextField()  # 저축금리유형명
    intr_rate = models.FloatField()  # 저축금리
    intr_rate2 = models.FloatField()  # 최고우대금리
    save_trm = models.TextField()  # 저축기간 (단위: 개월)

class Saving(models.Model):
    dcls_month = models.TextField()  # 공시제출월
    fin_co_no = models.TextField()  # 금융회사코드
    kor_co_nm = models.TextField()  # 금융회사명
    fin_prdt_cd = models.TextField(unique=True)  # 금융상품코드
    fin_prdt_nm = models.TextField()  # 금융상품명
    join_member = models.TextField()  # 가입대상
    join_way = models.TextField()  # 가입방법
    join_deny = models.IntegerField()  # 가입제한 (1: 제한없음, 2: 서민전용, 3: 일부제한)
    etc_note = models.TextField()  # 기타설명
    spcl_cnd = models.TextField()  # 우대조건
    mtrt_int = models.TextField()  # 만기후이자율

class SavingOption(models.Model):
    saving = models.ForeignKey(Saving, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()  # 금융상품코드
    intr_rate_type_nm = models.TextField()  # 저축금리유형명
    rsrv_type_nm = models.TextField()  # 적립유형명
    intr_rate = models.FloatField()  # 저축금리
    intr_rate2 = models.FloatField()  # 최고우대금리
    save_trm = models.IntegerField()  # 저축기간 (단위: 개월)