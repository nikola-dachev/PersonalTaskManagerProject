from django.urls import path, include

from personal_task_manager.tasks.views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, \
    TaskDeleteView, TaskUpdateCompleteView, TaskListOverDueView, TaskListCompletedView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>', include([
        path('', TaskDetailView.as_view(), name='task_detail'),
        path('update/', TaskUpdateView.as_view(), name='task_update'),
        path('delete/', TaskDeleteView.as_view(), name='task_delete'),
        path('complete/', TaskUpdateCompleteView.as_view(), name='task_complete'),
    ])),
    path('overdue/', TaskListOverDueView.as_view(), name='task_overdue'),
    path('completed/', TaskListCompletedView.as_view(), name='task_completed'),
]