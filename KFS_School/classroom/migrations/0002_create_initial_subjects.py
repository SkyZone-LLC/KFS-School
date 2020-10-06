# Generated by Django 2.0.1 on 2018-01-18 18:07

from django.db import migrations


def create_subjects(apps, schema_editor):
    Subject = apps.get_model('classroom', 'Subject')
    Subject.objects.create(name='Coding', color='#ffc107')
    Subject.objects.create(name='Mindfulness', color='#ffc107')
    Subject.objects.create(name='Breathing', color='#ffc107')
    Subject.objects.create(name='Yoga Poses', color='#ffc107')





class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_subjects),
    ]
