# Start Streamlit Web App
Write-Host "🚀 Starting Housing Price Prediction Web App..." -ForegroundColor Green
Write-Host ""

# Check if model files exist
if (-not (Test-Path "model.pkl") -or -not (Test-Path "pipeline.pkl")) {
    Write-Host "❌ Model files not found!" -ForegroundColor Red
    Write-Host "Please run 'python main.py' first to train the model." -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Model files found" -ForegroundColor Green
Write-Host "🌐 Starting web app on http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Start Streamlit
streamlit run streamlit_app.py
