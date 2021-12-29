# Generated by Django 4.0 on 2021-12-29 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_project_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlight', models.JSONField()),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.news')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
            ],
        ),
    ]
