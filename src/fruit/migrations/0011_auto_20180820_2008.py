# Generated by Django 2.0.8 on 2018-08-20 18:08

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import fruit.models.image
import fruit.models.kind
import utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fruit', '0010_auto_20170913_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', utils.fields.AutoDateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('image', utils.fields.ContentTypeRestrictedImageField(upload_to=fruit.models.image.Image._upload_to, verbose_name='image')),
                ('caption', models.CharField(blank=True, max_length=280, verbose_name='caption')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images_tmp', to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'ordering': ('-created',),
            },
        ),
        migrations.RemoveField(
            model_name='fruit',
            name='cover_image',
        ),
        migrations.AlterField(
            model_name='kind',
            name='key',
            field=models.CharField(default=fruit.models.kind._get_random_key, help_text='ID for API and also index in the markers font', max_length=4, unique=True, verbose_name='key'),
        ),
        migrations.AddField(
            model_name='image',
            name='fruit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='fruit.Fruit'),
        ),
    ]
