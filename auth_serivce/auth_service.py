from functools import wraps
from flask import current_app, request, session
from web import db


# Wrapper for requests that checks for a session cookie containing a user, and if so creates a User object
# with some basic data populated from the cookie.  Request handlers can use the user for further authorization
# if needed.
@app.before_request()
def get_user():
    def _handler_decorator(f):
        @wraps(f)
        def __handler_decorator(*args, **kwargs):
            session.get('user')


            result = f(*args, **kwargs)
            return result

        return __handler_decorator

    return _handler_decorator


def _determine_user_from_session():
    return None
