# Generated by Django 3.0.6 on 2020-05-15 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('meta_keywords', models.CharField(max_length=255)),
                ('meta_description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'category',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('brand', models.CharField(max_length=255)),
                ('sku', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9)),
                ('image', models.ImageField(upload_to='')),
                ('is_active', models.BooleanField(default=True)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('amount', models.IntegerField()),
                ('description', models.TextField()),
                ('meta_keywords', models.CharField(max_length=255)),
                ('meta_description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='dtlcatalog.Category')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'db_table': 'product',
                'ordering': ['-created_at'],
            },
        ),
    ]
