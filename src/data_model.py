"""Data models for the camera and user specification."""
from dataclasses import dataclass
@dataclass
class DatasetSpec:
    """
    Data model for specifications of an image dataset.
    """

    overlap: float
    sidelap: float
    height: float
    scan_dimension_x: float
    scan_dimension_y: float
    exposure_time_ms: int

    def __post_init__(self):
        if not (0 <= self.overlap <= 1):
            raise ValueError(f"Overlap must be between 0 and 1")
        if not (0 <= self.sidelap <= 1):
            raise ValueError(f"Sidelap must be between 0 and 1")
        if self.height <= 0:
            raise ValueError("Height must be positive")
        if self.scan_dimension_x <= 0:
            raise ValueError("Scan dimension x must be positive")
        if self.scan_dimension_y <= 0:
            raise ValueError("Scan dimension y must be positive")
        if self.exposure_time_ms <= 0:
            raise ValueError("Exposure time must be positive")
    pass


class Camera:
    """
    Data model for a simple pinhole camera.

    References:
    - https://github.com/colmap/colmap/blob/3f75f71310fdec803ab06be84a16cee5032d8e0d/src/colmap/sensor/models.h#L220
    - https://en.wikipedia.org/wiki/Pinhole_camera_model
    """

    pass


class Waypoint:
    """
    Waypoints are positions where the drone should fly to and capture a photo.
    """

    pass
