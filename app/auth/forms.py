import wtforms as wtf
from flask_wtf import FlaskForm
import wtforms.validators as validator

required = validator.InputRequired("The area must be filled!")


class RegistrationForm(FlaskForm):
    username = wtf.StringField(
        "Username",
        validators=[
            required,
            validator.Length(min=3, max=50),
            validator.Regexp(
                # (no _ or . at the beginning)[allowed allowed characters](no _ or . at the end)
                r"^(?![_.])[a-zA-Z0-9._]+(?<![_.])$",
                message="Wrong username (must be neither spaces nor _ or . at the beginning and at the end)!",
            ),
        ],
    )
    email = wtf.EmailField(
        "Email",
        validators=[
            required,
            validator.Email("Enter the correct email!"),
            validator.Length(min=10, max=255),
        ],
    )
    password = wtf.PasswordField(
        "Password", validators=[required, validator.Length(min=5)]
    )
    password_again = wtf.PasswordField(
        "Password again",
        validators=[
            required,
            validator.Length(min=5),
            validator.EqualTo("password", message="Passwords must match!"),
        ],
    )
    submit = wtf.SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = wtf.EmailField(
        "Email",
        validators=[
            required,
            validator.Email("Enter the correct email!"),
            validator.Length(min=10, max=255),
        ],
    )
    password = wtf.PasswordField(
        "Password", validators=[required, validator.Length(min=5)]
    )
    submit = wtf.SubmitField("Log In")


class LoginAdminForm(FlaskForm):
    password = wtf.PasswordField(
        "Admin password", validators=[required, validator.Length(min=5)]
    )
    submit = wtf.SubmitField("Log In")
