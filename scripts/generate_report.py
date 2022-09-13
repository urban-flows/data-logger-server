from pathlib import Path
from datetime import date, timedelta, datetime
import re
import os
import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p",
                        "--data_path",
                        help="path to the parent of the year directory of the data")
    parser.add_argument("-r",
                        "--report_path",
                        help="path where report text file will be created and saved",
                        default="."
                        )
    return parser.parse_args()


if __name__ == "__main__":

    args = get_args()
    date = date.today()

    current_day = date.strftime("%d")
    current_month = date.strftime("%m")
    current_year = date.strftime("%Y")

    data_path = Path(str(args.p))

    if not data_path.is_dir():
        raise FileNotFoundError('No directory exists at the given path')

    current_date_path = data_path / current_year / current_month / current_day

    paths = list()
    for single_date in (date - timedelta(n) for n in range(7)):
        current_path = data_path / single_date.strftime("%Y") / single_date.strftime("%m") / single_date.strftime("%d")
        paths += Path(current_path).glob('*')

    files = [x for x in paths if x.is_file()]
    station_id_filter = re.compile("0{4}[0-9]{6}")

    station_ids = [re.findall(station_id_filter, str(file))[0] for file in files]
    unique_stations = set(station_ids)
    number_stations = len(unique_stations)

    report_name = 'report_' + current_year + current_month + current_day
    report_header = 'Data Logger Server Report ' + current_day + "_" + current_month + "_" + current_year + os.linesep
    report_stations = 'Number of stations reported within the week: ' + str(number_stations) + os.linesep
    report_list = 'List of stations: ' + str(unique_stations) + os.linesep

    if Path(args.r).is_dir():
        with open('reports/' + report_name, 'w') as f:
            f.write(report_header + report_stations + report_list)
    else:
        raise FileNotFoundError(f"No directory exists at the location specified: {args.r}")

