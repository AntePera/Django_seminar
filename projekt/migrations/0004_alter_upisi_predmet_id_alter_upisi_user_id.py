# Generated by Django 4.2.1 on 2023-06-09 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0003_alter_upisi_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upisi',
            name='predmet_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projekt.predmeti'),
        ),
        migrations.AlterField(
            model_name='upisi',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
