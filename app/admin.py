import flask

from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash

from .models import User, Post, Tag
from .funcs import redirect_to_url_for_


class _AdminMixin:
    """Custom admin mixin"""

    def is_accessible(self) -> bool:
        return bool(flask.session.get("admin_logged", None))

    def inaccessible_callback(self, name: str, **kwargs) -> flask.Response:
        return redirect_to_url_for_("auth.log_in_admin")


class _BaseModelViewWithURL(ModelView):
    """Custom view for models with url"""

    def on_model_change(self, form, model: Post | Tag, is_created: bool):
        model.generate_correct_url()
        return super(_BaseModelViewWithURL, self).on_model_change(
            form, model, is_created
        )


class HomeAdminView(_AdminMixin, AdminIndexView):
    """Admin home view using custom admin mixin"""

    pass


class UserAdminView(_AdminMixin, ModelView):
    """Custom admin view for 'User' model"""

    form_columns = ["username", "email", "password"]

    def on_model_change(self, form, model: User, is_created: bool):
        model.password = generate_password_hash(model.password)
        return super(UserAdminView, self).on_model_change(form, model, is_created)


class PostAdminView(_AdminMixin, _BaseModelViewWithURL):
    """Admin view for 'Post' model using custom view for models with url"""

    form_columns = ["title", "body", "user_id", "tags"]


class TagAdminView(_AdminMixin, _BaseModelViewWithURL):
    """Admin view for 'Tag' model using custom view for models with url"""

    form_columns = ["title"]


class CommentAdminView(_AdminMixin, ModelView):
    """Admin view for 'Comment' model"""

    form_columns = ["body", "post_id", "user_id"]


class LikeAdminView(_AdminMixin, ModelView):
    """Admin view for 'Like' model"""

    form_columns = ["post_id", "user_id"]
