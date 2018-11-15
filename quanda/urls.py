from django.urls.conf import path
from . import views

app_name = 'quanda'
urlpatterns = [
    path('ask', views.AskQuestionView.as_view(), name='ask'),
    #path('ask/', views.AskQuestionView.as_view()),
]