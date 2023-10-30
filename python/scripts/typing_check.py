from typing import NamedTuple, Literal, TypedDict, Sequence, Iterable, Mapping, TypeVar, Callable
from dataclasses import dataclass
from pympler import asizeof
from datetime import datetime


# NamedTuple #################
class CoordinatesNT(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates_nt() -> CoordinatesNT:
    return CoordinatesNT(latitude=10.0, longitude=20.0)


coordinates_nt = get_coordinates_nt()
print(coordinates_nt.latitude, coordinates_nt.longitude)


# Literal #####################
def get_coordinated_literal() -> dict[Literal['latitude'] | Literal['longitude'], float]:
    return {'latitude': 10.0, 'longitude': 20.0}


coordinates_literal = get_coordinated_literal()
print(coordinates_literal['latitude'], coordinates_literal['longitude'])


# TypedDict ###################
class CoordinatesTD(TypedDict):
    latitude: float
    longitude: float


def get_coordinated_td() -> CoordinatesTD:
    return {'latitude': 10.0, 'longitude': 20.0}


coordinates_td = get_coordinated_td()
print(coordinates_td['latitude'], coordinates_td['longitude'])


# DataClass ###################
@dataclass
class CoordinatesDC:
    latitude: float
    longitude: float


def get_coordinates_dc() -> CoordinatesDC:
    return CoordinatesDC(latitude=10.0, longitude=20.0)


coordinates_dc = get_coordinates_dc()
print(coordinates_dc.latitude, coordinates_dc.longitude)

print(asizeof.asizeof(coordinates_dc))
print(asizeof.asizeof(coordinates_nt))


# Iterable #################
# when just iterate through all elements
@dataclass
class User:
    birthdate: datetime


users_tuple = (
    User(birthdate=datetime.fromisoformat("1988-01-01")),
    User(birthdate=datetime.fromisoformat("1999-02-11")),
    User(birthdate=datetime.fromisoformat("1987-09-21")),
)

users_list = [
    User(birthdate=datetime.fromisoformat("1988-01-01")),
    User(birthdate=datetime.fromisoformat("1999-02-11")),
    User(birthdate=datetime.fromisoformat("1987-09-21")),
]

users_gen = (user for user in users_list)


def get_younger_user_iterable(users: Iterable[User]) -> User:
    """
    :param users: Iterable since we do not need to get users by indexes
    :return:
    """
    sorted_users = sorted(users, key=lambda u: u.birthdate)
    return sorted_users[0]


user = get_younger_user_iterable(users_list)
print(user)
user = get_younger_user_iterable(users_tuple)
print(user)
user = get_younger_user_iterable(users_gen)
print(user)


def get_younger_user_sequence(users: Sequence[User]) -> User:
    """
    :param users: Here we get user by index so the users type is Sequence
    :return:
    """
    print(users[0])
    sorted_users = sorted(users, key=lambda u: u.birthdate)
    return sorted_users[0]


user = get_younger_user_sequence(users_list)
print(user)
user = get_younger_user_sequence(users_tuple)
print(user)
# We cannot use the following function for generators
# users_gen = (user for user in users_list)
# user = get_younger_user_sequence(users_gen)
# print(user)


# Mapping #################
def print_some_user(users: Mapping[str, User]) -> None:
    """
    :param users: Mapping - for any key/value container
    :return:
    """
    print(users['my_user'])


print_some_user({
    'my_user': User(birthdate=datetime.fromisoformat("1988-01-01")),
    'next_one': User(birthdate=datetime.fromisoformat("1999-02-11")),
})


class Users(Mapping):
    def __init__(self, users: Sequence[User]) -> None:
        self._users = users

    def __getitem__(self, key: int) -> User:
        return self._users[key]

    def __iter__(self):
        return iter(self._users)

    def __len__(self):
        return len(self._users)


users_container = Users((
    User(birthdate=datetime.fromisoformat("1988-01-01")),
    User(birthdate=datetime.fromisoformat("1999-02-11")),
    User(birthdate=datetime.fromisoformat("1987-09-21")),
))


def get_some_user(users: Mapping[int, User]) -> User:
    """
    :param users: Mapping - for any key/value container
    :return:
    """
    return users[0]


user = get_some_user(users_container)
print(user)


# Generics #################
T = TypeVar("T")


def first(iterable: Iterable[T]) -> T | None:
    for element in iterable:
        return element


print(first(['one', 'two']))
print(first([1, 2]))
print(first((11, 22)))


# Callable #################
def mysum(a: int, b: int) -> int:
    return a + b


def process_operation(operation: Callable[[int, int], int],
                      arg1: int, arg2: int) -> int:
    return operation(arg1, arg2)


print(process_operation(mysum, 11, 22))
