from typing import Type, TypeVar

from fastapi import HTTPException
from pydantic import BaseModel

Model = TypeVar("Model", bound=BaseModel)


def _dict_loader(t: Type[Model], o: dict) -> Model:
    populated_keys = o.keys()
    required_keys = set(t.schema()['required'])
    missing_keys = required_keys.difference(populated_keys)
    if missing_keys:
        raise ValueError(f'Required keys missing: {missing_keys}')
    all_definition_keys = t.schema()['properties'].keys()
    return t(**{k: v for k, v in o.items() if k in all_definition_keys})


def _list_loader(t: Type[Model], o: list) -> Model:
    keys = t.__fields__.keys()
    if o is None:
        raise HTTPException(status_code=400, detail='Someting went wrong.')
    if len(keys) != len(o):
        raise ValueError('Missing values')
    return t(**dict(zip(keys, o)))
