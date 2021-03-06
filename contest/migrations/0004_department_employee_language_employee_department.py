# Generated by Django 4.0.4 on 2022-04-19 12:12

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0003_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('floor', models.PositiveIntegerField()),
            ],
            managers=[
                ('deparments', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='contest.programminglanguage'),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='contest.department'),
        ),
    ]
