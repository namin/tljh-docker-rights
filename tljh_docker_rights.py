from tljh.hooks import hookimpl
from tljh.user import ensure_user_group

@hookimpl
def tljh_new_user_create(username):
    ensure_user_group(username, 'docker')
