from django.urls import path, include

from personal_task_manager.category.views import CategoryListView,DetailCategoryView, UpdateCategoryView, DeleteCategoryView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('<int:pk>/', include([
        path('', DetailCategoryView.as_view(), name='category-detail'),
        path('update/', UpdateCategoryView.as_view(), name='category-update'),
        path('delete/', DeleteCategoryView.as_view(), name='category-delete'),

    ]))
]