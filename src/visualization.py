"""Utility to visualize photo plans.
"""

"""Utility to visualize photo plans.
"""

import typing as T
import plotly.graph_objects as go
from src.data_model import Waypoint


def plot_photo_plan(photo_plans: T.List[Waypoint]) -> go.Figure:
    """Plot the photo plan on a 2D grid.

    Args:
        photo_plans: List of waypoints for the photo plan.

    Returns:
        Plotly figure object.
    """

    # Extract x and y coordinates from the Waypoints
    xs = [wp.x for wp in photo_plans]
    ys = [wp.y for wp in photo_plans]

    # Create the Plotly figure
    fig = go.Figure()

    # Add the drone flight path (connected waypoints)
    fig.add_trace(go.Scatter(
        x=xs,
        y=ys,
        mode="lines+markers",
        name="Flight Path",
        line=dict(color="royalblue", width=2),
        marker=dict(size=6, color="orange")
    ))

    # Mark the start and end points
    fig.add_trace(go.Scatter(
        x=[xs[0]],
        y=[ys[0]],
        mode="markers+text",
        text=["Start"],
        textposition="bottom center",
        marker=dict(color="green", size=10)
    ))

    fig.add_trace(go.Scatter(
        x=[xs[-1]],
        y=[ys[-1]],
        mode="markers+text",
        text=["End"],
        textposition="bottom center",
        marker=dict(color="red", size=10)
    ))

    # Format layout
    fig.update_layout(
        title="Drone Photo Flight Plan",
        xaxis_title="X Coordinate (m)",
        yaxis_title="Y Coordinate (m)",
        width=800,
        height=600,
        showlegend=True,
        template="plotly_white"
    )

    # Ensure equal scaling for x and y axes
    fig.update_yaxes(scaleanchor="x", scaleratio=1)

    return fig
