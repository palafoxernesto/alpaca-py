from datetime import datetime
from typing import Union, Optional, List

from alpaca.common import NonEmptyRequest
from alpaca.data import DataFeed


class BaseQuotesRequest(NonEmptyRequest):
    """
    A base request object for retrieving quote data for securities. You most likely should not use this directly and instead
    use the asset class specific request objects.

    Attributes:
        symbol_or_symbols (Union[str, List[str]]): The ticker identifier or list of ticker identifiers.
        start (Optional[datetime]): The beginning of the time interval for desired data.
        end (Optional[datetime]): The end of the time interval for desired data.
        limit (Optional[int]): Upper limit of number of data points to return.
    """

    symbol_or_symbols: Union[str, List[str]]
    start: Optional[Union[datetime, str]]
    end: Optional[Union[datetime, str]]
    limit: Optional[int]


class StockQuotesRequest(BaseQuotesRequest):
    """
    This request class is used to submit a request for stock quote data.

    See BaseQuotesRequest for more information on available parameters.

    Attributes:
        feed (Optional[DataFeed]): The stock data feed to retrieve from.
    """

    feed: Optional[DataFeed]


class CryptoQuotesRequest(BaseQuotesRequest):
    """
    This request class is used to submit a request for crypto quote data.

    See BaseQuotesRequest for more information on available parameters.
    """

    pass
