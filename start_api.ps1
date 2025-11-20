# Start Flask API Server
Write-Host "🚀 Starting Housing Price Prediction API..." -ForegroundColor Green
Write-Host ""

# Check if model files exist
if (-not (Test-Path "model.pkl") -or -not (Test-Path "pipeline.pkl")) {
    Write-Host "❌ Model files not found!" -ForegroundColor Red
    Write-Host "Please run 'python main.py' first to train the model." -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Model files found" -ForegroundColor Green
Write-Host "📡 Starting API server on http://localhost:5000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Available endpoints:" -ForegroundColor Yellow
Write-Host "  - GET  http://localhost:5000/health" -ForegroundColor White
Write-Host "  - POST http://localhost:5000/predict" -ForegroundColor White
Write-Host "  - POST http://localhost:5000/predict-batch" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Start the server
python app.py
