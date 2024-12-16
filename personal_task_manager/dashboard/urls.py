from django.urls import path

from personal_task_manager.dashboard.views import ListDashboardView,AnalyticsView, PreferencesView

urlpatterns= [
    path('', ListDashboardView.as_view(), name='dashboard'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
    path('preferences/', PreferencesView.as_view(), name='preferences'),

]