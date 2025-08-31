# 💱 Multi-Currency Converter

A powerful and elegant currency converter built with **Streamlit** that converts between **multiple currencies** using live exchange rates.

## ✨ Features

- **Multi-Currency Support**: Convert between 10+ major currencies
- **Live Exchange Rates**: Real-time conversion using the Open Exchange Rates API
- **Bidirectional Conversion**: Convert between any two supported currencies
- **Clean UI**: Modern, responsive interface built with Streamlit
- **Error Handling**: Graceful handling of API failures and network issues
- **Real-time Updates**: Shows last update timestamp
- **Formula Display**: Educational display of conversion calculations
- **Currency Symbols**: Beautiful display with proper currency symbols

## 🌍 Supported Currencies

- **USD** - US Dollar ($)
- **INR** - Indian Rupee (₹)
- **EUR** - Euro (€)
- **GBP** - British Pound (£)
- **JPY** - Japanese Yen (¥)
- **AUD** - Australian Dollar (A$)
- **CAD** - Canadian Dollar (C$)
- **CHF** - Swiss Franc (CHF)
- **CNY** - Chinese Yuan (¥)
- **SGD** - Singapore Dollar (S$)

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download this project**
   ```bash
   # If using git
   git clone <repository-url>
   cd currency-converter
   
   # Or simply download and extract the files
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   - The app will automatically open in your default browser
   - Usually at: `http://localhost:8501`

## 🎯 How to Use

1. **Select Source Currency**: Choose the currency you want to convert FROM
2. **Select Target Currency**: Choose the currency you want to convert TO
3. **Enter Amount**: Input the amount in the source currency
4. **Click Convert**: Press the "Convert" button to get live rates
5. **View Results**: See the converted amount and current exchange rate

## 🏗️ Project Structure

```
currency-converter/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── config.py          # Configuration file
├── test_app.py        # Test script
├── demo.py            # Demo script
├── run_app.bat        # Windows launcher
├── run_app.sh         # Unix/Linux/Mac launcher
└── README.md          # Project documentation
```

## 🔧 Technical Details

### Dependencies

- **streamlit**: Web application framework
- **requests**: HTTP library for API calls
- **json**: JSON parsing (built-in)
- **datetime**: Date/time handling (built-in)

### API Integration

The app uses the **Open Exchange Rates API** (https://open.er-api.com/v6/latest/USD) to fetch live exchange rates for all supported currencies. This is a free, reliable service that provides real-time currency conversion data.

### Multi-Currency Conversion Logic

The app handles three types of conversions:
1. **USD to Other**: Direct multiplication using API rates
2. **Other to USD**: Direct division using API rates  
3. **Cross-Currency**: Convert via USD (Other → USD → Target)

### Error Handling

The application includes comprehensive error handling for:
- Network connectivity issues
- API failures
- Unsupported currencies
- Invalid responses
- Unexpected errors

## 🌐 Deployment

### Local Development
```bash
streamlit run app.py
```

### Cloud Deployment
This Streamlit app can be easily deployed to:
- **Streamlit Cloud** (recommended)
- **Heroku**
- **AWS/GCP/Azure**
- Any platform that supports Python web applications

## 📱 Features Breakdown

### Core Functionality
- ✅ Multi-currency conversion (10+ currencies)
- ✅ Live exchange rates
- ✅ Real-time API integration
- ✅ Clean, modern UI
- ✅ Cross-currency conversion

### User Experience
- ✅ Intuitive dropdown selection
- ✅ Clear input/output display
- ✅ Loading indicators
- ✅ Success/error messages
- ✅ Formula explanations
- ✅ Currency symbols

### Technical Quality
- ✅ Well-commented code
- ✅ Error handling
- ✅ Responsive design
- ✅ Session state management
- ✅ Backward compatibility

## 🧪 Testing

Run the test suite to verify functionality:
```bash
python test_app.py      # Test all functions
python demo.py          # See conversions in action
```

## 🔄 Backward Compatibility

The app maintains full backward compatibility with the original INR ↔ USD functionality:
- Original functions are preserved
- Original UI elements can be restored
- All existing features work as before

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Adding more currencies
- Improving the UI/UX
- Enhancing error handling

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Streamlit** team for the amazing web app framework
- **Open Exchange Rates** for providing free currency data
- **Python community** for excellent libraries and tools

---

**Happy Converting! 💱✨**
