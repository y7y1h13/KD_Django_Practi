from django.db import models

class User(models.Model):
    username = models.CharField(max_length=64, verbose_name='Username')
    useremail = models.EmailField(max_length=128, verbose_name='Useremail')
    password = models.CharField(max_length=64, verbose_name='Password')
    registered = models.DateTimeField(auto_now_add=True, verbose_name='AddDate')

    GENDERS = (
        ('M', '남성'),
        ('W', '여성'),
    )

    JOBS = (
        ('P', '교수/강사(Professor/Lecturer)'),
        ('S', '학생(Student)'),
        ('R', '연구원(Researcher)'),
        ('E', '기타(Etc.)')
    )

    gender = models.CharField(max_length=1, verbose_name='성별', choices=GENDERS)
    job = models.CharField(max_length=1, verbose_name='직업', choices=JOBS)

    def __self__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
