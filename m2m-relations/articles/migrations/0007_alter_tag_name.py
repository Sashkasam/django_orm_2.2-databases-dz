# Generated by Django 4.1.7 on 2023-02-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_tag_options_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]