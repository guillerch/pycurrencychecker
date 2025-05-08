import pytest
from unittest.mock import patch, Mock
from pycurrencychecker.pycurrencychecker import CurrencyChecker

@pytest.fixture
def currency_checker():
    return CurrencyChecker(api_key="test_api_key")

@patch("pycurrencychecker.pycurrencychecker.requests.get")
def test_get_currency_list(mock_get, currency_checker):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"currencies": {"USD": "United States Dollar", "EUR": "Euro"}}
    mock_get.return_value = mock_response

    result = currency_checker.get_currency_list()
    assert result == {"currencies": {"USD": "United States Dollar", "EUR": "Euro"}}
    mock_get.assert_called_once_with(f"{currency_checker.ENDPOINTS['list']}?access_key=test_api_key")

@patch("pycurrencychecker.pycurrencychecker.requests.get")
def test_get_currency_rate(mock_get, currency_checker):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"quotes": {"USDEUR": 0.85, "USDGBP": 0.75}}
    mock_get.return_value = mock_response

    result = currency_checker.get_currency_rate()
    assert result == {"quotes": {"USDEUR": 0.85, "USDGBP": 0.75}}
    mock_get.assert_called_once_with(
        f"{currency_checker.ENDPOINTS['live']}?access_key=test_api_key&source=USD&currencies=EUR,GBP,JPY,CAD,AUD,CHF,CNY,SEK,NZD,BOB"
    )

@patch("pycurrencychecker.pycurrencychecker.requests.get")
def test_get_currency_historical(mock_get, currency_checker):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"historical": True, "quotes": {"USDEUR": 0.84}}
    mock_get.return_value = mock_response

    result = currency_checker.get_currency_historical(date="2023-10-01")
    assert result == {"historical": True, "quotes": {"USDEUR": 0.84}}
    mock_get.assert_called_once_with(
        f"{currency_checker.ENDPOINTS['historical']}?access_key=test_api_key&date=2023-10-01&source=USD&currencies=EUR,GBP,JPY,CAD,AUD,CHF,CNY,SEK,NZD,BOB"
    )

@patch("pycurrencychecker.pycurrencychecker.requests.get")
def test_get_currency_convert(mock_get, currency_checker):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"success": True, "result": 0.85}
    mock_get.return_value = mock_response

    result = currency_checker.get_currency_convert(from_currency="USD", to_currency="EUR", amount=1)
    assert result == {"success": True, "result": 0.85}
    mock_get.assert_called_once_with(
        f"{currency_checker.ENDPOINTS['convert']}?access_key=test_api_key&from=USD&to=EUR&amount=1&date=2023-10-01"
    )

@patch("pycurrencychecker.pycurrencychecker.requests.get")
def test_get_currency_time_frame(mock_get, currency_checker):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"timeframe": True, "quotes": {"USDEUR": {"2023-10-01": 0.84, "2023-10-02": 0.85}}}
    mock_get.return_value = mock_response

    result = currency_checker.get_currency_time_frame(start_date="2023-10-01", end_date="2023-10-02")
    assert result == {"timeframe": True, "quotes": {"USDEUR": {"2023-10-01": 0.84, "2023-10-02": 0.85}}}
    mock_get.assert_called_once_with(
        f"{currency_checker.ENDPOINTS['time-frame']}?access_key=test_api_key&start_date=2023-10-01&end_date=2023-10-02&source=USD&currencies=EUR,GBP,JPY,CAD,AUD,CHF,CNY,SEK,NZD,BOB"
    )

@patch("pycurrencychecker.pycurrencychecker.requests.get")
def test_get_currency_change(mock_get, currency_checker):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"change": True, "quotes": {"USDEUR": {"start_rate": 0.84, "end_rate": 0.85}}}
    mock_get.return_value = mock_response

    result = currency_checker.get_currency_change(start_date="2023-10-01", end_date="2023-10-02")
    assert result == {"change": True, "quotes": {"USDEUR": {"start_rate": 0.84, "end_rate": 0.85}}}
    mock_get.assert_called_once_with(
        f"{currency_checker.ENDPOINTS['change']}?access_key=test_api_key&start_date=2023-10-01&end_date=2023-10-02&source=USD&currencies=EUR,GBP,JPY,CAD,AUD,CHF,CNY,SEK,NZD,BOB"
    )