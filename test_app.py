#!/usr/bin/env python3
"""
Simple test file for Currency Converter app
Run this to test the core functions without starting Streamlit
"""

import requests
import json
from app import get_exchange_rate, convert_currency, get_exchange_rates, convert_currency_multi

def test_api_connection():
    """Test if the API is accessible"""
    print("🔍 Testing API connection...")
    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD", timeout=5)
        if response.status_code == 200:
            print("✅ API connection successful!")
            return True
        else:
            print(f"❌ API returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ API connection failed: {e}")
        return False

def test_exchange_rate_function():
    """Test the get_exchange_rate function (backward compatibility)"""
    print("\n🔍 Testing exchange rate function (backward compatibility)...")
    success, rate, error = get_exchange_rate()
    
    if success:
        print(f"✅ Exchange rate function working! Rate: {rate}")
        return True
    else:
        print(f"❌ Exchange rate function failed: {error}")
        return False

def test_exchange_rates_function():
    """Test the new get_exchange_rates function"""
    print("\n🔍 Testing multi-currency exchange rates function...")
    success, rates, error = get_exchange_rates()
    
    if success:
        print(f"✅ Multi-currency exchange rates function working!")
        print(f"   Available currencies: {list(rates.keys())}")
        print(f"   Number of currencies: {len(rates)}")
        return True
    else:
        print(f"❌ Multi-currency exchange rates function failed: {error}")
        return False

def test_currency_conversion():
    """Test the convert_currency function (backward compatibility)"""
    print("\n🔍 Testing currency conversion (backward compatibility)...")
    
    # Test data
    test_rate = 83.50  # Example USD to INR rate
    test_amount = 100.0
    
    # Test INR to USD
    usd_result = convert_currency(test_amount, "INR_to_USD", test_rate)
    expected_usd = test_amount / test_rate
    print(f"INR to USD: {test_amount} INR = {usd_result:.2f} USD (Expected: {expected_usd:.2f})")
    
    # Test USD to INR
    inr_result = convert_currency(test_amount, "USD_to_INR", test_rate)
    expected_inr = test_amount * test_rate
    print(f"USD to INR: {test_amount} USD = {inr_result:.2f} INR (Expected: {expected_inr:.2f})")
    
    # Verify results
    if abs(usd_result - expected_usd) < 0.01 and abs(inr_result - expected_inr) < 0.01:
        print("✅ Currency conversion working correctly!")
        return True
    else:
        print("❌ Currency conversion has errors!")
        return False

def test_multi_currency_conversion():
    """Test the new convert_currency_multi function"""
    print("\n🔍 Testing multi-currency conversion...")
    
    # Get live rates for testing
    success, rates, error = get_exchange_rates()
    if not success:
        print(f"❌ Cannot test multi-currency conversion: {error}")
        return False
    
    # Test various conversions
    test_cases = [
        (100, "USD", "INR"),
        (100, "INR", "USD"),
        (100, "EUR", "GBP"),
        (100, "JPY", "AUD")
    ]
    
    all_tests_passed = True
    
    for amount, from_curr, to_curr in test_cases:
        if from_curr in rates and to_curr in rates:
            try:
                result = convert_currency_multi(amount, from_curr, to_curr, rates)
                print(f"✅ {amount} {from_curr} → {result:.2f} {to_curr}")
            except Exception as e:
                print(f"❌ {amount} {from_curr} → {to_curr} failed: {e}")
                all_tests_passed = False
        else:
            print(f"⚠️  Skipping {from_curr} → {to_curr} (rates not available)")
    
    if all_tests_passed:
        print("✅ Multi-currency conversion working correctly!")
        return True
    else:
        print("❌ Some multi-currency conversions failed!")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting Currency Converter Tests...\n")
    
    tests = [
        test_api_connection,
        test_exchange_rate_function,
        test_exchange_rates_function,
        test_currency_conversion,
        test_multi_currency_conversion
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The app should work correctly.")
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
    
    print("\n💡 To run the full app: streamlit run app.py")

if __name__ == "__main__":
    main()
