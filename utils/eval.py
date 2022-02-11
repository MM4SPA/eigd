import pandas as pd
import numpy as np

# define event tolerances
event_tolerances = {
    # level 0
    "game status changing event": 75,
    "individual ball event": 75,
    # level 1
    "static ball event": 75,
    "referee decision": 75,
    # level 2
    "ball reception": 5,
    "ball release": 5,
    # level 3
    "intentional release": 5,
    "unintentional release": 25,
    # level 4
    "shot": 5,
    "pass": 5,
    "successful interference": 25,
    "self induced": 25,
    # level 5+
    "pass successful": 5,
    "pass intercepted": 5,
    "after foul": 25,
    "ball in field": 25,
    "foul": 75,
    "ball out of field": 75,
    "goal": 75,
    "pass successful deflected": 5,
    "pass successful untouched": 5,
    "pass off target": 5,
    "referee decision other": 25,
}


def _convert2int(_df, cols: list):
    for col in cols:
        _df[col] = _df[col].astype(np.integer)
    return _df


def result_records2df(global_results_records):
    df_results = pd.DataFrame.from_records(global_results_records)
    df_results["precision"] = 100 * df_results["precision"]  # to percentage
    df_results["recall"] = 100 * df_results["recall"]  # to percentage
    df_results.set_index(["event_type", "method"]).sort_values(
        by=["hierarchy_level", "method"]
    )
    return df_results


def format_nnm_output(df):
    df_results_nnm = df.loc[df.method == "NNM"][
        ["event_type", "hierarchy_level", "precision", "recall", "TP", "FP", "FN",]
    ]
    # formatting
    # The lack of NaN rep in integer columns is a pandas "gotcha": https://pandas.pydata.org/pandas-docs/stable/user_guide/gotchas.html#support-for-integer-na
    # -> replace NaN with zero and perform integer conversion
    df_results_nnm = _convert2int(df_results_nnm.fillna(0.0), ["TP", "FP", "FN"])
    df_results_nnm = df_results_nnm.set_index(["hierarchy_level", "event_type"])
    return df_results_nnm


def format_scm_output(df):
    df_results_scm = df.loc[df.method == "SCM"][
        ["event_type", "hierarchy_level", "precision", "recall", "TP", "FP", "FN",]
        + ["SQC_num", "SQI_num"]
    ]
    df_results_scm = _convert2int(
        df_results_scm.fillna(0.0), ["TP", "FP", "FN", "SQC_num", "SQI_num"]
    )

    # fraction of consistent sequencies in percentage
    df_results_scm["SQC_frac"] = (
        df_results_scm["SQC_num"]
        / (df_results_scm["SQC_num"] + df_results_scm["SQI_num"])
        * 100
    )

    df_results_scm = df_results_scm.set_index(["hierarchy_level", "event_type"])
    return df_results_scm


def stack_df_nnm_scm(df_results_nnm, df_results_scm):
    df_nnm_scm = pd.concat(
        [df_results_nnm, df_results_scm],
        keys=["hierarchy_level", "event_type"],
        axis=1,
    )

    # dirty column renaming
    df_nnm_scm.columns = pd.MultiIndex.from_tuples(
        [
            ("NNM", *list(mcol[1:]))
            if mcol[0] == "hierarchy_level"
            else ("SCM", *list(mcol[1:]))
            for mcol in df_nnm_scm.columns.values
        ]
    )
    return df_nnm_scm

