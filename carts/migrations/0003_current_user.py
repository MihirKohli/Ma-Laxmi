# Generated by Django 3.1 on 2022-03-02 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20220215_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Current_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_user_model', models.CharField(max_length=100)),
            ],
        ),
    ]