# Generated by Django 3.2.5 on 2021-08-25 00:42

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
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='지역명', max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='캠핑장명', max_length=150)),
                ('photo', models.ImageField(default='default.jpeg', help_text='대표이미지', upload_to='')),
                ('address', models.CharField(help_text='상세주소', max_length=150)),
                ('is_state', models.CharField(choices=[('OPEN', 'OPEN'), ('CLOSE', 'CLOSE')], help_text='캠핑장 상태', max_length=5)),
                ('note', models.TextField(help_text='비고', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='생성일시')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='수정일시')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('location', models.ForeignKey(help_text='지역 FK', on_delete=django.db.models.deletion.CASCADE, to='camp.location')),
                ('user', models.ForeignKey(help_text='작성자 FK', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(db_index=True, help_text='별칭', max_length=150)),
                ('gender', models.CharField(choices=[('남', '남'), ('여', '여')], help_text='성별', max_length=2)),
                ('user', models.OneToOneField(help_text='사용자 FK', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
