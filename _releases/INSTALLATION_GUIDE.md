# Gemini Plugin with Custom Headers - Installation Guide

## Overview

This is a modified version of the Dify Gemini plugin that adds support for custom HTTP headers. This allows you to add any custom headers to Gemini API requests through the Dify model configuration interface.

## Features

- **Custom Headers Support**: Add custom HTTP headers to all Gemini API requests
- **JSON Configuration**: Configure headers using simple JSON format in the Dify UI
- **Supports both LLM and Text Embedding models**

## Installation

### Method 1: Install via Dify Marketplace (Recommended when available)

1. Open your Dify instance
2. Navigate to **Settings** → **Plugins**
3. Click **Install Plugin**
4. Upload the `gemini-custom-headers.difypkg` file
5. Click **Install**

### Method 2: Manual Installation

1. Download the `gemini-custom-headers.difypkg` file
2. In your Dify instance, go to **Settings** → **Plugins**
3. Click **Install from file**
4. Select the downloaded `.difypkg` file
5. Wait for the installation to complete

## Configuration

After installation, configure the Gemini model provider:

1. Go to **Settings** → **Model Providers**
2. Find and select **Gemini**
3. Enter your configuration:
   - **API Key**: Your Google Gemini API key (required)
   - **Base URL**: Custom base URL (optional)
   - **Files URL**: Local files URL prefix (optional)
   - **Custom Headers**: Custom HTTP headers in JSON format (optional)

### Custom Headers Format

Enter custom headers as a JSON object:

```json
{
  "X-Custom-Header": "your-value",
  "X-API-Version": "v1",
  "X-Request-Source": "dify"
}
```

**Example use cases:**
- Adding custom authentication headers
- Setting API version headers
- Adding tracking or correlation IDs
- Including custom metadata in requests

## Changes from Original Plugin

This plugin adds the following enhancements to the official Gemini plugin:

1. **New credential field** in `provider/google.yaml`:
   - `custom_headers`: JSON-formatted string for custom HTTP headers

2. **Enhanced client initialization** in both LLM and text embedding models:
   - Parses custom headers from credentials
   - Applies headers to all HTTP requests via `HttpOptions`

3. **Shared utility method** in `common_gemini.py`:
   - `_parse_custom_headers()`: Safely parses and validates custom header JSON

## Technical Details

### Modified Files

- `models/gemini/provider/google.yaml`: Added custom_headers field
- `models/gemini/models/common_gemini.py`: Added header parsing logic
- `models/gemini/models/llm/llm.py`: Integrated custom headers in LLM client
- `models/gemini/models/text_embedding/text_embedding.py`: Integrated custom headers in embedding client

### Error Handling

The plugin includes robust error handling:
- Invalid JSON in custom headers will be logged and ignored
- Non-dictionary JSON values will be rejected
- The plugin will continue to work normally if custom headers are not provided

## Compatibility

- **Minimum Dify Version**: 1.4.0
- **Plugin Version**: 0.7.4 (based on official Gemini plugin)
- **Supported Model Types**:
  - Large Language Models (LLM)
  - Text Embedding

## Support

For issues or questions:
- Check the [Dify Documentation](https://docs.dify.ai)
- Visit the [Dify GitHub Repository](https://github.com/langgenius/dify)

## License

This plugin is based on the official Dify Gemini plugin and follows the same license terms.
