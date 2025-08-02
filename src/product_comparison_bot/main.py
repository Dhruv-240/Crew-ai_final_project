#!/usr/bin/env python
import warnings
from product_comparison_bot.crew import ProductComparisonBot

# Suppress irrelevant syntax warnings (e.g., from pysbd)
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def compare_products(product_1: str, product_2: str, user_preferences: str) -> str:
    """
    Compare two products and return the result as a string.
    """
    inputs = {
        'product_1': product_1,
        'product_2': product_2,
        'user_preferences': user_preferences
    }

    try:
        # CrewAI usually returns final output from kickoff()
        result = ProductComparisonBot().crew().kickoff(inputs=inputs)
        return str(result) if result else "⚠️ No result returned from the crew."
    except Exception as e:
        return f"❌ An error occurred: {e}"


def run():
    """
    Default entry point for CLI tools like `uv run run_crew`.
    """
    compare_products(
        product_1=input("Enter first product: "),
        product_2=input("Enter second product: "),
        user_preferences=input("Enter your preferences: ")
    )
  


# Optional manual test
if __name__ == "__main__":
    run()
