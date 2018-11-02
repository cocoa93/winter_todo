# Generated by Django 2.1.2 on 2018-10-30 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('UI', 'urgent&important'), ('NI', 'not urgent&important'), ('UN', 'urgent&not important'), ('NN', 'not urgent&not important')], default='NN', max_length=2),
        ),
    ]
