import flask_login
from flask import abort
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView


class SecuredHomeView(AdminIndexView):
    """
    Функция переопределяет настройки доступа стартовой страницы админки.
    """
    def is_accessible(self):
        if not flask_login.current_user.is_authenticated:
            abort(401)
        return flask_login.current_user.is_admin

    @expose('/')
    def index(self):
        return self.render('/admin/index.html')


class CustomModelView(ModelView):
    """
    Функция переопределяет настройки доступа для каждой страницы модели.
    А так же включает отображение primary key(id) и foreign key.
    """
    column_display_pk = True
    column_hide_backrefs = False

    def is_accessible(self):
        if not flask_login.current_user.is_authenticated:
            abort(401)
        return flask_login.current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        abort(403)
