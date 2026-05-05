from pydantic import BaseModel, Field

from core.constants import DEFAULT_COLS, DEFAULT_OUTPUT, DEFAULT_ROWS


class LayoutConfig(BaseModel):
    items: dict[str, str]
    out_path: str = DEFAULT_OUTPUT
    cols: int = Field(default=DEFAULT_COLS, ge=1)
    rows: int = Field(default=DEFAULT_ROWS, ge=1)
    margin: float = Field(default=36, ge=0)
