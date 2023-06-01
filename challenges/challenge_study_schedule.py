def verify(element):
    if element is None:
        return True
    if isinstance(element, str):
        return True

    return False


def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0

    for student in permanence_period:
        if verify(student[0]) or verify(student[1]):
            return None

        if target_time >= student[0] and target_time <= student[1]:
            count += 1

    return count
