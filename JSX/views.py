from django.shortcuts import render, get_object_or_404
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import User, Test, MyTest, Feedback, FeedbackContent, Subject, Teacher, Student, StudyroomArticle, TalkroomArticle, StudyComment, TalkComment, Manage, Alarm
# @api_view(["GET"])
# def username_list(request):
#     # user = request.user
#     # articles = user.article_set.all()
#     users = User.objects.all()
#     serializer = UsernameSerializer(users, many=True)
#     return Response(serializer.data, status=200)

# username/ 특정 유저 불러오기
@api_view(["GET"])
def me_detail(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UsernameSerializer(user)
    return Response(serializer.data, status=200)

# alarmsum/ 특정 유저 알람 총 갯수 조회
@api_view(["GET"])
def me_alarmsum_list(request):
    # user = request.user 로그인한 유저라는 뜻.
    user = User.objects.get(id=2)   # 우리의 유저는 무조건 1번사람 고정.
    alarms = user.alarm_set.all() # 유저에 대한 전체 알람.
    alarm_len = len(alarms)
    return Response({'alarm_len' : alarm_len})

# 내 알람 제목 조회
@api_view(["GET"])
def me_alarm_title(request):
    user = User.objects.get(id=2)
    alarm = user.alarm_set.all() # 유저에 대한 전체 알람.
    serializer = alarmSerializer(alarm, many=True)
    return Response(serializer.data, status=200)

# 모의고사 리스트 조회
@api_view(["GET"])
def testlist(request):
    test = Test.objects.all() #테스트 전체 내용 조회
    serializer = testSerializer(test, many=True) 
    return Response(serializer.data, status=200)


# subjectstudytime/ 1번 유저의 특정과목과 해당과목의 공부시간을 조회하는 함수(과목별 공부시간)
@api_view(["GET"])
def manage_subject_study_time_time(request):
    user = User.objects.get(id=1)   # 우리의 유저는 무조건 1번사람.
    manages = user.manage_set.all() # 유저에 대한 매니지 정보 전부조회
    serializer = ManageSerializer(manages)
    return Response(serializer.data, status=200)

from datetime import datetime, timedelta
from django.db.models import Sum
# # totalstudytime/ 1번 유저의 일별 총 공부시간을 조회하는 함수-------------------
@api_view(["GET"])
def manage_total_studytime(request):
    user = User.objects.get(id=1)   # 우리의 유저는 무조건 1번사람.
    manages = user.manage_set.all() # 유저에 대한 매니지 정보 전부조회
    microseconds=manages.aggregate(sum=Sum('subject_time'))['sum']
    
    serializer = TolalTimeSerializer(manages, many=True)
    # total_studytime = sum(serializer.subject_time)
    # total_studytime = sum(serializer)
    
    # return Response()
    return Response({'total_studytime' : str(microseconds)})
    # return Response({'total_studytime' : total_studytime})

# subjectadd/ URL에 대한 간단한 응답을 반환하는 뷰 함수
@api_view(["POST"])
def manage_subject(request):
    user = User.objects.get(id=1) # 사실은request.user, 즉 요청보낸 사람.
    data = request.data
    serializer = ManageSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user_id=user)
        return Response(serializer.data, status=201)
    
#article_list / 전체 게시글 조회
@api_view(["GET"])
def article_list(request):
    studyroomArticle = StudyroomArticle.objects.all()   # 우리의 게시글 번호는 무조건 1번
    serializer = StudyroomArticleSerializer(studyroomArticle, many=True)
    return Response(serializer.data, status=200)

# testcomplete / 모의고사에서 문제풀이 완료 숫자 변화, 지금은 모든 시험 조회임.
@api_view(["GET"])
def mytests_complete(request):
    mytests = MyTest.objects.all() # 내가 본 테스트의 전체
    # mytests = user.mytest_set.filter(status=1) # 내가 본 테스트 중 스테이터스가 1인 것들.
    # 즉, complete라는 것은 status로 구분이 되는데, 그걸 filtering해서 complete된것만 가져오기.
    serializer = testcompleteSerializer(mytests, many=True)
    return Response(serializer.data, status=200)

# testfeedbackcomplete / 모의고사에서 피드백 완료 개수, 지금은 모든 피드백 개수 조회임
@api_view(["GET"])
def feedback_complete(request):
    # user = User.objects.get(id=1) # 나로부터 시작
    user = Teacher.objects.get(id=1)
    myfeedback = user.feedback_set.all() #내가 받은 피드백 전체 
    serializer = testfeedbackcompleteSerializer(myfeedback, many=True)
    return Response(serializer.data, status=200)



# feedback_feedbackcontent / 문제지 내 피드백 내용
@api_view(["GET"])
def feedback_contents(request,feedback_id):
    # user = User.objects.get(id=9)   # 우리의 유저는 무조건 1번사람. 필요없음.
    feedback = Feedback.objects.get(id=feedback_id)
    feedbackContents = feedback.feedbackcontent_set.all() # 유저에 대한 매니지 정보 전부조회
    # feedbackContents = FeedbackContent.objects.get(pk=feedback_id)
    serializer = feedbackContentsSerializer(feedbackContents, many=True)
    return Response(serializer.data, status=200)

# (커뮤니티) 게시글 밑 댓글 작성
@api_view(["POST"])
def articles_comments(request,article_id):
    user = User.objects.get(id=1)
    article = StudyroomArticle.objects.get(pk=article_id)
    data = request.data
    serializer = articlescommentsSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(studyroom_article_id=article, user_id = user)
        return Response(serializer.data, status=201)
    

# testpagetimer / 테스트 타이머
@api_view(["GET"])
def testpage_timer(request):
    subjecttime = Subject.objects.all() #내가 받은 피드백 전체
    serializer = subjecttimerserialiar(subjecttime, many=True) # 시간값만 가져오기
    return Response(serializer.data, status=200)

#특정 게시글 댓글 총 갯수 
@api_view(["GET"])
def articles_comments_num(request,article_id):
    article = StudyroomArticle.objects.get(pk=article_id)
    comment = article.studycomment_set.all() 
    comment_len = len(comment)
    return Response({'comment_len' : comment_len})


# user = User.objects.get(id=2)   # 우리의 유저는 무조건 1번사람 고정.
#     alarms = user.alarm_set.all() # 유저에 대한 전체 알람.
#     alarm_len = len(alarms)
#     return Response({'alarm_len' : alarm_len})