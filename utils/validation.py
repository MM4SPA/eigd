from utils.eval import event_tolerances
from utils.hierarchy import create_hierarchy_descriptions
from utils.sequences import get_sequence_number, get_sequence
import numpy as np


def get_positives(
    prediction, reference, event_tolerances, hierarchy_level=0, active_sequences=None
):
    """
    Returns a dict with True and False positives either with or without SCM (based on prediction)

    Parameters
    ----------
    prediction: List of dict
    reference: List of dict
    event_tolerances: dict
        Unique tolerance areas for each event type
    hierarchy_level: int in [0, 4]
        Level in the hierarchy
    active_sequences: List of List of List of int
        List with the active sequences for prediction (0) and reference (1) each containing the start and end points
        (both included) of active match for the respective annotation. If specified, sequence consistency matching is
        applied for computing the precision
    Returns
    -------
    stats: dict
    """
    # initialize variables
    true_positives = {}
    false_positives = {}
    stats = {}

    # prediction loop
    for predicted_event in prediction:

        # DEBUG
        # goal = False
        # if 'game status event' in predicted_event['action']:
        #    if 'static ball action' in predicted_event['action']['game status event']:
        #        goal = True
        #        if predicted_event['action']['game status event']['referee decision'] == 'referee other':
        #            goal = True
        # if not goal:
        #    continue
        # if goal:
        #    debug =0

        # initialize variables
        temporal_distances = []
        prediction_descriptions = create_hierarchy_descriptions(predicted_event)
        if hierarchy_level < len(prediction_descriptions):
            prediction_dc = prediction_descriptions[hierarchy_level]
        else:
            continue
        prediction_time = predicted_event["time"]
        sequence_consistent = True

        # initialize tolerance
        if prediction_dc in event_tolerances:
            tolerance = event_tolerances[prediction_dc]
        else:
            tolerance = 25
            continue

        # without SCM: find nearest neighbour
        if active_sequences is None:
            # find closest event of same description
            for reference_event in reference:
                # get description
                reference_descriptions = create_hierarchy_descriptions(reference_event)
                if hierarchy_level < len(reference_descriptions):
                    reference_dc = reference_descriptions[hierarchy_level]
                else:
                    reference_dc = reference_descriptions[-1]
                # add matching descriptions to distances
                if reference_dc == prediction_dc:
                    temporal_distances.append(
                        np.abs(reference_event["time"] - prediction_time)
                    )

        # with SCM: check for sequence consistency and then assign event with same order within sequence
        else:
            # initialize prediction sequence
            sequence_number = get_sequence_number(prediction_time, active_sequences[0])

            if sequence_number is not None:  # referee decision
                # find order within sequence
                prediction_occurrence = None
                num_sequence_predictions = 0
                if sequence_number == 0:
                    prediction_sequence_boundaries = [
                        0,
                        active_sequences[0][sequence_number + 1][0],
                    ]
                elif sequence_number == len(active_sequences[0]) - 1:
                    prediction_sequence_boundaries = [
                        active_sequences[0][sequence_number][0],
                        1000000,
                    ]
                else:
                    prediction_sequence_boundaries = [
                        active_sequences[0][sequence_number][0],
                        active_sequences[0][sequence_number + 1][0],
                    ]
                prd_sequence = get_sequence(prediction, prediction_sequence_boundaries)
                for event in prd_sequence:
                    # initialize event
                    event_descriptions = create_hierarchy_descriptions(event)
                    if hierarchy_level < len(event_descriptions):
                        event_dc = event_descriptions[hierarchy_level]
                    else:
                        event_dc = event_descriptions[-1]
                    # count number of occurrences
                    if event_dc == prediction_dc:
                        if event["time"] == prediction_time:
                            prediction_occurrence = num_sequence_predictions
                        num_sequence_predictions += 1

                # find matching sequence order for reference
                sequence_reference_times = []
                if sequence_number == 0:
                    reference_sequence_boundaries = [
                        0,
                        active_sequences[1][sequence_number + 1][0],
                    ]
                elif sequence_number == len(active_sequences[1]) - 1:
                    reference_sequence_boundaries = [
                        active_sequences[1][sequence_number][0],
                        1000000,
                    ]
                else:
                    reference_sequence_boundaries = [
                        active_sequences[1][sequence_number][0],
                        active_sequences[1][sequence_number + 1][0],
                    ]
                ref_sequence = get_sequence(reference, reference_sequence_boundaries)
                for event in ref_sequence:
                    # initialize event
                    event_descriptions = create_hierarchy_descriptions(event)
                    if hierarchy_level < len(event_descriptions):
                        event_dc = event_descriptions[hierarchy_level]
                    else:
                        event_dc = event_descriptions[-1]
                    if event_dc == prediction_dc:
                        sequence_reference_times.append(event["time"])

                # update global dict
                if prediction_dc not in stats:
                    stats[prediction_dc] = {}
                # sequence consistent events
                if len(sequence_reference_times) == num_sequence_predictions:
                    # update temporal distances
                    temporal_distances.append(
                        np.abs(
                            sequence_reference_times[prediction_occurrence]
                            - prediction_time
                        )
                    )
                    # update number of consistent events
                    if "SQC" in stats[prediction_dc]:
                        stats[prediction_dc]["SQC"] += 1
                    else:
                        stats[prediction_dc]["SQC"] = 1
                # sequence inconsistent events
                else:
                    # update number of inconsistent events
                    sequence_consistent = False
                    if "SQI" in stats[prediction_dc]:
                        stats[prediction_dc]["SQI"] += 1
                    else:
                        stats[prediction_dc]["SQI"] = 1

        # assign to true/false positives
        if sequence_consistent:
            if len(temporal_distances) and np.min(temporal_distances) <= tolerance:
                if prediction_dc in true_positives:
                    true_positives[prediction_dc] += 1
                else:
                    true_positives[prediction_dc] = 1
            else:
                if prediction_dc in false_positives:
                    false_positives[prediction_dc] += 1
                else:
                    false_positives[prediction_dc] = 1

    # save results to stats dict
    for dc in set(list(true_positives.keys()) + list(false_positives.keys())):
        if dc not in stats:
            stats[dc] = {}
        if dc in true_positives:
            if "TP" in stats[dc]:
                stats[dc]["TP"] += true_positives[dc]
            else:
                stats[dc]["TP"] = true_positives[dc]
        if dc in false_positives:
            if "FP" in stats[dc]:
                stats[dc]["FP"] += false_positives[dc]
            else:
                stats[dc]["FP"] = false_positives[dc]
    return stats


def get_negatives(
    prediction, reference, event_tolerances, hierarchy_level=0, active_sequences=None
):
    """
    Returns a dict with False negatives either with or without SCM (based on reference)

    Parameters
    ----------
    prediction: List of dict
    reference: List of dict
    event_tolerances: dict
        Unique tolerance areas for each event type
    hierarchy_level: int in [0, 4]
        Level in the hierarchy
    active_sequences: List of List of List of int
        List with the active sequences for prediction (0) and reference (1) each containing the start and end points
        (both included) of active match for the respective annotation. If specified, sequence consistency matching is
        applied for computing the precision
    Returns
    -------
    stats: dict
    """
    # initialize variables
    false_negatives = {}
    stats = {}

    # prediction loop
    for reference_event in reference:

        # initialize variables
        temporal_distances = []
        reference_descriptions = create_hierarchy_descriptions(reference_event)
        if hierarchy_level < len(reference_descriptions):
            reference_dc = reference_descriptions[hierarchy_level]
        else:
            continue
        reference_time = reference_event["time"]
        sequence_consistent = True

        # initialize tolerance
        if reference_dc in event_tolerances:
            tolerance = event_tolerances[reference_dc]
        else:
            tolerance = 25
            continue

        # without SCM: find nearest neighbour
        if active_sequences is None:
            # find closest event of same description
            for predicted_event in prediction:
                # get description
                prediction_descriptions = create_hierarchy_descriptions(predicted_event)
                if hierarchy_level < len(prediction_descriptions):
                    prediction_dc = prediction_descriptions[hierarchy_level]
                else:
                    prediction_dc = prediction_descriptions[-1]
                # add matching descriptions to distances
                if reference_dc == prediction_dc:
                    temporal_distances.append(
                        np.abs(predicted_event["time"] - reference_time)
                    )

        # with SCM: check for sequence consistency and then assign event with same order within sequence
        else:
            # initialize prediction sequence
            sequence_number = get_sequence_number(reference_time, active_sequences[1])

            if sequence_number is not None:  # referee decision
                # find order within sequence
                reference_occurrence = None
                num_sequence_references = 0
                if sequence_number == 0:
                    reference_sequence_boundaries = [
                        0,
                        active_sequences[1][sequence_number + 1][0],
                    ]
                elif sequence_number == len(active_sequences[1]) - 1:
                    reference_sequence_boundaries = [
                        active_sequences[1][sequence_number][0],
                        1000000,
                    ]
                else:
                    reference_sequence_boundaries = [
                        active_sequences[1][sequence_number][0],
                        active_sequences[1][sequence_number + 1][0],
                    ]

                ref_sequence = get_sequence(reference, reference_sequence_boundaries)
                for event in ref_sequence:
                    # initialize event
                    event_descriptions = create_hierarchy_descriptions(event)
                    if hierarchy_level < len(event_descriptions):
                        event_dc = event_descriptions[hierarchy_level]
                    else:
                        event_dc = event_descriptions[-1]
                    # count number of occurrences
                    if event_dc == reference_dc:
                        if event["time"] == reference_time:
                            reference_occurrence = num_sequence_references
                        num_sequence_references += 1

                # find matching sequence order in prediction
                sequence_prediction_times = []
                if sequence_number == 0:
                    prediction_sequence_boundaries = [
                        0,
                        active_sequences[0][sequence_number + 1][0],
                    ]
                elif sequence_number == len(active_sequences[0]) - 1:
                    prediction_sequence_boundaries = [
                        active_sequences[0][sequence_number][0],
                        1000000,
                    ]
                else:
                    prediction_sequence_boundaries = [
                        active_sequences[0][sequence_number][0],
                        active_sequences[0][sequence_number + 1][0],
                    ]

                prd_sequence = get_sequence(prediction, prediction_sequence_boundaries)
                for event in prd_sequence:
                    # initialize event
                    event_descriptions = create_hierarchy_descriptions(event)
                    if hierarchy_level < len(event_descriptions):
                        event_dc = event_descriptions[hierarchy_level]
                    else:
                        event_dc = event_descriptions[-1]
                    if event_dc == reference_dc:
                        sequence_prediction_times.append(event["time"])

                # update global dict
                if reference_dc not in stats:
                    stats[reference_dc] = {}
                # sequence consistent events
                if len(sequence_prediction_times) == num_sequence_references:
                    if reference_occurrence is None:
                        print("Sequence corrupted?")
                    # update temporal distances
                    temporal_distances.append(
                        np.abs(
                            sequence_prediction_times[reference_occurrence]
                            - reference_time
                        )
                    )
                    # update number of consistent events
                    if "SQC" in stats[reference_dc]:
                        stats[reference_dc]["SQC"] += 1
                    else:
                        stats[reference_dc]["SQC"] = 1
                # sequence inconsistent events
                else:
                    # update number of inconsistent events
                    sequence_consistent = False
                    if "SQI" in stats[reference_dc]:
                        stats[reference_dc]["SQI"] += 1
                    else:
                        stats[reference_dc]["SQI"] = 1

        # assign to true/false positives
        if sequence_consistent and (
            len(temporal_distances) == 0 or np.min(temporal_distances) > tolerance
        ):
            if reference_dc in false_negatives:
                false_negatives[reference_dc] += 1
            else:
                false_negatives[reference_dc] = 1

    # save results to stats dict
    for dc in list(false_negatives.keys()):
        if dc not in stats:
            stats[dc] = {}
        if dc in false_negatives:
            if "FN" in stats[dc]:
                stats[dc]["FN"] += false_negatives[dc]
            else:
                stats[dc]["FN"] = false_negatives[dc]
    return stats


def perform_full_validation(references, predictions):

    global_results_records = []
    # of format:
    # {
    #     "method": None,
    #     "hierarchy_level": None,
    #     "event_type": None,
    #     "precision": 0.0
    #     "recall": 0.0
    #     "TP":
    #     "FP":
    #     "FN":
    #     "SQC_num":
    #     "SQI_num":
    # }

    for scm in [0, 1]:
        if scm:
            print(
                "------------------ Sequence Consistency Matching (SCM) Results ------------------"
            )
        else:
            print(
                "------------------ Nearest Neighbour Matching (NNM) Results ------------------"
            )
        for hierarchy_level in range(6):
            print(f"\n#### Hierarchy Level {hierarchy_level} ####")
            pos_stats = {}
            neg_stats = {}
            # iterate over all combinations
            for ctr1, reference in enumerate(references):
                for ctr2, prediction in enumerate(predictions):
                    if prediction != reference:
                        # compare annotations
                        for scene in range(len(reference)):
                            # initialize sequences
                            if scm:
                                # initialize active match for both annotations
                                active_sequences = [
                                    prediction[scene][0]["act"]["active"],
                                    reference[scene][0]["act"]["active"],
                                ]

                                # check for same number of sequences
                                assert len(active_sequences[0]) == len(
                                    active_sequences[1]
                                ), f"Number of sequences for scene {scene} does not match!"
                            else:
                                active_sequences = None

                            # compute precision
                            current_pos = get_positives(
                                prediction[scene][1],
                                reference[scene][1],
                                event_tolerances=event_tolerances,
                                active_sequences=active_sequences,
                                hierarchy_level=hierarchy_level,
                            )

                            # compute recall
                            current_neg = get_negatives(
                                prediction[scene][1],
                                reference[scene][1],
                                event_tolerances=event_tolerances,
                                active_sequences=active_sequences,
                                hierarchy_level=hierarchy_level,
                            )

                            # update global positive stats
                            for dc in current_pos:
                                if dc in pos_stats:
                                    for key in current_pos[dc]:
                                        if key in pos_stats[dc]:
                                            pos_stats[dc][key] += current_pos[dc][key]
                                        else:
                                            pos_stats[dc][key] = current_pos[dc][key]
                                else:
                                    pos_stats[dc] = current_pos[dc]

                            # update global negative stats
                            for dc in current_neg:
                                if dc in neg_stats:
                                    for key in current_neg[dc]:
                                        if key in neg_stats[dc]:
                                            neg_stats[dc][key] += current_neg[dc][key]
                                        else:
                                            neg_stats[dc][key] = current_neg[dc][key]
                                else:
                                    neg_stats[dc] = current_neg[dc]

            # print global stats
            for dc in set(list(pos_stats.keys()) + list(neg_stats.keys())):
                # compute precision
                if dc in pos_stats and "FP" in pos_stats[dc] and "TP" in pos_stats[dc]:
                    prc = pos_stats[dc]["TP"] / (
                        pos_stats[dc]["TP"] + pos_stats[dc]["FP"]
                    )
                elif dc in pos_stats and "TP" in pos_stats[dc]:
                    prc = 1.0
                else:
                    prc = 0

                # compute recall
                if dc in neg_stats:
                    if (
                        dc in pos_stats
                        and "TP" in pos_stats[dc]
                        and "FN" in neg_stats[dc]
                    ):
                        rec = pos_stats[dc]["TP"] / (
                            pos_stats[dc]["TP"] + neg_stats[dc]["FN"]
                        )
                    elif dc in pos_stats and "TP" in pos_stats[dc]:
                        rec = 1.0
                    else:
                        rec = 0
                else:
                    rec = 0

                # print results
                print("\n" + dc)
                print(
                    "Precision %.1f%% (%d TP/%d FP)"
                    % (
                        100 * prc,
                        pos_stats[dc]["TP"]
                        if dc in pos_stats and "TP" in pos_stats[dc]
                        else 0,
                        pos_stats[dc]["FP"]
                        if dc in pos_stats and "FP" in pos_stats[dc]
                        else 0,
                    )
                )

                if scm:
                    print(
                        "%d Consistent vs. %d Inconsistent -> %.0f%%)"
                        % (
                            pos_stats[dc]["SQC"]
                            if dc in pos_stats and "SQC" in pos_stats[dc]
                            else 0,
                            pos_stats[dc]["SQI"]
                            if dc in pos_stats and "SQI" in pos_stats[dc]
                            else 0,
                            100
                            * pos_stats[dc]["SQC"]
                            / (pos_stats[dc]["SQI"] + pos_stats[dc]["SQC"])
                            if dc in pos_stats
                            and "SQC" in pos_stats[dc]
                            and "SQI" in pos_stats[dc]
                            else 0,
                        )
                    )
                print(
                    "Recall %.1f%% (%d TP/%d FN)"
                    % (
                        100 * rec,
                        pos_stats[dc]["TP"]
                        if dc in pos_stats and "TP" in pos_stats[dc]
                        else 0,
                        neg_stats[dc]["FN"]
                        if dc in neg_stats and "FN" in neg_stats[dc]
                        else 0,
                    )
                )
                global_results_records.append(
                    {
                        "method": "SCM" if scm else "NNM",
                        "hierarchy_level": hierarchy_level,
                        "event_type": dc,
                        "recall": rec,
                        "precision": prc,
                        "TP": pos_stats[dc]["TP"]
                        if dc in pos_stats and "TP" in pos_stats[dc]
                        else 0.0,
                        "FP": pos_stats[dc]["FP"]
                        if dc in pos_stats and "FP" in pos_stats[dc]
                        else 0.0,
                        "FN": neg_stats[dc]["FN"]
                        if dc in neg_stats and "FN" in neg_stats[dc]
                        else 0.0,
                        "SQC_num": pos_stats[dc]["SQC"]
                        if (scm and "SQC" in pos_stats[dc])
                        else None,
                        "SQI_num": pos_stats[dc]["SQI"]
                        if (scm and "SQI" in pos_stats[dc])
                        else None,
                    }
                )

                if scm:
                    print(
                        "%d Consistent vs. %d Inconsistent -> %.0f%%)"
                        % (
                            neg_stats[dc]["SQC"]
                            if dc in neg_stats and "SQC" in neg_stats[dc]
                            else 0,
                            neg_stats[dc]["SQI"]
                            if dc in neg_stats and "SQI" in neg_stats[dc]
                            else 0,
                            100
                            * neg_stats[dc]["SQC"]
                            / (neg_stats[dc]["SQI"] + neg_stats[dc]["SQC"])
                            if dc in neg_stats
                            and "SQC" in neg_stats[dc]
                            and "SQI" in neg_stats[dc]
                            else 0,
                        )
                    )

    return global_results_records
