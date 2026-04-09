#!/bin/bash
# Railway build script

set -e

echo "📦 Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt

echo "✓ Build complete"
