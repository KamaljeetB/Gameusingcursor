#!/bin/bash

echo "🚀 Deploying Labubu Obstacle Course to GitHub Pages..."

# Check if we're in the right directory
if [ ! -f "main.py" ]; then
    echo "❌ Error: main.py not found. Please run this script from the game directory."
    exit 1
fi

# Create web directory if it doesn't exist
if [ ! -d "web" ]; then
    echo "📁 Creating web directory..."
    mkdir web
fi

# Copy web files
echo "📋 Copying web files..."
cp web/index.html .

# Initialize git if not already done
if [ ! -d ".git" ]; then
    echo "🔧 Initializing git repository..."
    git init
    git add .
    git commit -m "🎮 Initial commit - Labubu Obstacle Course"
fi

# Check if remote exists
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "🔗 Please add your GitHub repository as origin:"
    echo "   git remote add origin https://github.com/KamaljeetB/Gameusingcursor.git"
    exit 1
fi

# Push to GitHub
echo "📤 Pushing to GitHub..."
git add .
git commit -m "🌐 Update web deployment files"
git push origin main

echo "✅ Deployment complete!"
echo "🌐 Your game should be available at: https://kamaljeetb.github.io/Gameusingcursor"
echo ""
echo "📋 Next steps:"
echo "1. Go to your GitHub repository settings"
echo "2. Scroll down to 'Pages' section"
echo "3. Set source to 'Deploy from a branch'"
echo "4. Select 'gh-pages' branch (or 'main' if you prefer)"
echo "5. Save and wait for deployment"
echo ""
echo "🎮 Your friends can now play at: https://kamaljeetb.github.io/Gameusingcursor"
