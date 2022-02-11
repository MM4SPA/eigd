def get_annotator_handball_scenes(multi_annotations, annotator):
    """
    Extracts all 5 sequences for the multi-annotated matches 'ad969d' and 'e835a' for a given annotator

    Parameters
    ----------
    multi_annotations: pd.DataFrame
    annotator: str

    Returns
    -------
    List of List
        List of 10 lists for every sequence each containing two lists for meta (status) events and on-ball events
    """
    # annotations for given annotator
    single_annotations = multi_annotations[multi_annotations["annotator"] == annotator]

    # match 1: ad969d

    # TODO Improve: get all sub_df identified by (match_id, subset_id)
    m1 = single_annotations[single_annotations["match_id"] == "ad969d"]

    # sequences
    m1_seq_1 = m1[m1["subset_id"] == "00-15-00"]

    m1_seq_2 = m1[m1["subset_id"] == "00-30-00"]

    m1_seq_3 = m1[m1["subset_id"] == "00-43-00"]

    m1_seq_4 = m1[m1["subset_id"] == "01-11-00"]

    m1_seq_5 = m1[m1["subset_id"] == "01-35-00"]

    # match 2: e8a35a
    m2 = single_annotations[single_annotations["match_id"] == "e8a35a"]

    m2_seq_1 = m2[m2["subset_id"] == "00-02-00"]

    m2_seq_2 = m2[m2["subset_id"] == "00-07-00"]

    m2_seq_3 = m2[m2["subset_id"] == "00-14-00"]

    m2_seq_4 = m2[m2["subset_id"] == "01-05-00"]

    m2_seq_5 = m2[m2["subset_id"] == "01-14-00"]

    # read annotations
    meta_ad_1, on_ball_ad_1 = extract_status_and_onball_events(
        m1_seq_1, 0, 8183 + 25, "active", "B"
    )
    meta_ad_2, on_ball_ad_2 = extract_status_and_onball_events(
        m1_seq_2, 0, 7692 + 25, "active", "A"
    )
    meta_ad_3, on_ball_ad_3 = extract_status_and_onball_events(
        m1_seq_3, 0, 8990 + 25, "inactive", "A"
    )
    meta_ad_4, on_ball_ad_4 = extract_status_and_onball_events(
        m1_seq_4, 0, 8947 + 25, "active", "A"
    )
    meta_ad_5, on_ball_ad_5 = extract_status_and_onball_events(
        m1_seq_5, 0, 8299 + 25, "active", "A"
    )

    meta_e8_1, on_ball_e8_1 = extract_status_and_onball_events(
        m2_seq_1, 0, 8999 + 25, "inactive", "B"
    )
    meta_e8_2, on_ball_e8_2 = extract_status_and_onball_events(
        m2_seq_2, 0, 8998 + 25, "active", "A"
    )
    meta_e8_3, on_ball_e8_3 = extract_status_and_onball_events(
        m2_seq_3, 0, 8471 + 25, "active", "B"
    )
    meta_e8_4, on_ball_e8_4 = extract_status_and_onball_events(
        m2_seq_4, 0, 8506 + 25, "inactive", "A"
    )
    meta_e8_5, on_ball_e8_5 = extract_status_and_onball_events(
        m2_seq_5, 0, 8950 + 25, "active", "B"
    )

    return [
        [meta_ad_1, on_ball_ad_1],
        [meta_ad_2, on_ball_ad_2],
        [meta_ad_3, on_ball_ad_3],
        [meta_ad_4, on_ball_ad_4],
        [meta_ad_5, on_ball_ad_5],
        [meta_e8_1, on_ball_e8_1],
        [meta_e8_2, on_ball_e8_2],
        [meta_e8_3, on_ball_e8_3],
        [meta_e8_4, on_ball_e8_4],
        [meta_e8_5, on_ball_e8_5],
    ]


def get_annotator_soccer_scenes(multi_annotations, annotator):
    """
    Extracts all 5 sequences for the multi-annotated matches 'ad969d' and 'e835a' for a given annotator

    Parameters
    ----------
    multi_annotations: pd.DataFrame
    annotator: str, int

    Returns
    -------
    List of List
        List of 10 lists for every sequence each containing two lists for meta (status) events and on-ball events
    """
    # annotations for given annotator
    single_annotations = multi_annotations[multi_annotations["annotator"] == annotator]

    # match 1: argentina vs belgium
    arg = single_annotations[single_annotations["match_id"] == "Argentina-vs-Belgium"]

    arg_seq_1 = arg[arg["subset_id"] == "19875-27375"]

    arg_seq_2 = arg[arg["subset_id"] == "32500-40000"]

    arg_seq_3 = arg[arg["subset_id"] == "91400-98900"]

    arg_seq_4 = arg[arg["subset_id"] == "118225-125725"]

    arg_seq_5 = arg[arg["subset_id"] == "138650-146150"]

    # read annotations
    # fix obvious errors during annotation -> necessary for SCM based on "game status changing event"
    meta_arg_1, on_ball_arg_1 = extract_status_and_onball_events(
        arg_seq_1, 19875, 27375, "active", "A"
    )
    meta_arg_2, on_ball_arg_2 = extract_status_and_onball_events(
        arg_seq_2, 32500, 40000, "active", "B"
    )
    meta_arg_3, on_ball_arg_3 = extract_status_and_onball_events(
        arg_seq_3, 91400, 98900, "inactive", "A"
    )
    meta_arg_4, on_ball_arg_4 = extract_status_and_onball_events(
        arg_seq_4, 118225, 125725, "active", "B"
    )
    meta_arg_5, on_ball_arg_5 = extract_status_and_onball_events(
        arg_seq_5, 138650, 146150, "inactive", "A"
    )

    bra = single_annotations[single_annotations["match_id"] == "Brazil-vs-Germany"]

    bra_seq_1 = bra[bra["subset_id"] == "14350-21850"]

    bra_seq_2 = bra[bra["subset_id"] == "49225-56725"]

    bra_seq_3 = bra[bra["subset_id"] == "60500-68000"]

    bra_seq_4 = bra[bra["subset_id"] == "106500-114000"]

    bra_seq_5 = bra[bra["subset_id"] == "139500-147000"]

    meta_bra_1, on_ball_bra_1 = extract_status_and_onball_events(
        bra_seq_1, 14350, 21850, "active", "B"
    )
    meta_bra_2, on_ball_bra_2 = extract_status_and_onball_events(
        bra_seq_2, 49225, 56725, "active", "A"
    )
    meta_bra_3, on_ball_bra_3 = extract_status_and_onball_events(
        bra_seq_3, 60500, 68000, "active", "B"
    )
    meta_bra_4, on_ball_bra_4 = extract_status_and_onball_events(
        bra_seq_4, 106500, 114000, "inactive", "B"
    )
    meta_bra_5, on_ball_bra_5 = extract_status_and_onball_events(
        bra_seq_5, 139500, 147000, "inactive", "A"
    )

    return [
        [meta_arg_1, on_ball_arg_1],
        [meta_arg_2, on_ball_arg_2],
        [meta_arg_3, on_ball_arg_3],
        [meta_arg_4, on_ball_arg_4],
        [meta_arg_5, on_ball_arg_5],
        [meta_bra_1, on_ball_bra_1],
        [meta_bra_2, on_ball_bra_2],
        [meta_bra_3, on_ball_bra_3],
        [meta_bra_4, on_ball_bra_4],
        [meta_bra_5, on_ball_bra_5],
    ]


def extract_status_and_onball_events(
    sequence_annotation, start, end, initial_act="inactive", initial_poss="0"
):
    """
    Read the given sequence annotation and return meta (status) and on-ball events
    Parameters
    ----------
    sequence_annotation: pd.DataFrame
    start: int
        First Frame in the sequence
    end: int
        Last Frame
    initial_poss: str in {'A', 'B', '0'}
        Possession at the first frame
    initial_act: str in {'active', 'inactive'}
        Activeness of the game at the first frame

    Returns
    -------
    meta: dict
    on_ball_events: list of dict
    """

    # define possession
    possession = {"A": [], "B": [], "none": []}
    current_team = initial_poss
    last_start = start

    # read possession
    for _, annotation in sequence_annotation.iterrows():
        if "ball possession" in annotation["label_flat"]:
            possession[current_team].append([last_start, annotation["t_start"] - 1])
            if "team" in annotation["label_flat"].split(".")[-1]:
                current_team = annotation["label_flat"].split(".")[-1][-1]
            else:
                current_team = "none"
            last_start = annotation["t_start"]
    # append last sequence
    possession[current_team].append([last_start, end])

    # define activeness
    activeness = {"active": [], "inactive": []}
    current_state = initial_act
    last_start = start

    # read activeness sequence_annotation["label_flat"].unique()
    for _, annotation in sequence_annotation.iterrows():
        # referee decision pauses match
        if "referee decision" in annotation["label_flat"]:
            activeness[current_state].append([last_start, annotation["t_start"] - 1])
            current_state = "inactive"
            last_start = annotation["t_start"]

        # static ball action resumes match
        elif "static ball event" in annotation["label_flat"]:
            if current_state == "active":  # missing referees decision
                activeness["active"].append([last_start, annotation["t_start"] - 3])
                activeness["inactive"].append(
                    [annotation["t_start"] - 2, annotation["t_start"] - 1]
                )
            else:  # correct order
                activeness["inactive"].append([last_start, annotation["t_start"] - 1])
            current_state = "active"
            last_start = annotation["t_start"]

        # missing static ball action
        elif current_state == "inactive" and (
            "shot" in annotation["label_flat"]
            or "pass" in annotation["label_flat"]
            or "unintentional" in annotation["label_flat"]
            or "ball reception" in annotation["label_flat"]
        ):
            activeness["inactive"].append([last_start, annotation["t_start"] - 1])
            current_state = "active"
            last_start = annotation["t_start"]

    # append last sequence
    activeness[current_state].append([last_start, end])

    # combine possession and activeness
    active_possession = {}
    for poss_ind in possession:
        active_possession.update({poss_ind: []})
        for seq in possession[poss_ind]:
            # search for active samples
            active_samples = []
            for sample in range(seq[0], seq[1] + 1):
                active = True
                # if inactive match
                for inactive_match in activeness["inactive"]:
                    if inactive_match[0] <= sample <= inactive_match[1]:
                        active = False
                        break
                if active:
                    active_samples.append(sample)
            if len(active_samples) > 1:
                active_poss_seq = []
                start = active_samples[0]
                for i in range(1, len(active_samples)):
                    if active_samples[i] - active_samples[i - 1] > 1:
                        active_poss_seq.append([start, active_samples[i - 1]])
                        start = active_samples[i]
                    elif i == len(active_samples) - 1:
                        active_poss_seq.append([start, active_samples[i]])
                for act_seq in active_poss_seq:
                    active_possession[poss_ind].append(act_seq)

    # summarize in meta dict
    meta = {"poss": possession, "act": activeness, "act_poss": active_possession}

    # define atomic events
    on_ball_events = []

    # read atomic events
    for _, annotation in sequence_annotation.iterrows():

        # skip None events
        if "none" in annotation["label_flat"]:
            continue

        # read atomic events
        hierarchy_labels = annotation["label_flat"].split(".")[1:]
        descriptor_labels = []
        # transform labels
        for j, label in enumerate(hierarchy_labels):
            if "intentional" in label:
                descriptor = label + " release"
            elif label in ["successful", "unsuccessful"]:
                descriptor = hierarchy_labels[j - 1] + " " + label
            elif "untouched" in label:
                descriptor = hierarchy_labels[j - 2] + " " + "successful untouched"
            elif "deflected" in label:
                descriptor = hierarchy_labels[j - 2] + " " + "successful deflected"
            elif label in ["intercepted", "off target", "blocked/intercepted"]:
                descriptor = hierarchy_labels[j - 2] + " " + label
            # elif label == "self induced":
            #     descriptor = "other"
            # elif label in ["referee decision", "static ball event"]:
            #     descriptor_labels.append("game status event")
            #    descriptor = label
            elif label == "other":
                descriptor = hierarchy_labels[j - 1] + " " + label
            else:
                descriptor = label
            descriptor_labels.append(descriptor)

        # create dict
        hierarchy_path = {}
        for j, key in enumerate(reversed(descriptor_labels)):
            if not j:
                hierarchy_path = key
            else:
                hierarchy_path = {key: hierarchy_path}
        event = {"time": annotation["t_start"], "action": hierarchy_path}
        on_ball_events.append(event)

    return meta, on_ball_events
