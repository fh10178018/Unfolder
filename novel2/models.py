# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminUser(models.Model):
    num = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, blank=True, null=True)
    pic = models.CharField(max_length=255, blank=True, null=True)
    weibo = models.CharField(max_length=255, blank=True, null=True)
    signature = models.CharField(max_length=255)
    post = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'admin_user'


class AdminUserContent(models.Model):
    num1 = models.ForeignKey(AdminUser, models.DO_NOTHING, db_column='num1')
    contents_num = models.IntegerField(primary_key=True)
    contents = models.TextField()
    datatime = models.DateTimeField(blank=True, null=True)
    like_num = models.IntegerField(blank=True, null=True)
    pic = models.CharField(max_length=255, blank=True, null=True)
    empty = models.CharField(max_length=255, blank=True, null=True)
    editor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_user_content'


class AdminUserContentComments(models.Model):
    content_num1 = models.ForeignKey(AdminUserContent, models.DO_NOTHING, db_column='content_num1')
    comment_num = models.IntegerField(primary_key=True)
    comment = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    editor1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_user_content_comments'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class IndexContents(models.Model):
    num = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=18)
    subtitile = models.CharField(max_length=100)
    createtime = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    viewnum = models.IntegerField(blank=True, null=True)
    likenum = models.IntegerField(blank=True, null=True)
    firstimg = models.CharField(max_length=255)
    demo = models.IntegerField(blank=True, null=True)
    editor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_contents'


class ShopGoods(models.Model):
    shop_name1 = models.CharField(primary_key=True, max_length=40)
    code2 = models.IntegerField()
    goods = models.CharField(max_length=255)
    goods_pic = models.CharField(max_length=255)
    price = models.FloatField()
    introduction = models.TextField()
    goods_discount = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_goods'


class ShopTag(models.Model):
    code1 = models.AutoField(primary_key=True)
    tag1 = models.CharField(max_length=255)
    tag2 = models.CharField(max_length=255, blank=True, null=True)
    tag3 = models.CharField(max_length=255, blank=True, null=True)
    tag4 = models.CharField(max_length=255, blank=True, null=True)
    tag5 = models.CharField(max_length=255, blank=True, null=True)
    tag6 = models.CharField(max_length=255, blank=True, null=True)
    tag7 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_tag'


class ShopUser(models.Model):
    code = models.AutoField(primary_key=True)
    shop_name = models.ForeignKey(ShopGoods, models.DO_NOTHING, db_column='shop_name')
    location_long = models.CharField(max_length=255)
    location_la = models.CharField(max_length=255)
    business_scope = models.CharField(max_length=255)
    shop_keeper = models.CharField(max_length=10)
    contact = models.CharField(max_length=20)
    funded_date = models.DateTimeField()
    pic = models.CharField(max_length=255)
    openning_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shop_user'
        unique_together = (('code', 'shop_name'),)

class Webviews(models.Model):
    time = models.DateField(blank=True, null=True)
    adminview = models.IntegerField(blank=True, default=0)
    view = models.IntegerField(blank=True, default=0)
    num = models.AutoField(primary_key=True)
    merchantview = models.IntegerField(blank=True, default=0)
    demoview = models.IntegerField(blank=True, default=0)

    class Meta:
        managed = False
        db_table = 'webviews'