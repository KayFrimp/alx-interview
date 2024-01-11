#!/usr/bin/python3
"""canUnlockAll Module"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened
       boxes is a list of lists with keys that can
       open boxes

       Returns:
           True if all boxes can be unlocked else False"""
    n = len(boxes)
    unlocked_boxes = {0}

    for i in range(n):
        for key in boxes[i]:
            if key < n and key not in unlocked_boxes:
                if key != i:
                    unlocked_boxes.add(key)

    return len(unlocked_boxes) == n
