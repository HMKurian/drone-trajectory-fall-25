import typing as T
import math

import numpy as np

from src.data_model import Camera, DatasetSpec, Waypoint
from src.camera_utils import (
    compute_image_footprint_on_surface,
    compute_ground_sampling_distance,
)


def compute_distance_between_images(
    camera: Camera, dataset_spec: DatasetSpec
) -> np.ndarray:
    """Compute the distance between images in the horizontal and vertical directions for specified overlap and sidelap.

    Args:
        camera: Camera model used for image capture.
        dataset_spec: user specification for the dataset.

    Returns:
        The horizontal and vertical distance between images (as a 2-element array).

    notes:
        when a drone camera captures an image, it covers a certain area on the ground, known as the image footprint.
        Consecutive images overlap both horizontally and vertically to ensure complete coverage of the area being surveyed.

    implementation:
        we compute the image footprint which tells us how much area is covered by one image at a certain height.
        - foot print = [Fx, Fy]
        Overlap and sidelap are derived from the dataset specification.
        ex: if overlap is 0.8, it means that 80% of the area covered by one image overlaps with the next image.
        - overlap = 0.8 => 20% new area in the next image
        The distance between images can be calculated as:
            - distance_x = Fx * (1 - overlap)
            - distance_y = Fy * (1 - sidelap)
    """
    #compute footprint at the specified height
    footprint = compute_image_footprint_on_surface(camera, dataset_spec.height)
    Fx = footprint[0]
    Fy = footprint[1]

    #compute distance between images based on overlap and sidelap
    distance_x = Fx * (1 - dataset_spec.overlap)
    distance_y = Fy * (1 - dataset_spec.sidelap)

    return np.array([distance_x, distance_y])

    
    
    


def compute_speed_during_photo_capture(
    camera: Camera, dataset_spec: DatasetSpec, allowed_movement_px: float = 1
) -> float:
    """Compute the speed of drone during an active photo capture to prevent more than 1px of motion blur.

    Args:
        camera: Camera model used for image capture.
        dataset_spec: user specification for the dataset.
        allowed_movement_px: The maximum allowed movement in pixels. Defaults to 1 px.

    Returns:
        The speed at which the drone should move during photo capture.
    """
    raise NotImplementedError()


def generate_photo_plan_on_grid(
    camera: Camera, dataset_spec: DatasetSpec
) -> T.List[Waypoint]:
    """Generate the complete photo plan as a list of waypoints in a lawn-mower pattern.

    Args:
        camera: Camera model used for image capture.
        dataset_spec: user specification for the dataset.

    Returns:
        Scan plan as a list of waypoints.

    """
    raise NotImplementedError()