import unittest
from unittest.mock import Mock, patch

from src.utils import financial_transactions
from src.utils_csv_excel import distributor_file


class TestDistributorFile(unittest.TestCase):


@patch("distributor.csv.reader")
def test_csv_file(self, mock_csv_reader):
    mock_csv_reader.return_value = [["header1", "header2"], ["data1", "data2"]]
    result = distributor_file("test.csv")
    self.assertEqual(result, [["header1", "header2"], ["data1", "data2"]])

@patch("distributor.pd.read_excel")
def test_xlsx_file(self, mock_read_excel):
    mock_read_excel.return_value = "Mock excel data"
    result = distributor_file("test.xlsx")
    self.assertEqual(result, "Mock excel data")
@patch("distributor.financial_transactions")
def test_json_file(self, mock_financial_transactions):
        result = distributor_file("test.json")
        mock_financial_transactions.assert_called_once_with("test.json")

@patch("distributor.datetime")
@patch("distributor.transaction_log")
def test_exception_handling(self, mock_transaction_log, mock_datetime):
    mock_datetime.datetime.now.side_effect = [Mock(), Mock()]
    mock_transaction_log.info = Mock()
    mock_open = Mock()
    mock_open.side_effect = Exception("File not found")

    with patch("builtins.open", mock_open):
            result = distributor_file("test.txt")
            mock_transaction_log.error.assert_called_once_with("Error : File not found")
            self.assertEqual(result, [])

# @patch("distributor.datetime")
# @patch("distributor.transaction_log")
# def test_finally_block(self, mock_transaction_log, mock_datetime):
#     mock_datetime.datetime.now.side_effect = [Mock(), Mock()]
#     mock_transaction_log.debug = Mock()
#
#     assert result = distributor_file("test.xlsx")
#
#     mock_transaction_log.debug.assert_called_once_with("The function worked in 0:00:00 second")
