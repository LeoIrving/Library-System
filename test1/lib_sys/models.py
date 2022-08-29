from django.db import models

# Create your models here.


#作者
class AuthorInfo(models.Model):
    aut_name = models.CharField(max_length=30)
    aut_gender = models.BooleanField(default=False)
    aut_age = models.IntegerField()
    aut_comment = models.CharField(max_length=100)

    def __str__(self):
        return self.aut_name

# 借书人
class BorrowerInfo(models.Model):
    bor_name = models.CharField(max_length=30)
    bor_gender = models.BooleanField(default=False)
    bor_age = models.IntegerField()
    bor_comment = models.CharField(max_length=100)

    def __str__(self):
        return self.bor_name

# 捐赠人   
class LenderInfo(models.Model):
    len_name = models.CharField(max_length=30)
    len_gender = models.BooleanField(default=False)
    len_age = models.IntegerField()
    len_comment = models.CharField(max_length=100)

    def __str__(self):
        return self.len_name

# 图书
class BookInfo(models.Model):
    btitle = models.CharField(max_length=30)
    bauthor = models.ForeignKey('AuthorInfo',on_delete=models.CASCADE)
    bpub_date = models.DateField()
    bpub_name = models.CharField(max_length=30)
    len_date = models.DateField()
    lender = models.ForeignKey('LenderInfo',on_delete=models.CASCADE)
    is_bor = models.BooleanField(default=False)
    bor_date = models.DateField()
    borrower = models.ForeignKey('BorrowerInfo',on_delete=models.CASCADE)

    def __str__(self):
        return self.btitle