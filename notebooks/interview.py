from pprint import pprint

import numpy as np
import pandas as pd


def random_matrix() -> np.ndarray:
    shape = (5, 3)
    return np.random.random_integers(
        low=1,
        high=10,
        size=shape,
    )


def max_by_min(array: np.ndarray) -> np.ndarray:
    min_values = np.min(array, axis=0)
    max_values = np.max(array, axis=0)
    return max_values / min_values


def max_by_min_apply(array: np.ndarray) -> np.ndarray:
    return np.apply_along_axis(
        lambda column: np.max(column) / np.min(column),
        axis=0,
        arr=array,
    )


def create_city_company() -> pd.DataFrame:
    # city company dataframe
    cities = [
        "Kyiv",
        "Kyiv",
        "Odesa",
        "Kharkiv",
        "Lviv",
    ]
    companies = [
        "Luxoft",
        "GlobalLogic",
        "Luxoft",
        "EPAM",
        "Luxoft",
    ]
    return pd.DataFrame(
        {
            "city": cities,
            "company": companies,
        }
    )


def company_city_presence_matrix(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(
        index="city",
        columns="company",
        aggfunc=len,
        fill_value=0,
    )


if __name__ == "__main__":
    # print("testing")
    # matrix = random_matrix()
    # pprint(matrix)
    # pprint(max_by_min(matrix))
    # pprint(max_by_min_apply(matrix))
    df = create_city_company()
    pprint(df)
    matrix = company_city_presence_matrix(df)
    pprint(matrix)
