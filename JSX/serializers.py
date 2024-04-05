from rest_framework import serializers
from .models import  User, Test, MyTest, Feedback, FeedbackContent, Subject, Teacher, Student, StudyroomArticle, TalkroomArticle, StudyComment, TalkComment, Manage, Alarm

class subjectserialiar(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'photo']

class ManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manage
        fields = ['subject_name']

class TolalTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manage
        fields = ['subject_time']

class commentserialiar(serializers.ModelSerializer):

    class ArticleUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['username']

    user_id = ArticleUserSerializer()
    class Meta:
        model = StudyComment
        fields = ['content', 'created_at','user_id']

class StudyroomArticleSerializer(serializers.ModelSerializer):
    user_id = UsernameSerializer()
    subject_id = subjectserialiar()
    studycomment_set = commentserialiar(many=True)
    class Meta:
        model = StudyroomArticle
        fields = '__all__'

class StudyroomsubjectnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyroomArticle
        fields = ['subject_id']


class testcompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTest
        fields = ['test_id']


class testfeedbackcompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['completed_at']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['my_test_id']

class TeachernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['user_id']


class feedbackContentsSerializer(serializers.ModelSerializer):
    # user_id = UsernameSerializer(read_only=True)
    # teacher_id = TeachernameSerializer()

    class FeedbackSerializer(serializers.ModelSerializer):
        class FeedbackTeacherSerializer(serializers.ModelSerializer):
            class FeedbackUserSerializer(serializers.ModelSerializer):
                class Meta:
                    model = User
                    fields = ['username']    

            user_id = FeedbackUserSerializer()
            class Meta:
                model = Teacher
                fields = ['user_id']
                
        teacher_id = FeedbackTeacherSerializer()
        class Meta:
            model = Feedback
            fields = ['teacher_id']
            
    feedback_id = FeedbackSerializer()
    class Meta:
        model = FeedbackContent
        fields = ['content', 'feedback_id']
        


class articlescommentsSerializer(serializers.ModelSerializer):

    user_id = UsernameSerializer(read_only=True)
    class Meta:
        model = StudyComment
        fields = ["content", "created_at", "user_id"]
        # extra_kwargs = {"user_id": {"read_only": True}}
        # read_only_fields  = ('user_id',)


class subjecttimerserialiar(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['test_time']

class alarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm
        fields = ['title']

class testSerializer(serializers.ModelSerializer):
    subject_id = subjectserialiar()
    class Meta:
        model = Test
        fields = ['info','question','answer','commentary', 'subject_id']

