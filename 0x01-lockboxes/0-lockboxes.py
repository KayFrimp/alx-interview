def canUnlockAll(boxes):
    n = len(boxes)
    unlocked_boxes = {0}

    for i in range(n):
        for key in boxes[i]:
            if key < n and key not in unlocked_boxes:
                if key != i:
                    unlocked_boxes.add(key)

    return len(unlocked_boxes) == n
