import re
from enum import Enum
from typing import List, Pattern, Type

from src.python.shared.core.value_object.value_object_exception import ValueObjectException


class GuardResult:
    def __init__(self, is_failure: bool, error_value: str = None, weight: int = 1):
        self.is_failure: bool = is_failure
        self.weight: int = weight
        if is_failure is True:
            self.error_value: str = error_value

    def get_error_value(self) -> str:
        return self.error_value


class Guard:
    @staticmethod
    def against_at_least(key: str, minimum_value: int, value: str) -> GuardResult:
        if minimum_value > len(value):
            return GuardResult(True, f'{key} is not at least {minimum_value} chars')
        return GuardResult(False)

    @staticmethod
    def against_at_most(key: str, maximum_value: int, value: str) -> GuardResult:
        if maximum_value <= len(value):
            return GuardResult(True, f'{key} is not at most {maximum_value} chars')
        return GuardResult(False)

    @staticmethod
    def against_none(key: str, value: str) -> GuardResult:
        if value is None:
            return GuardResult(True, f'{key} cannot be None', weight=10)
        return GuardResult(False)

    @staticmethod
    def against_wrong_enum(key: str, value: str, enum: Type[Enum]) -> GuardResult:
        for _enum in enum:
            if _enum.value == value:
                return GuardResult(False)
        return GuardResult(True, f'{key} is not valid', weight=2)

    @staticmethod
    def against_regex(key: str, value: str, regex: Pattern[str]) -> GuardResult:
        if not re.fullmatch(regex, value):
            return GuardResult(True, f'{key} is not valid', weight=2)
        return GuardResult(False)


class MultiGuard:
    def __init__(self):
        self.results: List[GuardResult] = []

    def add_result(self, result: GuardResult):
        self.results.append(result)
        self.results = sorted(self.results, key=lambda item: item.weight)

    def check(self):
        if self.check_for_failure():
            raise ValueObjectException(self.get_all_error_results())

    def check_for_failure(self) -> bool:
        return any(result.is_failure for result in self.results)

    def get_all_error_results(self) -> list:
        errors: List[str] = []
        for result in self.results:
            if result.is_failure:
                errors.append(result.get_error_value())
        return errors
