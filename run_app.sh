#!/bin/bash

echo "🚀 Starting Currency Converter..."
echo ""

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "🌐 Starting the app..."
streamlit run app.py
