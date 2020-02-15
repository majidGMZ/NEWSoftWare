from django.db import models
from django.contrib.auth.models import User,BaseUserManager,AbstractBaseUser

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    availability = models.BooleanField(verbose_name='availability', default=True)
    wigu = models.TextField(verbose_name='wigu', default="")
    education = models.TextField(verbose_name='education', default="")
    language = models.TextField(verbose_name='language', default="")
    about = models.TextField(verbose_name='about', default="")
    interest = models.TextField(verbose_name='interest', default="")
    birthday = models.DateField(default=None,null=True)
    link = models.TextField(verbose_name='link', default="")
    is_verified = models.BooleanField(verbose_name='is_verified', default=False)

    civ = models.TextField(verbose_name='civ', default="")
    cil = models.TextField(verbose_name='cil', default="")
    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class Spaces(models.Model):
    user_id = models.IntegerField()
    address = models.TextField()
    price = models.IntegerField()


class SpaceRank(models.Model):
    space_id = models.IntegerField()
    user_id = models.IntegerField()
    rank = models.IntegerField(default=0)


class Comments(models.Model):
    space_id = models.IntegerField()
    comment = models.TextField('comment', default="")
    user_id = models.IntegerField()