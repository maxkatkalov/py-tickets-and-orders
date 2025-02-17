from __future__ import annotations
from typing import Optional

from django.contrib.auth import get_user_model

from db.models import User


def create_user(
    username: str,
    password: str,
    email: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
) -> User:
    user_to_create = get_user_model().objects.create_user(
        username=username,
        password=password,
    )

    if email:
        user_to_create.email = email

    if first_name:
        user_to_create.first_name = first_name

    if last_name:
        user_to_create.last_name = last_name

    user_to_create.save()

    return user_to_create


def get_user(user_id: int) -> User | str:
    try:
        return get_user_model().objects.get(id=user_id)
    except get_user_model().DoesNotExist:
        return f"User with id {user_id} doesn`t exist"


def update_user(
    user_id: int,
    username: Optional[str] = None,
    password: Optional[str] = None,
    email: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
) -> None:
    user_to_update = get_user(user_id=user_id)

    if username:
        user_to_update.username = username

    if password:
        user_to_update.set_password(password)

    if email:
        user_to_update.email = email

    if first_name:
        user_to_update.first_name = first_name

    if last_name:
        user_to_update.last_name = last_name

    user_to_update.save()
