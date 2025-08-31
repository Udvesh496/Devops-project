# Configuration file for Currency Converter
# Easy to modify for different currencies or API endpoints

# API Configuration
API_BASE_URL = "https://open.er-api.com/v6/latest"
BASE_CURRENCY = "USD"
TARGET_CURRENCY = "INR"

# App Configuration
APP_TITLE = "💱 Currency Converter"
APP_ICON = "💱"
PAGE_LAYOUT = "wide"

# UI Configuration
DEFAULT_AMOUNT = 100.0
MIN_AMOUNT = 0.01
AMOUNT_STEP = 0.01
DECIMAL_PLACES = 2
RATE_DECIMAL_PLACES = 4

# Timeout Configuration
API_TIMEOUT = 10  # seconds

# Error Messages
ERROR_MESSAGES = {
    "network": "Network error: {error}",
    "api": "API error: {error}",
    "json": "Invalid response from API: {error}",
    "format": "Unexpected API response format: {error}",
    "general": "Unexpected error: {error}"
}

# Success Messages
SUCCESS_MESSAGES = {
    "conversion": "✅ Conversion successful!",
    "rate_info": "💡 Current Exchange Rate: 1 USD = {rate:.4f} INR"
}

# Loading Messages
LOADING_MESSAGES = {
    "fetching_rates": "Fetching live exchange rates..."
}
