from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='regiane', email='regi@gmail.com', password='senha')
    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'regi@gmail.com')
    )  # retornando em formato de objeto python

    assert result.username == 'regiane'
