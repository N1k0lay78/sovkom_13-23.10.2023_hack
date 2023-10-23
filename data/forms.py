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


class FormDelete(FlaskForm):
    submit = SubmitField("Удалить")


class FormSendMessage(FlaskForm):
    academic = StringField("Преподаватель", validators=[DataRequired()], render_kw={"placeholder": "Введите преподавателя"})
    link = StringField("Ссылка", validators=[DataRequired()], render_kw={"placeholder": "Введите ссылку"})
    number = StringField("Телефон", validators=[DataRequired()], render_kw={"placeholder": "+7 (9**) *** ** **"})
    group = StringField("Группа", validators=[DataRequired()], render_kw={"placeholder": "Введите название"})
    surname = StringField("Отчество", validators=[DataRequired()], render_kw={"placeholder": "Введите отчество"})
    name = StringField("Имя", validators=[DataRequired()], render_kw={"placeholder": "Введите имя"})
    family = StringField("Фамилия", validators=[DataRequired()], render_kw={"placeholder": "Введите фамилию"})
    email = StringField("Почта", validators=[DataRequired()], render_kw={"placeholder": "Введите почту"})
    message = StringField("text area", widget=TextArea(), validators=[DataRequired()], render_kw={"placeholder": "Введите сообщение", "rows": "3"})
    password = PasswordField("Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()], render_kw={"placeholder": "Введите пароль"})
    data_field = DateTimeLocalField("date", format='%m/%d/%y')
    favoritedirection = SelectField("selection", choices=((1, "Программирование"), (2, "Математика"), (3, "Экономика"), (4, "Физика")))
    text_area = StringField("text area", widget=TextArea(), render_kw={"placeholder": "Введите текст", "rows": "3"})
    submit = SubmitField("Отправить")


class FormAbit(FlaskForm):
    email = StringField("Почта", validators=[DataRequired()], render_kw={"placeholder": "Введите почту"})
    password = PasswordField("Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()], render_kw={"placeholder": "Введите пароль"})
    repeat_password = PasswordField("Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()], render_kw={"placeholder": "Повторите пароль"})

    surname = StringField("Отчество", validators=[DataRequired()], render_kw={"placeholder": "Введите отчество"})
    name = StringField("Имя", validators=[DataRequired()], render_kw={"placeholder": "Введите имя"})
    family = StringField("Фамилия", validators=[DataRequired()], render_kw={"placeholder": "Введите фамилию"})
    birthday = DateTimeLocalField("Дата рождения", format='%m/%d/%y')

    phone = StringField("Телефон", validators=[DataRequired()], render_kw={"placeholder": "+7 (9**) *** ** **"})
    social = StringField("Ссылка на профиль в соц. сеть", validators=[DataRequired()], render_kw={"placeholder": "t.me/@rjkzavr"})

    direction = SelectField("Направление", choices=((1, "Программирование"), (2, "Математика"), (3, "Экономика"), (4, "Физика")))
    about = StringField("О себе", widget=TextArea(), render_kw={"placeholder": "Введите текст", "rows": "3"})

    job = StringField("Место работы", validators=[DataRequired()], render_kw={"placeholder": "Введите место работы"})
    time_job = StringField("Время работы", validators=[DataRequired()], render_kw={"placeholder": "Введите период работы"})

    achievements = StringField("Достижения", widget=TextArea(), render_kw={"placeholder": "Введите текст", "rows": "3"})
    motivation_message = StringField("Мотивационное письмо", widget=TextArea(), render_kw={"placeholder": "Введите текст", "rows": "3"})

    submit = SubmitField("Отправить")






class FormFile(FlaskForm):
    name = StringField("Название файла", validators=[DataRequired()], render_kw={"placeholder": "Введите название"})
    file = FileField("")
    submit = SubmitField("Сохранить")


class FormFileEdit(FlaskForm):
    name = StringField("Название файла", validators=[DataRequired()], render_kw={"placeholder": "Введите название"})
    href = StringField("Ссылка", render_kw={"placeholder": "Введите ссылку"})
    submit = SubmitField("Сохранить")


class FormLogin(FlaskForm):
    email = StringField("Почта", validators=[DataRequired()], render_kw={"placeholder": "Введите почту"})
    password = PasswordField("Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()], render_kw={"placeholder": "Введите пароль"})
    submit = SubmitField("Войти")


class FormTest(FlaskForm):
    text_input = StringField("text input", render_kw={"placeholder": "Введите почту"})
    text_area = StringField("text area", widget=TextArea(), render_kw={"placeholder": "Введите текст", "rows": "3"})
    select_field = SelectField("selection", choices=((1, "один"), (2, "два"), (3, "три"), (4, "четыре")))
    data_field = DateTimeLocalField("date", format='%m/%d/%y')
    favoritedirection = SelectField("selection", choices=((1, "Программирование"), (2, "Математика"), (3, "Экономика"), (4, "Физика")))
    radio_field = RadioField("radio input", choices=[(1, "Верхняя неделя"), (2, "Нижняя неделя"), (3, "Каждую неделю")])
    direction = SelectField("selection", choices=((1, "Программирование"), (2, "Математика"), (3, "Экономика"), (4, "Физика")))

    file_field = FileField("file input")
    image_field = FileField("image input")

    password = PasswordField("password", render_kw={"placeholder": "Введите пароль"})

    cancel = SubmitField("Отмена")
    submit = SubmitField("Войти")


class FormDelete(FlaskForm):
    submit = SubmitField("Удалить")

class FormEditInfo(FlaskForm):
    email = StringField("Почта", validators=[DataRequired()], render_kw={"placeholder": "Введите почту"})
    surname = StringField("Отчество", validators=[DataRequired()], render_kw={"placeholder": "Введите отчество"})
    name = StringField("Имя", validators=[DataRequired()], render_kw={"placeholder": "Введите имя"})
    family = StringField("Фамилия", validators=[DataRequired()], render_kw={"placeholder": "Введите фамилию"})
    submit = SubmitField("Отправить")

class FormEditPassword(FlaskForm):
    current_password = PasswordField("Текущий пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()], render_kw={"placeholder": "Введите пароль"})
    password = PasswordField("Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()], render_kw={"placeholder": "Введите пароль"})
    repeat_password = PasswordField("Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()], render_kw={"placeholder": "Повторите пароль"})
    submit = SubmitField("Изменить пароль")