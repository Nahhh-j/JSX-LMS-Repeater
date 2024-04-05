from django.urls import path

from JSX import views

urlpatterns = [
    # path("", views.data),
    # path("", views.article_list)
    path("testlist/", views.testlist),
    path("me/<int:user_id>/", views.me_detail),
    path("me/alarmsum/", views.me_alarmsum_list),
    path("me/alarm/title/", views.me_alarm_title),
    path("manage/subject-study-time/", views.manage_subject_study_time_time),
    path("manage/total-studytime/", views.manage_total_studytime),
    path("manage/subject/", views.manage_subject),
    path("articles/", views.article_list),
    path("articles/<int:article_id>/comments/", views.articles_comments),
    path("mytests/complete/", views.mytests_complete),
    path("feedback/complete/", views.feedback_complete),
    path("feedback/<int:feedback_id>/contents/", views.feedback_contents),
    path("articles/<int:article_id>/commentsum/", views.articles_comments_num),
    # path("testnamekorean/", views.testnamekorean_list),
    
    path("testpage/timer/", views.testpage_timer),
]