# Generated by Django 4.1 on 2022-12-05 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_identification_mcq_tf_trueorfalse_delete_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_title', models.CharField(max_length=2555)),
                ('identification_questions', models.ManyToManyField(to='quiz.identification')),
                ('mcq_questions', models.ManyToManyField(to='quiz.mcq')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.modules')),
                ('tof_questions', models.ManyToManyField(to='quiz.trueorfalse')),
            ],
        ),
    ]
