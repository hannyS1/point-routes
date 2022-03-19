import functools
import inspect

from sqlalchemy.orm import Session

from config.database import SessionLocal


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def session(func):

    def _get_func_annotations(func_obj) -> dict:
        arg_spec = inspect.getfullargspec(func_obj)
        annotations = {}
        for arg in arg_spec.args:
            annotations[arg] = arg_spec.annotations.get(arg, None)
        return annotations

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        current_session = SessionLocal()
        new_args = []
        args_index = 0
        for key, value in _get_func_annotations(func).items():
            if value == Session:
                new_args.append(current_session)
                new_args += args[args_index:]
                break
            new_args.append(args[args_index])
            args_index += 1

        try:
            result = func(*new_args, **kwargs)
        except Exception as e:
            current_session.close()
            raise e
        finally:
            current_session.close()
        return result

    return wrapper
