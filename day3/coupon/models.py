from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)#유니크는 중복안되게해준다
    use_from = models.DateTimeField()#유효기간
    use_to = models.DateTimeField()
    amount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)])#쿠폰 금액 한계
    activate = models.BooleanField()



    def __str__(self):
        return self.code