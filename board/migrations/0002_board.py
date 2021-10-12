# Generated by Django 3.2.5 on 2021-08-25 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='free_hit',
            name='free',
            field=models.ForeignKey(help_text='자유게시판 FK', on_delete=django.db.models.deletion.CASCADE, related_name='children', to='board.free'),
        ),
        migrations.AlterField(
            model_name='notice_hit',
            name='notice',
            field=models.ForeignKey(help_text='공지사항 FK', on_delete=django.db.models.deletion.CASCADE, related_name='children', to='board.notice'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(help_text='대표이미지', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post_good',
            name='post',
            field=models.ForeignKey(help_text='후기 FK', on_delete=django.db.models.deletion.CASCADE, related_name='children_good', to='board.post'),
        ),
        migrations.AlterField(
            model_name='post_hit',
            name='post',
            field=models.ForeignKey(help_text='후기 FK', on_delete=django.db.models.deletion.CASCADE, related_name='children_hit', to='board.post'),
        ),
    ]
