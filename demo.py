#!/usr/bin/env python3
"""
Demo script for Currency Converter
This script demonstrates the core functionality without starting Streamlit
"""

from app import get_exchange_rate, convert_currency, get_exchange_rates, convert_currency_multi

def demo_conversions():
    """Demonstrate various currency conversions"""
    print("🎯 Currency Converter Demo")
    print("=" * 50)
    
    # Get current exchange rate (backward compatibility)
    print("📡 Fetching live exchange rate (INR ↔ USD)...")
    success, rate, error = get_exchange_rate()
    
    if not success:
        print(f"❌ Failed to get exchange rate: {error}")
        return
    
    print(f"✅ Current Exchange Rate: 1 USD = {rate:.4f} INR")
    print()
    
    # Demo conversions (backward compatibility)
    test_amounts = [100, 500, 1000, 5000, 10000]
    
    print("🔄 INR to USD Conversions:")
    print("-" * 30)
    for amount in test_amounts:
        usd_result = convert_currency(amount, "INR_to_USD", rate)
        print(f"₹{amount:>8,.2f} = ${usd_result:>8.2f}")
    
    print()
    print("🔄 USD to INR Conversions:")
    print("-" * 30)
    for amount in test_amounts:
        inr_result = convert_currency(amount, "USD_to_INR", rate)
        print(f"${amount:>8,.2f} = ₹{inr_result:>8,.2f}")
    
    print()
    print("💡 Formula Examples (INR ↔ USD):")
    print("-" * 30)
    example_amount = 1000
    usd_example = convert_currency(example_amount, "INR_to_USD", rate)
    inr_example = convert_currency(example_amount, "USD_to_INR", rate)
    
    print(f"INR to USD: ₹{example_amount:,} ÷ {rate:.4f} = ${usd_example:.2f}")
    print(f"USD to INR: ${example_amount:,} × {rate:.4f} = ₹{inr_example:,.2f}")
    
    print()
    print("🚀 Multi-Currency Demo")
    print("=" * 50)
    
    # Get multi-currency rates
    print("📡 Fetching multi-currency exchange rates...")
    success, rates, error = get_exchange_rates()
    
    if not success:
        print(f"❌ Failed to get multi-currency rates: {error}")
        return
    
    print(f"✅ Available currencies: {', '.join(rates.keys())}")
    print(f"   Total currencies: {len(rates)}")
    print()
    
    # Demo multi-currency conversions
    print("🔄 Multi-Currency Conversions:")
    print("-" * 40)
    
    # Popular currency pairs
    currency_pairs = [
        ("EUR", "GBP"),
        ("JPY", "AUD"),
        ("CAD", "CHF"),
        ("CNY", "SGD"),
        ("INR", "EUR"),
        ("USD", "JPY")
    ]
    
    for from_curr, to_curr in currency_pairs:
        if from_curr in rates and to_curr in rates:
            amount = 100
            result = convert_currency_multi(amount, from_curr, to_curr, rates)
            print(f"{amount:>6} {from_curr} → {result:>8.2f} {to_curr}")
        else:
            print(f"{'':>6} {from_curr} → {to_curr} (rates not available)")
    
    print()
    print("💡 Cross-Currency Formula Examples:")
    print("-" * 40)
    
    # Show cross-currency conversion
    from_curr, to_curr = "EUR", "GBP"
    if from_curr in rates and to_curr in rates:
        amount = 1000
        result = convert_currency_multi(amount, from_curr, to_curr, rates)
        
        # Calculate cross rate
        usd_to_from = 1 / rates[from_curr]
        usd_to_to = rates[to_curr]
        cross_rate = usd_to_to / usd_to_from
        
        print(f"Cross conversion: {amount} {from_curr} → {to_curr}")
        print(f"Formula: {amount} {from_curr} ÷ {rates[from_curr]:.4f} = {amount/rates[from_curr]:.4f} USD")
        print(f"         {amount/rates[from_curr]:.4f} USD × {rates[to_curr]:.4f} = {result:.2f} {to_curr}")
        print(f"Cross rate: 1 {from_curr} = {cross_rate:.4f} {to_curr}")
    
    print()
    print("🚀 To run the full web app: streamlit run app.py")

if __name__ == "__main__":
    demo_conversions()
