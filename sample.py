"""
A sample Python script demonstrating basic syntax.
Author: Example User
"""

import datetime  # Import a built-in module

def greet_user(name):
    """A function that returns a personalized greeting."""
    hour = datetime.datetime.now().hour
    
    if hour < 12:
        period = "morning"
    elif hour < 18:
        period = "afternoon"
    else:
        period = "evening"
        
    return f"Good {period}, {name}! Welcome to 
