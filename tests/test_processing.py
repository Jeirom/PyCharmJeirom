import pytest

from src.processing import *


@pytest.mark.parametrize(
    "data, state, expected",
    [
        (
            [{"state": "EXECUTED"}, {"state": "PENDING"}, {"state": "EXECUTED"}],
            "EXECUTED",
            [{"state": "EXECUTED"}, {"state": "EXECUTED"}],
        ),
        (
            [{"state": "SUCCESS"}, {"state": "PENDING"}, {"state": "SUCCESS"}],
            "SUCCESS",
            [{"state": "SUCCESS"}, {"state": "SUCCESS"}],
        ),
        (
            [{"state": "FAILED"}, {"state": "PENDING"}, {"state": "FAILED"}],
            "FAILED",
            [{"state": "FAILED"}, {"state": "FAILED"}],
        ),
    ],
)
def test_filter_by_state(data, state, expected):
    assert filter_by_state(data, state) == expected


def test_sort_by_date_asc(mock_list_of_dicts):
    sorted_list = sort_by_date(mock_list_of_dicts, reverse=False)
    assert sorted_list == [
        {"date": "2021-12-31"},
        {"date": "2022-01-01"},
        {"date": "2022-01-02"},
        {"date": "2022-01-03"},
    ]


def test_sort_by_date_desc(mock_list_of_dicts):
    sorted_list = sort_by_date(mock_list_of_dicts)
    assert sorted_list == [
        {"date": "2022-01-03"},
        {"date": "2022-01-02"},
        {"date": "2022-01-01"},
        {"date": "2021-12-31"},
    ]
