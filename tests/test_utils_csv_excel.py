from unittest import TestCase, mock
from unittest.mock import patch
from main import distributor_file
import pandas as pd
import io


class TestDistributorFile(TestCase):

    @patch('builtins.open')
    @patch('csv.DictReader')
    def test_CSV_file(self, mock_dict_reader, mock_open):
        mock_dict_reader.return_value = [{'transaction_id': '1', 'amount': '100'},
                                         {'transaction_id': '2', 'amount': '200'}]
        mock_open.return_value = io.StringIO("transaction_id;amount\n1;100\n2;200\n")

        result = distributor_file('example.csv')

        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result, mock.MagicMock)

    @patch('pandas.read_excel')
    def test_XLSX_file(self, mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame({'transaction_id': [1, 2], 'amount': [100, 200]})

        result = distributor_file('example.xlsx')

        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

    @patch('utils.financial_transactions')
    def test_JSON_file(self, mock_financial_transactions):
        result = distributor_file('example.json')

        mock_financial_transactions.assert_called_once_with('example.json')
