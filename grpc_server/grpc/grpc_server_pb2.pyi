from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateGamePartialUpdateRequest(_message.Message):
    __slots__ = ["id", "status", "user_1_points", "user_2_points", "winner"]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_1_POINTS_FIELD_NUMBER: _ClassVar[int]
    USER_2_POINTS_FIELD_NUMBER: _ClassVar[int]
    WINNER_FIELD_NUMBER: _ClassVar[int]
    id: int
    status: str
    user_1_points: float
    user_2_points: float
    winner: str
    def __init__(self, id: _Optional[int] = ..., winner: _Optional[str] = ..., user_1_points: _Optional[float] = ..., user_2_points: _Optional[float] = ..., status: _Optional[str] = ...) -> None: ...

class CreateGameRequest(_message.Message):
    __slots__ = ["user_1", "user_2"]
    USER_1_FIELD_NUMBER: _ClassVar[int]
    USER_2_FIELD_NUMBER: _ClassVar[int]
    user_1: int
    user_2: int
    def __init__(self, user_1: _Optional[int] = ..., user_2: _Optional[int] = ...) -> None: ...

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
    __slots__ = ["checker_id", "game", "is_dead", "is_king", "is_white", "killed", "new_positions", "user"]
    CHECKER_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_FIELD_NUMBER: _ClassVar[int]
    IS_DEAD_FIELD_NUMBER: _ClassVar[int]
    IS_KING_FIELD_NUMBER: _ClassVar[int]
    IS_WHITE_FIELD_NUMBER: _ClassVar[int]
    KILLED_FIELD_NUMBER: _ClassVar[int]
    NEW_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    checker_id: int
    game: int
    is_dead: bool
    is_king: bool
    is_white: bool
    killed: _containers.RepeatedScalarFieldContainer[int]
    new_positions: _containers.RepeatedScalarFieldContainer[str]
    user: int
    def __init__(self, game: _Optional[int] = ..., user: _Optional[int] = ..., checker_id: _Optional[int] = ..., new_positions: _Optional[_Iterable[str]] = ..., is_king: bool = ..., is_white: bool = ..., is_dead: bool = ..., killed: _Optional[_Iterable[int]] = ...) -> None: ...

class GameResponse(_message.Message):
    __slots__ = ["finish_at", "id", "start_at", "status", "user_1_info", "user_1_points", "user_1_turn", "user_2_info", "user_2_points", "winner"]
    FINISH_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    START_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_1_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_1_POINTS_FIELD_NUMBER: _ClassVar[int]
    USER_1_TURN_FIELD_NUMBER: _ClassVar[int]
    USER_2_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_2_POINTS_FIELD_NUMBER: _ClassVar[int]
    WINNER_FIELD_NUMBER: _ClassVar[int]
    finish_at: str
    id: int
    start_at: str
    status: str
    user_1_info: CreateGameRequestUserInfo
    user_1_points: float
    user_1_turn: bool
    user_2_info: CreateGameRequestUserInfo
    user_2_points: float
    winner: str
    def __init__(self, id: _Optional[int] = ..., user_1_info: _Optional[_Union[CreateGameRequestUserInfo, _Mapping]] = ..., user_2_info: _Optional[_Union[CreateGameRequestUserInfo, _Mapping]] = ..., user_1_turn: bool = ..., winner: _Optional[str] = ..., user_1_points: _Optional[float] = ..., user_2_points: _Optional[float] = ..., start_at: _Optional[str] = ..., finish_at: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class MoveResponse(_message.Message):
    __slots__ = ["checker_id", "game", "id", "is_dead", "is_king", "is_last_move", "is_white", "new_positions", "user"]
    CHECKER_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_DEAD_FIELD_NUMBER: _ClassVar[int]
    IS_KING_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_MOVE_FIELD_NUMBER: _ClassVar[int]
    IS_WHITE_FIELD_NUMBER: _ClassVar[int]
    NEW_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    checker_id: int
    game: int
    id: int
    is_dead: bool
    is_king: bool
    is_last_move: bool
    is_white: bool
    new_positions: _containers.RepeatedScalarFieldContainer[str]
    user: int
    def __init__(self, id: _Optional[int] = ..., game: _Optional[int] = ..., user: _Optional[int] = ..., checker_id: _Optional[int] = ..., new_positions: _Optional[_Iterable[str]] = ..., is_king: bool = ..., is_white: bool = ..., is_dead: bool = ..., is_last_move: bool = ...) -> None: ...
