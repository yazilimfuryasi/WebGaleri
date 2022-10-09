# Generated by Django 4.0.3 on 2022-10-08 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galeri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sehir', models.CharField(max_length=45, verbose_name='Yer')),
                ('resim', models.ImageField(upload_to='uploads', verbose_name='Resim')),
                ('aciklama', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('kategori', models.CharField(choices=[(0, 'Yer'), (1, 'Gök'), (2, 'Derya')], max_length=25)),
            ],
        ),
    ]
