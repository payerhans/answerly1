from django.urls.conf import path
from quanda import views

app_name = 'quanda'
url_patterns = [
    #path('ask/', views.AskQuestionView.as_view(), name='ask'),
    path('ask', views.AskQuestionView.as_view(), name='ask'),
]