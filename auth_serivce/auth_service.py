from functools import wraps
from flask import current_app, request, session
from web import db


def get_user():
    def _handler_decorator(f):
        @wraps(f)
        def __handler_decorator(*args, **kwargs):
            # s = session.open_session(current_app, request)
            # print(session.digest_method())
            # print(session.key_derivation)
            # print(session.salt)
            print(session.setdefault('hello', 'secret world'))

            result = f(*args, **kwargs)
            return result

        return __handler_decorator

    return _handler_decorator


def _determine_user_from_session():
    return None
