from typing import Type, TypeVar

from pydantic import BaseModel

from src.python.shared.core.value_object.value_object import ValueObject

Model = TypeVar("Model", bound=BaseModel)


def dict_to_domain_loader(domain_class: Type[Model], incoming_dict: dict) -> Model:
    _loader_dict = {}
    _incoming_dict_keys = incoming_dict.keys()
    for key, value in domain_class.__annotations__.items():
        if key not in _incoming_dict_keys:
            raise ValueError(f"The following required key is missing: {key}")
        _loader_dict[key] = value(incoming_dict[key])
    return domain_class(**_loader_dict)


def domain_to_dict_loader(domain_instance: BaseModel, domain_class: Type[Model]) -> dict:
    return_value = {}
    domain_instance_dict: dict = domain_instance.dict()
    private_attributes: list = domain_class.get_private_attributes()
    for key in domain_instance_dict:
        if key in private_attributes:
            continue
        if ValueObject in domain_instance_dict[key].__class__.__mro__:
            return_value[key] = domain_instance_dict[key].get_value()
            continue
        return_value[key] = domain_instance_dict[key]
    return return_value
