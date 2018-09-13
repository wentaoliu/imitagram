# Generated by Django 2.1.1 on 2018-09-13 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sink', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sink', to=settings.AUTH_USER_MODEL)),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
