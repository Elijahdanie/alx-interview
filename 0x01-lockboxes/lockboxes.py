"""
This module computes if all boxes
can be unlocked
"""


def canUnlockAll(boxes):
    """
    This function returns a true if all boxes
    passed in can be unlocked else false
        Args:
            boxes: This is a list of boxes containing keys
                    so its a 2dimension array or list of list
    """

    keys = boxes[0] if len(boxes) > 0 else []
    