from typing import Any
from . import self_app

DEFAULT_DB = 'default'


class DBMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        # One time configuration and init
    
    def __call__(self, request) -> Any:
        # code to be executed for each request before
        # the view (and later middleware) are called.
        self._setup_db(request)
        response = self.get_response(request)

        # code to be executed for each request/response after the view is called
        return response
    
    def _setup_db(self, request):
        """Set  db based on request"""
        self_app.db = request.headers.get('db') or DEFAULT_DB


class DBRouter:
    """
    Specifies which database to connect to when using ORM.
    """

    def db_for_read(self, model, **hints):
        return getattr(self_app, 'db', DEFAULT_DB)

    def db_for_write(self, model, **hints):
        return getattr(self_app, 'db', DEFAULT_DB)

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
    
