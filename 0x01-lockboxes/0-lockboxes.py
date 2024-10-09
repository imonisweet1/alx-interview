#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened given the keys inside them.

    Args:
        boxes (list of list of int): A list of boxes,
        each containing a list of keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    num_of_boxes = len(boxes)
    unlocked_boxes = set([0])
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < num_of_boxes and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            keys.update(boxes[key])

    return len(unlocked_boxes) == num_of_boxes
