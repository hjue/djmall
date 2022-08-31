# Generated by Django 3.2.4 on 2021-06-26 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('goods', '0002_auto_20210627_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('create_time', models.DateField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modify_time', models.DateField(auto_now=True, null=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, null=True, verbose_name='是否删除')),
                ('id_order', models.CharField(max_length=64, verbose_name='订单流水号')),
                ('name', models.CharField(max_length=120, verbose_name='商品名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品价格')),
                ('count', models.IntegerField(verbose_name='商品数量')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='订单总金额')),
                ('pay_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='实际支付总金额')),
                ('pic', models.CharField(max_length=256, verbose_name='商品图片')),
                ('id_goods', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderitem_goods', to='goods.goods', verbose_name='商品(Spu)ID')),
                ('id_sku', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderitem_sku', to='goods.sku', verbose_name='商品(Sku)ID')),
            ],
            options={
                'verbose_name': '订单商品管理',
                'verbose_name_plural': '订单商品管理',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('create_time', models.DateField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modify_time', models.DateField(auto_now=True, null=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, null=True, verbose_name='是否删除')),
                ('sn', models.CharField(max_length=64, unique=True, verbose_name='订单流水号')),
                ('total_count', models.IntegerField(verbose_name='订单总数量')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='订单总金额')),
                ('postage', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='邮费')),
                ('user_remark', models.TextField(blank=True, null=True, verbose_name='用户订单备注')),
                ('admin_remark', models.TextField(blank=True, null=True, verbose_name='商家订单备注')),
                ('order_status', models.IntegerField(choices=[(1, '待支付'), (2, '已付款'), (3, '待收货'), (4, '已收获'), (5, '退款申请中'), (6, '待退货'), (7, '待退款'), (8, '已退货'), (9, '已退款'), (10, '已完成'), (-1, '异常')], default=1, verbose_name='订单状态')),
                ('consignee_name', models.CharField(blank=True, max_length=10, null=True, verbose_name='收货人姓名')),
                ('consignee_phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='收货人手机号')),
                ('consignee_address', models.TextField(blank=True, null=True, verbose_name='收货人地址')),
                ('pay_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='实际支付总金额')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='支付成功时间')),
                ('pay_code', models.CharField(blank=True, max_length=32, null=True, verbose_name='支付流水号')),
                ('pay_type', models.IntegerField(blank=True, choices=[(0, ''), (1, '支付宝支付'), (2, '微信支付')], default=0, verbose_name='支付方式')),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='优惠总金额')),
                ('shipping_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='物流公司名称')),
                ('shipping_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='物流单号')),
                ('shipping_send_time', models.DateTimeField(blank=True, null=True, verbose_name='物流发货时间')),
                ('shipping_receive_time', models.DateTimeField(blank=True, null=True, verbose_name='物流收货时间')),
                ('consignee_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_user', to='user.user', verbose_name='收货人')),
                ('id_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderitem_user', to='user.user', verbose_name='用户')),
            ],
            options={
                'verbose_name': '订单管理',
                'verbose_name_plural': '订单管理',
            },
        ),
    ]
