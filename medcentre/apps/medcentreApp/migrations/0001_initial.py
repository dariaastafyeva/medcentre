# Generated by Django 4.0.2 on 2022-02-24 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_title', models.CharField(max_length=200, verbose_name='название статьи')),
                ('art_text', models.TextField(verbose_name='содержимое статьи')),
                ('pub_date', models.DateTimeField(verbose_name='дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='автор коммента')),
                ('comment_text', models.CharField(max_length=200, verbose_name='текст коммента')),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medcentreApp.article')),
            ],
        ),
    ]