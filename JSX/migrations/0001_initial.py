# Generated by Django 4.2 on 2024-04-03 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_at', models.DateTimeField(auto_now_add=True)),
                ('accepted_at', models.DateTimeField()),
                ('completed_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('test_time', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('role', models.PositiveSmallIntegerField(choices=[(1, '학생'), (2, '선생')])),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user_photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=100)),
                ('difficulty', models.CharField(max_length=10)),
                ('question', models.FileField(upload_to='test_questions/')),
                ('answer', models.FileField(upload_to='test_answers/')),
                ('commentary', models.FileField(upload_to='test_commentaries/')),
                ('omr', models.FileField(upload_to='test_omrs/')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_status', models.BooleanField(default=True)),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.subject')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='JSX.user')),
            ],
        ),
        migrations.CreateModel(
            name='TalkroomArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('anything_photo1', models.ImageField(blank=True, null=True, upload_to='anything_photos/')),
                ('anything_photo2', models.ImageField(blank=True, null=True, upload_to='anything_photos/')),
                ('anything_photo3', models.ImageField(blank=True, null=True, upload_to='anything_photos/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.user')),
            ],
        ),
        migrations.CreateModel(
            name='TalkComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JSX.talkcomment')),
                ('talkroom_article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.talkroomarticle')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.user')),
            ],
        ),
        migrations.CreateModel(
            name='StudyroomArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question_photo1', models.ImageField(blank=True, null=True, upload_to='question_photos/')),
                ('question_photo2', models.ImageField(blank=True, null=True, upload_to='question_photos/')),
                ('question_photo3', models.ImageField(blank=True, null=True, upload_to='question_photos/')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.subject')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.user')),
            ],
        ),
        migrations.CreateModel(
            name='StudyComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JSX.studycomment')),
                ('studyroom_article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.studyroomarticle')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.user')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='JSX.user')),
            ],
        ),
        migrations.CreateModel(
            name='MyTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('score', models.PositiveSmallIntegerField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.student')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.test')),
            ],
        ),
        migrations.CreateModel(
            name='Manage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_time', models.DurationField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.user')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_num', models.PositiveSmallIntegerField()),
                ('content', models.TextField(max_length=500)),
                ('feedback_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.feedback')),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='my_test_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.mytest'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.teacher'),
        ),
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JSX.user')),
            ],
        ),
    ]
