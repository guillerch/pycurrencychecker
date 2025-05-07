import pytest
import requests
from unittest.mock import patch
from pycurrencychecker.utils.urls import ENDPOINTS

from pycurrencychecker.pycurrencychecker import (
    get_currency_list,
    get_currency_rate,
    get_currency_historical,
    get_currency_convert,
    get_currency_time_frame,
    get_currency_change,
)
BASE_URL = "https://api.exchangerate.host"

# Mock data for testing
mock_endpoints = {
    "list": f"{BASE_URL}/list",
    "live": f"{BASE_URL}/live",
    "historical": f"{BASE_URL}/historical",
    "convert": f"{BASE_URL}/convert",
    "timeframe": f"{BASE_URL}/timeframe",
    "change": f"{BASE_URL}/change",
}

mock_response = {"success": True, "data": "mocked_data"}

@pytest.fixture
def mock_endpoints_fixture(monkeypatch):
    monkeypatch.setattr("pycurrencychecker.utils.urls.ENDPOINTS", mock_endpoints)

@patch("requests.get")
def test_get_currency_list(mock_get, mock_endpoints_fixture):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response
    token = "test_token"
    result = get_currency_list(token)
    assert result == mock_response
    mock_get.assert_called_once_with(f"{mock_endpoints['list']}?access_key={token}")

@patch("requests.get")
def test_get_currency_rate(mock_get, mock_endpoints_fixture):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response
    token = "test_token"
    result = get_currency_rate(token, source="USD", currencies="EUR,GBP")
    assert result == mock_response
    mock_get.assert_called_once_with(
        f"{mock_endpoints['live']}?access_key={token}&source=USD&currencies=EUR,GBP"
    )

@patch("requests.get")
def test_get_currency_historical(mock_get, mock_endpoints_fixture):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response
    token = "test_token"
    result = get_currency_historical(token, date="2023-10-01", source="USD", currencies="EUR,GBP")
    assert result == mock_response
    mock_get.assert_called_once_with(
        f"{mock_endpoints['historical']}?access_key={token}&date=2023-10-01&source=USD&currencies=EUR,GBP"
    )

@patch("requests.get")
def test_get_currency_convert(mock_get, mock_endpoints_fixture):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response
    token = "test_token"
    result = get_currency_convert(token, from_currency="USD", to_currency="EUR", amount=100, date="2023-10-01")
    assert result == mock_response
    mock_get.assert_called_once_with(
        f"{mock_endpoints['convert']}?access_key={token}&from=USD&to=EUR&amount=100&date=2023-10-01"
    )

@patch("requests.get")
def test_get_currency_time_frame(mock_get, mock_endpoints_fixture):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response
    token = "test_token"
    result = get_currency_time_frame(token, start_date="2023-10-01", end_date="2023-10-31", source="USD", currencies="EUR,GBP")
    assert result == mock_response
    mock_get.assert_called_once_with(
        f"{mock_endpoints['timeframe']}?access_key={token}&start_date=2023-10-01&end_date=2023-10-31&source=USD&currencies=EUR,GBP"
    )

@patch("requests.get")
def test_get_currency_change(mock_get, mock_endpoints_fixture):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response
    token = "test_token"
    result = get_currency_change(token, start_date="2023-10-01", end_date="2023-10-31", source="USD", currencies="EUR,GBP")
    assert result == mock_response
    mock_get.assert_called_once_with(
        f"{mock_endpoints['change']}?access_key={token}&start_date=2023-10-01&end_date=2023-10-31&source=USD&currencies=EUR,GBP"
    )