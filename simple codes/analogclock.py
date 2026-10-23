# to create a python web application of a analog clock using the streamlit framework
import streamlit as st
import time
from datetime import datetime

def get_clock_html(now: datetime) -> str:
    """Generates the HTML/SVG string for the analog clock, date, and time."""
    # Calculate angles for hands
    second_angle = now.second * 6
    minute_angle = now.minute * 6 + now.second * 0.1
    hour_angle = (now.hour % 12) * 30 + now.minute * 0.5

    # Colors (Dark Theme)
    face_color = "#2C3E50"  # Dark Blue-Grey
    border_color = "#34495E"
    hour_mark_color = "#ECF0F1" # Off-white
    hour_hand_color = "#E74C3C" # Red
    minute_hand_color = "#3498DB" # Blue
    second_hand_color = "#F1C40F" # Yellow
    
    # Date and Time strings
    time_str = now.strftime("%H:%M:%S")
    date_str = now.strftime("%A, %B %d, %Y")

    return f"""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; font-family: sans-serif;">
        <svg width="400" height="400" viewBox="-200 -200 400 400">
            <!-- Clock Face -->
            <circle cx="0" cy="0" r="190" fill="{face_color}" stroke="{border_color}" stroke-width="10"/>

            <!-- Hour Marks -->
            {''.join([f'<line x1="0" y1="-160" x2="0" y2="-190" transform="rotate({i * 30})" stroke="{hour_mark_color}" stroke-width="4"/>' for i in range(12)])}

            <!-- Hour Hand -->
            <line x1="0" y1="0" x2="0" y2="-100" transform="rotate({hour_angle})" stroke="{hour_hand_color}" stroke-width="8" stroke-linecap="round" />

            <!-- Minute Hand -->
            <line x1="0" y1="0" x2="0" y2="-150" transform="rotate({minute_angle})" stroke="{minute_hand_color}" stroke-width="6" stroke-linecap="round" />

            <!-- Second Hand -->
            <line x1="0" y1="20" x2="0" y2="-160" transform="rotate({second_angle})" stroke="{second_hand_color}" stroke-width="2" stroke-linecap="round" />

            <!-- Center Pin -->
            <circle cx="0" cy="0" r="8" fill="{hour_mark_color}" />
        </svg>
        <div style="margin-top: 20px; text-align: center;">
            <h1 style="margin: 0; font-size: 3em;">{time_str}</h1>
            <p style="margin: 0; font-size: 1.5em; color: gray;">{date_str}</p>
        </div>
    </div>
    """

def main():
    st.title("Analog Clock")

    # Create a placeholder for the clock
    clock_placeholder = st.empty()

    # Run the clock loop
    while True:
        html_code = get_clock_html(datetime.now())
        # Render the SVG in the placeholder
        clock_placeholder.markdown(html_code, unsafe_allow_html=True)

        # Update every second
        time.sleep(1)

if __name__ == '__main__':
    main()