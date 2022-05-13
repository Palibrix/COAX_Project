# Generated by Django 4.0.4 on 2022-05-12 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0002_alter_departments_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depaments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='DANA')),
                ('phone', models.CharField(blank=True, max_length=25, verbose_name='Contact Phone')),
                ('web', models.URLField(blank=True, verbose_name='Website Address')),
            ],
        ),
        migrations.AddField(
            model_name='hospitals',
            name='departament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospitals.depaments'),
        ),
    ]
