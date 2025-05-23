import time
import argparse

from sdv.datasets.demo import download_demo

from utilities import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This program will generate synthetic data for csv files using SDV."
    )
    parser.add_argument(
        "--folder_path",
        required=False,
        type=str,
        help="Directory to a folder with one csv file. If none is provided, a demo dataset will be used.",
    )
    parser.add_argument(
        "--path_to_metadata",
        required=False,
        type=str,
        help="Path to metadata file. If none is provided, the metadata will be autodetected.",
    )
    parser.add_argument(
        "--num_rows",
        required=False,
        type=int,
        default=500,
        help="Number of rows to generate.",
    )
    parser.add_argument(
        "--save_path",
        required=False,
        type=str,
        help='Path to save the generated synthetic data (example="synthetic_data_sdv.csv"). If none is provided, the generated synthetic data will not be saved.',
    )
    parser.add_argument(
        "--constraint_path",
        required=False,
        type=str,
        help='Path to custom constraints (example="custom_constraints.json"). If none is provided, constraints will not be applied.',
    )

    args = parser.parse_args()

    if args.folder_path:
        data, count = read_csv_data(args.folder_path)
        metadata = autodetect_metadata(data)
        # if count > 1:
        #     raise Exception("Please upload only one table.")
    else:
        data, metadata = download_demo(
            modality="multi_table", dataset_name="fake_hotel_guests"
        )

    if args.path_to_metadata:
        metadata = Metadata.load_from_json(args.path_to_metadata)
    else:
        metadata = autodetect_metadata(data)

    metadata.save_to_json(filepath="metadata.json")

