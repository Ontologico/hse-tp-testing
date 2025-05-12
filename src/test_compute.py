from unittest.mock import patch

from src.compute import long_function


def test_long_function():
    with patch("time.sleep", return_value=None) as mock_sleep:
        result = long_function()

    assert result == "hey"
    mock_sleep.assert_called_once()  # Дополнительная проверка, что time.sleep был вызван
    mock_sleep.assert_called_with(10**9)  # Можно даже проверить, с какими аргументами
