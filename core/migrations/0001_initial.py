# Generated by Django 3.2.4 on 2021-06-15 18:15

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data da Modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo ?')),
                ('nome', models.CharField(max_length=100, verbose_name='Produto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Preço')),
                ('estoque', models.IntegerField(verbose_name='Estoque')),
                ('imagem', stdimage.models.StdImageField(upload_to='produtos', verbose_name='Imagem')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
