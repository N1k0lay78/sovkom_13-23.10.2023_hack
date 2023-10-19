from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import PasswordField, StringField, SubmitField, FileField, SelectField, RadioField, DateTimeField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea

"""
class FormLogin(FlaskForm):
    email = StringField("Почта", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()])
    submit = SubmitField("Войти")


class FormUserRegistration(FlaskForm):
    name = StringField("Ваше имя", validators=[DataRequired()])
    email = StringField("Почта", validators=[DataRequired()])
    level = SelectField("Ваш уровень", choices=((1, "Не занимался"),
                                                (2, "Занимаюсь пару месяцев"),
                                                (3, "Занимаюсь год"),
                                                (4, "Занимаюсь больше года")))
    password_1 = PasswordField("Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()])
    password_2 = PasswordField("Повторите Пароль",
                               validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()])
    submit = SubmitField("Зарегистрироваться")


class FormCompanyRegistration(FlaskForm):
    name = StringField("Название компании", validators=[DataRequired()])
    email = StringField("Почта", validators=[DataRequired()])
    rates = FloatField("Множитель цены", validators=[DataRequired()])
    logo = FileField("Логотип компании", validators=[FileAllowed(['jpg', 'png'])])
    password_1 = PasswordField("Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()])
    password_2 = PasswordField("Повторите Пароль",
                               validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()])
    submit = SubmitField("Зарегистрироваться")
"""


class FormLogin(FlaskForm):
    email = StringField("Почта", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()])
    submit = SubmitField("Войти")


class FormTest(FlaskForm):
    text_input = StringField("text input")
    text_area = StringField("text area", widget=TextArea())
    select_field = SelectField("selection", choices=((1, "один"), (2, "два"), (3, "три"), (4, "четыре")))
    data_field = DateTimeLocalField("date", format='%m/%d/%y')

    radio_field = RadioField("radio input", choices=[(1, "Верхняя неделя"), (2, "Нижняя неделя"), (3, "Каждую неделю")])

    file_field = FileField("file input")
    image_field = FileField("image input")

    password = PasswordField("password")

    cancel = SubmitField("Отмена")
    submit = SubmitField("Войти")


class FormDelete(FlaskForm):
    submit = SubmitField("Удалить")
