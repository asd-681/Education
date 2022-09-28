# Generated by Django 4.1 on 2022-08-30 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_emergencyservice_code_alter_incident_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencyservice',
            name='appeal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emergencyservices', to='core.person'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='incidents', to='core.person'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='service',
            field=models.ManyToManyField(null=True, related_name='incidents', to='core.emergencyservice'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, upload_to='project/media', verbose_name='Ваша фотография'),
        ),
    ]