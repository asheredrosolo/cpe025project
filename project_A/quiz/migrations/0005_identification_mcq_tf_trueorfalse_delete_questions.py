# Generated by Django 4.1.2 on 2022-10-31 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_questions_option1_alter_questions_option2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='identification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.CharField(max_length=255)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.modules')),
            ],
        ),
        migrations.CreateModel(
            name='mcq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option1', models.CharField(blank=True, max_length=255)),
                ('option2', models.CharField(blank=True, max_length=255)),
                ('option3', models.CharField(blank=True, max_length=255)),
                ('option4', models.CharField(blank=True, max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.modules')),
            ],
        ),
        migrations.CreateModel(
            name='TF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='trueorfalse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.tf')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.modules')),
            ],
        ),
        migrations.DeleteModel(
            name='questions',
        ),
    ]
