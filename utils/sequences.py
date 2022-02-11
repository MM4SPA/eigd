def get_sequence_number(event_time, active_sequences):
    """
    Find the matching sequence boundaries for a given event time

    Parameters
    ----------
    event_time: int
    active_sequences: List of List of int
        List with start and end points (both included) of active match

    Returns
    -------
    sequence_number: int or None
    """
    sequence_number = None
    # event during active match
    for i in range(len(active_sequences)):
        if active_sequences[i][0] <= event_time <= active_sequences[i][1]:
            sequence_number = i
            break
    # event during inactive match (between segments of active match)
    if sequence_number is None:
        for i in range(len(active_sequences) - 1):
            if active_sequences[i][0] <= event_time <= active_sequences[i+1][0]:
                sequence_number = i
                break
    # event before initial first sequence or after final active sequence
    if sequence_number is None:
        if event_time < active_sequences[0][0]:
            sequence_number = 0
        else:
            sequence_number = len(active_sequences) - 1
    return sequence_number


def get_sequence(annotation, sequence_boundaries):
    """
    Find the matching sequence for a given event time

    Parameters
    ----------
    annotation: List of dict
    sequence_boundaries: List  of int
        Start and end points (both included) of active match

    Returns
    -------
    sequence: List of dict
    """
    sequence = []
    for event in annotation:
        if sequence_boundaries[0] <= event['time'] <= sequence_boundaries[1] + 1:
            sequence.append(event)
    return sequence
