from flask_wtf import FlaskForm
from wtforms import PasswordField , StringField , SubmitField
from wtforms.validators import DataRequired , Email , length

#사용자 신규 작성 , 편집 폼 클래스
class UserForm(FlaskForm):
    username = StringField(
        "사용자명",
        validators=[
                DataRequired(message='사용자명은 필수입니다.'),
                length(max=30,message='30자 이내로 입력해주세요.')
        ]
    )

    email = StringField(
        '메일주소',
        validators=[
                DataRequired(message='메일주소는 필수입니다.'),
                Email(message='메일주소 형식으로 입력해주세요')
        ]
    )
    password = PasswordField(
        '비밀번호',
        validators=[
                DataRequired(message='비밀번호는 필수입니다')
        ]
    )

    submit = SubmitField('신규등록')