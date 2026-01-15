import json
import logging
from typing import Dict

from google.genai import errors

from dify_plugin.errors.model import (
    InvokeAuthorizationError,
    InvokeBadRequestError,
    InvokeConnectionError,
    InvokeError,
    InvokeRateLimitError,
    InvokeServerUnavailableError,
)


class _CommonGemini:
    @staticmethod
    def _parse_custom_headers(credentials: dict) -> Dict[str, str]:
        """
        Parse custom headers from credentials

        :param credentials: model credentials
        :return: dictionary of custom headers
        """
        custom_headers = {}
        if "custom_headers" in credentials and credentials["custom_headers"]:
            try:
                custom_headers = json.loads(credentials["custom_headers"])
                if not isinstance(custom_headers, dict):
                    logging.warning("custom_headers must be a JSON object, ignoring")
                    custom_headers = {}
            except json.JSONDecodeError:
                logging.warning("Failed to parse custom_headers as JSON, ignoring")
        return custom_headers

    @property
    def _invoke_error_mapping(self) -> dict[type[InvokeError], list[type[Exception]]]:
        """
        Map model invoke error to unified error
        """
        return {
            InvokeConnectionError: [errors.APIError],
            InvokeServerUnavailableError: [errors.ServerError],
            InvokeRateLimitError: [],
            InvokeAuthorizationError: [],
            InvokeBadRequestError: [
                errors.ClientError,
                errors.UnknownFunctionCallArgumentError,
                errors.UnsupportedFunctionError,
                errors.FunctionInvocationError,
            ],
        }
