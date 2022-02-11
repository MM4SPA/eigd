def create_hierarchy_descriptions(event):
    """
    Create descriptions according to the taxonomy_old hierarchy

    Parameters
    ----------
    event: dict

    Returns
    -------
    List of str or str
    """
    prediction_descriptions = []
    if isinstance(event["action"], dict):
        # first lvl
        first_lvl = list(event["action"].keys())[0]
        prediction_descriptions.append(first_lvl)
        # second highest
        if isinstance(event["action"][first_lvl], dict):
            second_lvl = list(event["action"][first_lvl].keys())[0]
            prediction_descriptions.append(second_lvl)
            # third highest
            if isinstance(event["action"][first_lvl][second_lvl], dict):
                third_lvl = list(event["action"][first_lvl][second_lvl].keys())[0]
                prediction_descriptions.append(third_lvl)
                # fourth highest
                if isinstance(event["action"][first_lvl][second_lvl][third_lvl], dict):
                    fourth_lvl = list(
                        event["action"][first_lvl][second_lvl][third_lvl].keys()
                    )[0]
                    prediction_descriptions.append(fourth_lvl)
                    if isinstance(
                        event["action"][first_lvl][second_lvl][third_lvl][fourth_lvl],
                        dict,
                    ):
                        # fifth highest
                        fifth_lvl = list(
                            event["action"][first_lvl][second_lvl][third_lvl][
                                fourth_lvl
                            ].keys()
                        )[0]
                        prediction_descriptions.append(fifth_lvl)
                        if isinstance(
                            event["action"][first_lvl][second_lvl][third_lvl][
                                fourth_lvl
                            ][fifth_lvl],
                            dict,
                        ):
                            # sixth highest
                            sixth_lvl = event["action"][first_lvl][second_lvl][
                                third_lvl
                            ][fourth_lvl][fifth_lvl]
                            prediction_descriptions.append(sixth_lvl)
                        else:
                            prediction_descriptions.append(
                                event["action"][first_lvl][second_lvl][third_lvl][
                                    fourth_lvl
                                ][fifth_lvl]
                            )
                    else:
                        prediction_descriptions.append(
                            event["action"][first_lvl][second_lvl][third_lvl][
                                fourth_lvl
                            ]
                        )
                else:
                    prediction_descriptions.append(
                        event["action"][first_lvl][second_lvl][third_lvl]
                    )
            else:
                prediction_descriptions.append(event["action"][first_lvl][second_lvl])
        else:
            prediction_descriptions.append(event["action"][first_lvl])
    else:
        prediction_descriptions.append(event["action"])
    return prediction_descriptions
