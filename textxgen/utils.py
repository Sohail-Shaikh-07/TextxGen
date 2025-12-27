# textxgen/utils.py

import logging
from typing import Any, Dict, List
from .exceptions import InvalidInputError


def validate_input(data: Any, expected_type: type, field_name: str) -> None:
    """
    Validates input data against an expected type.

    Args:
        data (Any): The input data to validate.
        expected_type (type): The expected type of the data.
        field_name (str): The name of the field being validated.

    Raises:
        InvalidInputError: If the data does not match the expected type.
    """
    if not isinstance(data, expected_type):
        raise InvalidInputError(
            f"'{field_name}' must be of type {expected_type.__name__}."
        )


def setup_logger(name: str, log_level: int = logging.INFO) -> logging.Logger:
    """
    Sets up and configures a logger.

    Args:
        name (str): Name of the logger.
        log_level (int): Logging level (default: logging.INFO).

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Create a console handler
    handler = logging.StreamHandler()
    handler.setLevel(log_level)

    # Create a formatter and add it to the handler
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger


def format_api_response(response: Dict[str, Any]) -> str:
    """
    Formats the API response into a readable string.

    Args:
        response (Dict[str, Any]): The API response.

    Returns:
        str: Formatted response string.
    """
    if "choices" in response:
        return response["choices"][0]["message"]["content"]
    elif "completions" in response:
        return response["completions"][0]["text"]
    else:
        return str(response)
