# -*- coding: utf-8 -*-
"""Functions to load and write datasets."""

__all__ = [
    "load_airline",
    "load_arrow_head",
    "load_gunpoint",
    "load_basic_motions",
    "load_osuleaf",
    "load_italy_power_demand",
    "load_japanese_vowels",
    "load_plaid",
    "load_longley",
    "load_lynx",
    "load_shampoo_sales",
    "load_UCR_UEA_dataset",
    "load_unit_test",
    "load_uschange",
    "load_PBS_dataset",
    "load_japanese_vowels",
    "load_gun_point_segmentation",
    "load_electric_devices_segmentation",
    "load_acsf1",
    "load_macroeconomic",
    "generate_example_long_table",
    "load_from_arff_to_dataframe",
    "load_from_long_to_dataframe",
    "load_from_tsfile",
    "load_from_tsfile_to_dataframe",
    "load_from_ucr_tsv_to_dataframe",
    "make_multi_index_dataframe",
    "write_dataframe_to_tsfile",
    "write_ndarray_to_tsfile",
    "write_results_to_uea_format",
    "write_tabular_transformation_to_arff",
    "load_tsf_to_dataframe",
    "load_unit_test_tsf",
]

from sktime._contrib.datasets._data_io import (
    generate_example_long_table,
    load_from_arff_to_dataframe,
    load_from_long_to_dataframe,
    load_from_tsfile,
    load_from_tsfile_to_dataframe,
    load_from_ucr_tsv_to_dataframe,
    load_tsf_to_dataframe,
    make_multi_index_dataframe,
    write_dataframe_to_tsfile,
    write_ndarray_to_tsfile,
    write_results_to_uea_format,
    write_tabular_transformation_to_arff,
)
from sktime._contrib.datasets._single_problem_loaders import (
    load_acsf1,
    load_airline,
    load_arrow_head,
    load_basic_motions,
    load_electric_devices_segmentation,
    load_gun_point_segmentation,
    load_gunpoint,
    load_italy_power_demand,
    load_japanese_vowels,
    load_longley,
    load_lynx,
    load_macroeconomic,
    load_osuleaf,
    load_PBS_dataset,
    load_plaid,
    load_shampoo_sales,
    load_UCR_UEA_dataset,
    load_unit_test,
    load_unit_test_tsf,
    load_uschange,
)
