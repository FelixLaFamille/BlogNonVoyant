# Generated by Django 3.1.6 on 2022-11-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Titre')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateField(blank=True, null=True)),
                ('published', models.BooleanField(default=False, verbose_name='Publié')),
                ('content', models.TextField(blank=True, verbose_name='Contenu')),
            ],
            options={
                'verbose_name': 'Article',
                'ordering': ['-created_on'],
            },
        ),
    ]