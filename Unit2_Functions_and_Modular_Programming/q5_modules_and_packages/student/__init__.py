"""student package.
__init__.py runs when the package is imported and exposes selected
functions so they can be used directly as student.get_details(...)."""

from .details import get_details, display_details
from .results import calculate_total, get_grade, display_result

__all__ = ["get_details", "display_details", "calculate_total",
           "get_grade", "display_result"]

print("[student package initialised]")
