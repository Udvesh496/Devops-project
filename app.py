import streamlit as st
import requests
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Currency Converter - Multi Currency",
    page_icon="💱",
    layout="wide"
)

# Define supported currencies with symbols
SUPPORTED_CURRENCIES = {
    "USD": {"name": "US Dollar", "symbol": "$"},
    "INR": {"name": "Indian Rupee", "symbol": "₹"},
    "EUR": {"name": "Euro", "symbol": "€"},
    "GBP": {"name": "British Pound", "symbol": "£"},
    "JPY": {"name": "Japanese Yen", "symbol": "¥"},
    "AUD": {"name": "Australian Dollar", "symbol": "A$"},
    "CAD": {"name": "Canadian Dollar", "symbol": "C$"},
    "CHF": {"name": "Swiss Franc", "symbol": "CHF"},
    "CNY": {"name": "Chinese Yuan", "symbol": "¥"},
    "SGD": {"name": "Singapore Dollar", "symbol": "S$"}
}

def get_exchange_rates():
    """
    Fetch live exchange rates from the API for all supported currencies
    Returns: tuple (success: bool, rates: dict, error_message: str)
    """
    try:
        # API endpoint for USD to all currencies conversion
        api_url = "https://open.er-api.com/v6/latest/USD"
        
        # Make API request with timeout
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse JSON response
        data = response.json()
        
        # Extract rates for supported currencies
        rates = {}
        for currency in SUPPORTED_CURRENCIES.keys():
            if currency in data['rates']:
                rates[currency] = data['rates'][currency]
            else:
                # If currency not found, skip it
                continue
        
        if not rates:
            return False, {}, "No supported currencies found in API response"
        
        return True, rates, ""
        
    except requests.exceptions.RequestException as e:
        return False, {}, f"Network error: {str(e)}"
    except json.JSONDecodeError as e:
        return False, {}, f"Invalid response from API: {str(e)}"
    except KeyError as e:
        return False, {}, f"Unexpected API response format: {str(e)}"
    except Exception as e:
        return False, {}, f"Unexpected error: {str(e)}"

def get_exchange_rate():
    """
    Fetch live exchange rate from the API (kept for backward compatibility)
    Returns: tuple (success: bool, rate: float, error_message: str)
    """
    try:
        # API endpoint for USD to INR conversion
        api_url = "https://open.er-api.com/v6/latest/USD"
        
        # Make API request with timeout
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse JSON response
        data = response.json()
        
        # Extract INR rate (USD to INR)
        inr_rate = data['rates']['INR']
        
        return True, inr_rate, ""
        
    except requests.exceptions.RequestException as e:
        return False, 0, f"Network error: {str(e)}"
    except json.JSONDecodeError as e:
        return False, 0, f"Invalid response from API: {str(e)}"
    except KeyError as e:
        return False, 0, f"Unexpected API response format: {str(e)}"
    except Exception as e:
        return False, 0, f"Unexpected error: {str(e)}"

def convert_currency_multi(amount, from_currency, to_currency, rates):
    """
    Convert currency between any two supported currencies
    Args:
        amount: float - amount to convert
        from_currency: str - source currency code
        to_currency: str - target currency code
        rates: dict - exchange rates from USD
    Returns: float - converted amount
    """
    if from_currency == to_currency:
        return amount
    
    if from_currency == "USD":
        # Converting from USD to another currency
        return amount * rates[to_currency]
    elif to_currency == "USD":
        # Converting from another currency to USD
        return amount / rates[from_currency]
    else:
        # Converting between two non-USD currencies
        # First convert to USD, then to target currency
        usd_amount = amount / rates[from_currency]
        return usd_amount * rates[to_currency]

def convert_currency(amount, conversion_type, exchange_rate):
    """
    Convert currency based on type and exchange rate (kept for backward compatibility)
    Args:
        amount: float - amount to convert
        conversion_type: str - "INR_to_USD" or "USD_to_INR"
        exchange_rate: float - USD to INR rate
    Returns: float - converted amount
    """
    if conversion_type == "INR_to_USD":
        # Convert INR to USD (divide by rate)
        return amount / exchange_rate
    else:
        # Convert USD to INR (multiply by rate)
        return amount * exchange_rate

def get_currency_symbol(currency_code):
    """Get currency symbol for display"""
    return SUPPORTED_CURRENCIES.get(currency_code, {}).get("symbol", currency_code)

def get_currency_name(currency_code):
    """Get full currency name for display"""
    return SUPPORTED_CURRENCIES.get(currency_code, {}).get("name", currency_code)

def main():
    """Main application function"""
    
    # Header section
    st.title("💱 Multi-Currency Converter")
    st.markdown("**Convert between multiple currencies using live exchange rates**")
    
    # Add some spacing
    st.markdown("---")
    
    # Sidebar for additional info
    with st.sidebar:
        st.header("ℹ️ Information")
        st.markdown("""
        **How it works:**
        1. Select source currency
        2. Select target currency
        3. Enter amount
        4. Click convert
        5. Get live rates!
        
        **Data Source:** Open Exchange Rates API
        **Supported Currencies:** USD, INR, EUR, GBP, JPY, AUD, CAD, CHF, CNY, SGD
        """)
        
        # Show last update time
        if 'last_update' in st.session_state:
            st.info(f"Last updated: {st.session_state.last_update}")
    
    # Main conversion area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Currency selection
        st.subheader("🔄 Currency Selection")
        
        # Create two columns for currency dropdowns
        col_from, col_to = st.columns(2)
        
        with col_from:
            from_currency = st.selectbox(
                "From Currency:",
                options=list(SUPPORTED_CURRENCIES.keys()),
                index=list(SUPPORTED_CURRENCIES.keys()).index("INR"),  # Default to INR
                format_func=lambda x: f"{get_currency_symbol(x)} {x} - {get_currency_name(x)}"
            )
        
        with col_to:
            to_currency = st.selectbox(
                "To Currency:",
                options=list(SUPPORTED_CURRENCIES.keys()),
                index=list(SUPPORTED_CURRENCIES.keys()).index("USD"),  # Default to USD
                format_func=lambda x: f"{get_currency_symbol(x)} {x} - {get_currency_name(x)}"
            )
        
        # Amount input
        st.subheader("💰 Amount")
        amount = st.number_input(
            f"Enter amount in {get_currency_symbol(from_currency)} {from_currency}:",
            min_value=0.01,
            value=100.0,
            step=0.01,
            format="%.2f"
        )
        
        # Convert button
        if st.button("🚀 Convert", type="primary", use_container_width=True):
            # Show loading spinner
            with st.spinner("Fetching live exchange rates..."):
                # Get exchange rates
                success, rates, error = get_exchange_rates()
                
                if success:
                    # Check if both currencies are supported
                    if from_currency not in rates:
                        st.error(f"❌ Exchange rate not available for {from_currency}")
                        st.warning(f"The API doesn't provide rates for {from_currency}. Please try another currency.")
                        return
                    
                    if to_currency not in rates:
                        st.error(f"❌ Exchange rate not available for {to_currency}")
                        st.warning(f"The API doesn't provide rates for {to_currency}. Please try another currency.")
                        return
                    
                    # Store last update time
                    st.session_state.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    # Convert currency
                    converted_amount = convert_currency_multi(amount, from_currency, to_currency, rates)
                    
                    # Display results
                    st.success("✅ Conversion successful!")
                    
                    # Create result display
                    col_result1, col_result2 = st.columns(2)
                    
                    with col_result1:
                        st.metric(
                            label=f"Original Amount",
                            value=f"{get_currency_symbol(from_currency)} {amount:,.2f} {from_currency}"
                        )
                    
                    with col_result2:
                        st.metric(
                            label=f"Converted Amount",
                            value=f"{get_currency_symbol(to_currency)} {converted_amount:,.2f} {to_currency}"
                        )
                    
                    # Show exchange rate info
                    if from_currency == "USD":
                        rate_info = f"1 USD = {rates[to_currency]:.4f} {to_currency}"
                    elif to_currency == "USD":
                        rate_info = f"1 {from_currency} = {1/rates[from_currency]:.4f} USD"
                    else:
                        # Cross rate
                        usd_to_from = 1 / rates[from_currency]
                        usd_to_to = rates[to_currency]
                        cross_rate = usd_to_to / usd_to_from
                        rate_info = f"1 {from_currency} = {cross_rate:.4f} {to_currency}"
                    
                    st.info(f"💡 Current Exchange Rate: {rate_info}")
                    
                    # Add some visual separation
                    st.markdown("---")
                    
                    # Show conversion formula
                    if from_currency == "USD":
                        st.markdown(f"**Formula:** {amount:.2f} USD × {rates[to_currency]:.4f} = {converted_amount:.2f} {to_currency}")
                    elif to_currency == "USD":
                        st.markdown(f"**Formula:** {amount:.2f} {from_currency} ÷ {rates[from_currency]:.4f} = {converted_amount:.2f} USD")
                    else:
                        # Cross conversion
                        usd_amount = amount / rates[from_currency]
                        st.markdown(f"**Formula:** {amount:.2f} {from_currency} ÷ {rates[from_currency]:.4f} = {usd_amount:.4f} USD × {rates[to_currency]:.4f} = {converted_amount:.2f} {to_currency}")
                        
                else:
                    # Show error message
                    st.error(f"❌ Failed to get exchange rates: {error}")
                    st.warning("Please check your internet connection and try again later.")
        
        # Add some spacing at the bottom
        st.markdown("")
        st.markdown("")
        
        # Footer
        st.markdown("---")
        st.markdown("*Built with ❤️ using Streamlit and Python*")

if __name__ == "__main__":
    main()
