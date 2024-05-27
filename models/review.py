#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review.

    Attributes:
        place_id (str): The id of the reviewed place.
        user_id (str): The id of the user that wrote the review.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
