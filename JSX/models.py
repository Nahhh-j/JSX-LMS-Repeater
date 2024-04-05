from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed password
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.PositiveSmallIntegerField(choices=[(1, '학생'), (2, '선생')])
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)

class Subject(models.Model):
    name = models.CharField(max_length=10)
    test_time = models.DurationField()  # Minutes

class Teacher(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    activity_status = models.BooleanField(default=True)

class Student(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

class Test(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    info = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10)
    question = models.FileField(upload_to='test_questions/')
    answer = models.FileField(upload_to='test_answers/')
    commentary = models.FileField(upload_to='test_commentaries/')
    omr = models.FileField(upload_to='test_omrs/')

class MyTest(models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    score = models.PositiveSmallIntegerField()

class Feedback(models.Model):
    my_test_id = models.ForeignKey(MyTest, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    required_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField()
    completed_at = models.DateTimeField()

class FeedbackContent(models.Model):
    feedback_id = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    page_num = models.PositiveSmallIntegerField()
    content = models.TextField(max_length=500)

class StudyroomArticle(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    question_photo1 = models.ImageField(upload_to='question_photos/', null=True, blank=True)
    question_photo2 = models.ImageField(upload_to='question_photos/', null=True, blank=True)
    question_photo3 = models.ImageField(upload_to='question_photos/', null=True, blank=True)

class TalkroomArticle(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    anything_photo1 = models.ImageField(upload_to='anything_photos/', null=True, blank=True)
    anything_photo2 = models.ImageField(upload_to='anything_photos/', null=True, blank=True)
    anything_photo3 = models.ImageField(upload_to='anything_photos/', null=True, blank=True)

class StudyComment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    studyroom_article_id = models.ForeignKey(StudyroomArticle, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

class TalkComment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    talkroom_article_id = models.ForeignKey(TalkroomArticle, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

class Manage(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    subject_time = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)

class Alarm(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)