# Generated by Django 4.1 on 2022-08-30 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_emergencyservice_appeal_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emergencyservice',
            options={'ordering': ('code',), 'verbose_name': 'Экстренные службы'},
        ),
        migrations.AlterModelOptions(
            name='incident',
            options={'ordering': ('data', 'number'), 'verbose_name': 'Обращения'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('surname', 'name', 'patronymic'), 'verbose_name': 'Заявитель'},
        ),
    ]