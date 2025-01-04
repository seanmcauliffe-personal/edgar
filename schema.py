from dataclasses import dataclass


@dataclass
class Education:
    degree: str
    field: str
    university: str
    year: int | None = None


@dataclass
class Executive:
    name: str
    age: int | None
    current_role: str
    past_roles: list[str]
    education: list[Education]
    compensation_salary: float
    compensation_stock: float
    compensation_bonus: float
    compensation_other: float
    compensation_total: float
    compensation_year: int
    start_date: str | None
    board_member: bool
    committee_memberships: list[str]
    other_board_memberships: list[str]
    notable_achievements: str | None
