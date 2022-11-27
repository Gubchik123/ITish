import flask

from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash


class _AdminMixin:
    def is_accessible(self):
        return bool(flask.session.get("admin_logged", None))

    def inaccessible_callback(self, name, **kwargs):
        return flask.redirect(flask.url_for("auth.log_in_admin"))


class _BaseModelViewWithURL(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_correct_url()
        return super(_BaseModelViewWithURL, self).on_model_change(
            form, model, is_created
        )


class HomeAdminView(_AdminMixin, AdminIndexView):
    pass


class UserAdminView(_AdminMixin, ModelView):
    form_columns = ["username", "email", "password"]

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)
        return super(UserAdminView, self).on_model_change(form, model, is_created)


class PostAdminView(_AdminMixin, _BaseModelViewWithURL):
    form_columns = ["title", "body", "user_id", "tags"]


class TagAdminView(_AdminMixin, _BaseModelViewWithURL):
    form_columns = ["title"]


class CommentAdminView(_AdminMixin, ModelView):
    form_columns = ["body", "post_id", "user_id"]


class LikeAdminView(_AdminMixin, ModelView):
    form_columns = ["post_id", "user_id"]
