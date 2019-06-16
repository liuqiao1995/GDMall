# Generated by Django 2.0.6 on 2019-06-16 17:35

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('brand', models.CharField(blank=True, max_length=255, verbose_name='品牌')),
                ('color', models.CharField(blank=True, max_length=255, verbose_name='颜色')),
                ('code', models.CharField(blank=True, max_length=255, verbose_name='尺码')),
                ('art_no', models.CharField(blank=True, max_length=255, verbose_name='货号')),
                ('pattern', models.CharField(blank=True, max_length=255, verbose_name='版型')),
                ('collar', models.CharField(blank=True, max_length=255, verbose_name='领型')),
                ('season', models.CharField(blank=True, max_length=255, verbose_name='季节')),
                ('ttm', models.CharField(blank=True, max_length=255, verbose_name='上市时间')),
            ],
            options={
                'verbose_name': '产品属性',
                'verbose_name_plural': '产品属性',
                'db_table': 'gd_attribute',
            },
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=30, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'db_table': 'gd_classify',
            },
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('name', models.CharField(default='商品未命名', max_length=255, verbose_name='商品名称')),
                ('color', models.CharField(max_length=10, verbose_name='颜色')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('code', models.CharField(max_length=10, verbose_name='尺码')),
                ('image', models.ImageField(upload_to='CommdityImg', verbose_name='商品小图')),
                ('stock', models.IntegerField(default=0, verbose_name='库存')),
                ('selected', models.BooleanField(default=False, verbose_name='是否选中')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'gd_commodity',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('title', models.CharField(max_length=60, verbose_name='产品标题')),
                ('sales', models.IntegerField(default=0, verbose_name='销量')),
                ('hits', models.IntegerField(default=0, verbose_name='点击量')),
                ('featured', models.BooleanField(default=False, verbose_name='是否主推')),
                ('putaway', models.BooleanField(default=False, verbose_name='是否上架')),
                ('classify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Classify', verbose_name='所属分类id')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品',
                'db_table': 'gd_goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('show_region', models.SmallIntegerField(choices=[(0, '产品大图'), (1, '产品图文')], verbose_name='展示区域')),
                ('image', models.ImageField(blank=True, upload_to='GoodsImg', verbose_name='图片')),
                ('content', mdeditor.fields.MDTextField(verbose_name='内容')),
                ('index', models.SmallIntegerField(default=0, verbose_name='展示顺序')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='所属产品id')),
            ],
            options={
                'verbose_name': '产品图片',
                'verbose_name_plural': '产品图片',
                'db_table': 'gd_goods_image',
            },
        ),
        migrations.CreateModel(
            name='IndexCarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('image', models.ImageField(blank=True, upload_to='Banner', verbose_name='轮播图片')),
                ('index', models.SmallIntegerField(default=0, verbose_name='展示顺序')),
                ('url', models.CharField(max_length=256, verbose_name='跳转地址')),
            ],
            options={
                'verbose_name': '首页轮播图',
                'verbose_name_plural': '首页轮播图',
                'db_table': 'gd_index_banner',
            },
        ),
        migrations.CreateModel(
            name='IndexVideoOrBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('image', models.ImageField(blank=True, upload_to='Banner', verbose_name='图片')),
                ('video', models.FileField(blank=True, upload_to='Video', verbose_name='视频')),
                ('show_type', models.SmallIntegerField(choices=[(0, '图片'), (1, '视频')], default=0, verbose_name='展示类型')),
                ('url', models.CharField(blank=True, max_length=256, verbose_name='跳转地址')),
            ],
            options={
                'verbose_name': '首页视频或图片栏',
                'verbose_name_plural': '首页视频或图片栏',
                'db_table': 'gd_index_video_or_banner',
            },
        ),
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('name', models.CharField(max_length=30, verbose_name='类别名称')),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别',
                'db_table': 'gd_sort',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='sort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Sort', verbose_name='所属类别id'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='所属产品id'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='所属产品id'),
        ),
    ]
