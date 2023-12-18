#!/usr/bin/python3
"""
Defines the Review class for representing user reviews.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who made the review.
        text (str): The text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
