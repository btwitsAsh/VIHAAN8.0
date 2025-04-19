"""
Test script to verify that all required packages are properly installed.
"""
import sys
print(f"Python version: {sys.version}")

# Test imports for all required packages
try:
    import click
    print("✓ click")
except ImportError:
    print("✗ click")

try:
    import matplotlib
    print(f"✓ matplotlib {matplotlib.__version__}")
except ImportError:
    print("✗ matplotlib")

try:
    import mlflow
    print(f"✓ mlflow {mlflow.__version__}")
except ImportError:
    print("✗ mlflow")

try:
    import numpy as np
    print(f"✓ numpy {np.__version__}")
except ImportError:
    print("✗ numpy")

try:
    import pandas as pd
    print(f"✓ pandas {pd.__version__}")
except ImportError:
    print("✗ pandas")

try:
    import sklearn
    print(f"✓ scikit-learn {sklearn.__version__}")
except ImportError:
    print("✗ scikit-learn")

try:
    import seaborn as sns
    print(f"✓ seaborn {sns.__version__}")
except ImportError:
    print("✗ seaborn")

try:
    import statsmodels
    print(f"✓ statsmodels {statsmodels.__version__}")
except ImportError:
    print("✗ statsmodels")

try:
    import zenml
    print(f"✓ zenml {zenml.__version__}")
except ImportError:
    print("✗ zenml")

print("\nAll import tests completed.")