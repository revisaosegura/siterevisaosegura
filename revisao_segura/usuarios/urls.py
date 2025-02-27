from django.urls import path
from django.contrib.auth import views as auth_views
from revisao_segura.usuarios.views import cadastro, login_view, dashboard, logout_view, perfil, editar_perfil, upload_documento, enviar_documento_cliente, excluir_documento  # 🔹 Correção da importação

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('perfil/', perfil, name='perfil'),
    path('editar-perfil/', editar_perfil, name='editar_perfil'),
    path('enviar_documento_cliente/', enviar_documento_cliente, name="enviar_documento_cliente"),
    path('upload_documento/', upload_documento, name="upload_documento"),  # ✅ Nova rota
    path('excluir_documento/<int:documento_id>/', excluir_documento, name='excluir_documento'),
    path('logout/', logout_view, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='usuarios/reset_password.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='usuarios/reset_password_sent.html'), name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='usuarios/reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='usuarios/reset_password_complete.html'), name='password_reset_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
]
