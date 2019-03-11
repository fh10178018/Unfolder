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


class Area(models.Model):
    area_num = models.IntegerField(primary_key=True)
    area_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'area'


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


class Categories(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_main_name = models.CharField(max_length=255)
    cat_detaill_name = models.CharField(db_column='cat_detaill-name', max_length=255)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'categories'


class Cities(models.Model):
    cityid = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    field_province = models.CharField(db_column='\r\nprovince', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_region = models.CharField(db_column='\r\nregion', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'


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


class ExtraTag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_main_name = models.CharField(max_length=255)
    tag_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'extra_tag'
        unique_together = (('tag_id', 'tag_name'),)


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


class MessagePic(models.Model):
    pic_id = models.AutoField(primary_key=True)
    shop_message = models.ForeignKey('ShopMessage', models.DO_NOTHING)
    pic = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'message_pic'


class Shop(models.Model):
    num = models.PositiveIntegerField(primary_key=True)
    shop_name = models.CharField(max_length=255)
    area = models.ForeignKey(Area, models.DO_NOTHING, db_column='area')
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    openningtime = models.CharField(max_length=255)
    point = models.CharField(max_length=255)
    permoney = models.CharField(max_length=255)
    pic = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop'

class ShopEnvironmentPic(models.Model):
    shop_num = models.IntegerField(primary_key=True)
    code3 = models.ForeignKey('Shops', models.DO_NOTHING, db_column='code3', blank=True, null=True)
    pic1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_environment_pic'

class ShopEnvironmentPicCopy(models.Model):
    shop_num = models.IntegerField(primary_key=True)
    code3 = models.ForeignKey('Shops', models.DO_NOTHING, db_column='code3', blank=True, null=True)
    pic1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_environment_pic_copy'

class ShopExtraTag(models.Model):
    tag_num = models.ForeignKey(ExtraTag, models.DO_NOTHING, db_column='tag_num')
    code1 = models.ForeignKey('Shops', models.DO_NOTHING, db_column='code1')

    class Meta:
        managed = False
        db_table = 'shop_extra_tag'

class ShopFood(models.Model):
    code = models.ForeignKey(Shop, models.DO_NOTHING, db_column='code')
    food_code = models.IntegerField(primary_key=True)
    food_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_food'


class ShopGoods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    code2 = models.ForeignKey('Shops', models.DO_NOTHING, db_column='code2')
    goods = models.CharField(max_length=255)
    goods_pic = models.CharField(max_length=255)
    price = models.FloatField()
    introduction = models.TextField(blank=True, null=True)
    goods_discount = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_goods'


class ShopMessage(models.Model):
    shop_message_num = models.AutoField(primary_key=True)
    shop_content_user = models.CharField(max_length=255)
    tag_libary = models.ForeignKey(ExtraTag, models.DO_NOTHING, db_column='tag_libary')
    content = models.CharField(max_length=255)
    prade = models.FloatField()
    creation_time = models.DateTimeField()
    code5 = models.ForeignKey('Shops', models.DO_NOTHING, db_column='code5')

    class Meta:
        managed = False
        db_table = 'shop_message'


class ShopOfficialPic(models.Model):
    shop_num = models.IntegerField(primary_key=True)
    code3 = models.ForeignKey('ShopUser', models.DO_NOTHING, db_column='code3', blank=True, null=True)
    pic1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_official_pic'


class ShopTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_num = models.ForeignKey(Categories, models.DO_NOTHING, db_column='tag_num')
    code1 = models.ForeignKey('Shops', models.DO_NOTHING, db_column='code1')

    class Meta:
        managed = False
        db_table = 'shop_tag'


class ShopUser(models.Model):
    code5 = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    pic = models.CharField(max_length=255)
    login_time = models.DateTimeField()
    register_time = models.DateTimeField()
    username = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_user'


class Shops(models.Model):
    shop_num = models.IntegerField(primary_key=True)
    code = models.ForeignKey(ShopUser, models.DO_NOTHING, db_column='code')
    shop_name = models.CharField(max_length=40)
    area = models.ForeignKey(Area, models.DO_NOTHING, db_column='area')
    shop_detail_address = models.CharField(max_length=255)
    shop_tel = models.CharField(max_length=40)
    shop_opening_hours = models.CharField(max_length=255, blank=True, null=True)
    shop_grade = models.FloatField()
    shop_average_price = models.FloatField(blank=True, null=True)
    city = models.ForeignKey(Cities, models.DO_NOTHING, db_column='city')
    pic = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shops'

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

class Film(models.Model):
    film_id = models.IntegerField(primary_key=True)
    film_name = models.CharField(max_length=255)
    film_pic = models.CharField(max_length=255, blank=True, null=True)
    film_enname = models.CharField(max_length=255, blank=True, null=True)
    film_grade = models.CharField(max_length=255, blank=True, null=True)
    film_state = models.CharField(max_length=255, blank=True, null=True)
    film_time = models.IntegerField(blank=True, null=True)
    film_showtime = models.DateTimeField(blank=True, null=True)
    film_like = models.IntegerField(blank=True, null=True)
    film_cats = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film'


class FilmGoods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    code6 = models.ForeignKey('Shops', models.DO_NOTHING, db_column='code6')
    film_code = models.ForeignKey(Film, models.DO_NOTHING, db_column='film_code')
    film_language = models.CharField(max_length=255, blank=True, null=True)
    film_time = models.DateTimeField(blank=True, null=True)
    film_prade = models.IntegerField(blank=True, null=True)
    film_num_office = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_goods'