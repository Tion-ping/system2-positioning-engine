from datetime import datetime
from pydantic import BaseModel


class Detection(BaseModel):
    bearing_vector: list[float]  # [E, N, U] unit vector in ENU frame
    score: float


class CameraEvent(BaseModel):
    cam_id: str
    timestamp: datetime
    detections: list[Detection]


class Position(BaseModel):
    timestamp: datetime
    lat: float
    lon: float
    alt_m: float
    cam_pair: str
    score_i: float | None
    score_j: float | None
