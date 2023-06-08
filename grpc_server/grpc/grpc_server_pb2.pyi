from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateGamePartialUpdateRequest(_message.Message):
    __slots__ = ["id", "status", "userOnePoints", "userTwoPoints", "winner"]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USERONEPOINTS_FIELD_NUMBER: _ClassVar[int]
    USERTWOPOINTS_FIELD_NUMBER: _ClassVar[int]
    WINNER_FIELD_NUMBER: _ClassVar[int]
    id: int
    status: str
    userOnePoints: float
    userTwoPoints: float
    winner: str
    def __init__(self, id: _Optional[int] = ..., winner: _Optional[str] = ..., userOnePoints: _Optional[float] = ..., userTwoPoints: _Optional[float] = ..., status: _Optional[str] = ...) -> None: ...

class CreateGameRequest(_message.Message):
    __slots__ = ["userOne", "userTwo"]
    USERONE_FIELD_NUMBER: _ClassVar[int]
    USERTWO_FIELD_NUMBER: _ClassVar[int]
    userOne: int
    userTwo: int
    def __init__(self, userOne: _Optional[int] = ..., userTwo: _Optional[int] = ...) -> None: ...

class CreateGameRequestUserInfo(_message.Message):
    __slots__ = ["email", "id", "username"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    id: int
    username: str
    def __init__(self, id: _Optional[int] = ..., username: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class CreateMoveRequest(_message.Message):
    __slots__ = ["checkerId", "game", "isDead", "isKing", "isWhite", "killed", "newPositions", "user"]
    CHECKERID_FIELD_NUMBER: _ClassVar[int]
    GAME_FIELD_NUMBER: _ClassVar[int]
    ISDEAD_FIELD_NUMBER: _ClassVar[int]
    ISKING_FIELD_NUMBER: _ClassVar[int]
    ISWHITE_FIELD_NUMBER: _ClassVar[int]
    KILLED_FIELD_NUMBER: _ClassVar[int]
    NEWPOSITIONS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    checkerId: int
    game: int
    isDead: bool
    isKing: bool
    isWhite: bool
    killed: _containers.RepeatedScalarFieldContainer[int]
    newPositions: _containers.RepeatedScalarFieldContainer[str]
    user: int
    def __init__(self, game: _Optional[int] = ..., user: _Optional[int] = ..., checkerId: _Optional[int] = ..., newPositions: _Optional[_Iterable[str]] = ..., isKing: bool = ..., isWhite: bool = ..., isDead: bool = ..., killed: _Optional[_Iterable[int]] = ...) -> None: ...

class GameResponse(_message.Message):
    __slots__ = ["finishAt", "id", "startAt", "status", "userOneInfo", "userOnePoints", "userOneTurn", "userTwoInfo", "userTwoPoints", "winner"]
    FINISHAT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STARTAT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USERONEINFO_FIELD_NUMBER: _ClassVar[int]
    USERONEPOINTS_FIELD_NUMBER: _ClassVar[int]
    USERONETURN_FIELD_NUMBER: _ClassVar[int]
    USERTWOINFO_FIELD_NUMBER: _ClassVar[int]
    USERTWOPOINTS_FIELD_NUMBER: _ClassVar[int]
    WINNER_FIELD_NUMBER: _ClassVar[int]
    finishAt: str
    id: int
    startAt: str
    status: str
    userOneInfo: CreateGameRequestUserInfo
    userOnePoints: float
    userOneTurn: bool
    userTwoInfo: CreateGameRequestUserInfo
    userTwoPoints: float
    winner: str
    def __init__(self, id: _Optional[int] = ..., userOneInfo: _Optional[_Union[CreateGameRequestUserInfo, _Mapping]] = ..., userTwoInfo: _Optional[_Union[CreateGameRequestUserInfo, _Mapping]] = ..., userOneTurn: bool = ..., winner: _Optional[str] = ..., userOnePoints: _Optional[float] = ..., userTwoPoints: _Optional[float] = ..., startAt: _Optional[str] = ..., finishAt: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class MoveResponse(_message.Message):
    __slots__ = ["checkerId", "game", "id", "isDead", "isKing", "isLastMove", "isWhite", "newPositions", "user"]
    CHECKERID_FIELD_NUMBER: _ClassVar[int]
    GAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ISDEAD_FIELD_NUMBER: _ClassVar[int]
    ISKING_FIELD_NUMBER: _ClassVar[int]
    ISLASTMOVE_FIELD_NUMBER: _ClassVar[int]
    ISWHITE_FIELD_NUMBER: _ClassVar[int]
    NEWPOSITIONS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    checkerId: int
    game: int
    id: int
    isDead: bool
    isKing: bool
    isLastMove: bool
    isWhite: bool
    newPositions: _containers.RepeatedScalarFieldContainer[str]
    user: int
    def __init__(self, id: _Optional[int] = ..., game: _Optional[int] = ..., user: _Optional[int] = ..., checkerId: _Optional[int] = ..., newPositions: _Optional[_Iterable[str]] = ..., isKing: bool = ..., isWhite: bool = ..., isDead: bool = ..., isLastMove: bool = ...) -> None: ...
