import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Projectile Motion Simulator", layout="centered")

st.title("🎯 Projectile Motion Simulation")
st.markdown("This simulation demonstrates the trajectory of a projectile based on initial velocity, launch angle, and gravity.")

velocity = st.number_input("Initial Velocity (m/s)", min_value=0.0, value=20.0, step=1.0)
angle_deg = st.number_input("Launch Angle (degrees)", min_value=0.0, max_value=90.0, value=45.0, step=1.0)
gravity = st.number_input("Gravity (m/s²)", min_value=0.1, value=9.81, step=0.1)

def simulate_projectile(v0, angle_deg, g):
    angle_rad = np.radians(angle_deg)
    t_flight = 2 * v0 * np.sin(angle_rad) / g
    t = np.linspace(0, t_flight, num=500)
    x = v0 * np.cos(angle_rad) * t
    y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2
    max_height = (v0**2) * (np.sin(angle_rad)**2) / (2 * g)
    range_ = (v0**2) * np.sin(2 * angle_rad) / g
    return t, x, y, t_flight, max_height, range_

if st.button("Run Simulation"):
    t, x, y, t_flight, max_height, range_ = simulate_projectile(velocity, angle_deg, gravity)

    st.subheader("📊 Results")
    st.write(f"**Time of Flight:** {t_flight:.2f} s")
    st.write(f"**Maximum Height:** {max_height:.2f} m")
    st.write(f"**Range:** {range_:.2f} m")

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Projectile Trajectory")
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Height (m)")
    ax.grid(True)
    st.pyplot(fig)
