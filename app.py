import streamlit as st
st.title("Seasonal-Farming-Agent")
st.subheader("An Assistant for Farmer")
season=st.selectbox(
    "Select the season",["October-December","June/July","March/May"]
    )
crop=st.selectbox(
    "Select crop",
    ["Rice", "Wheat", "Maize"]
)
weather=st.selectbox(
    "select current weather",
    ["Normal", "Heavy Rain", "High Temperature"]
)
machine_days=st.slider(
    "Day Since Last Machine Maintance",
    0,90
)
st.divider()
if st.button("Run agent"):
    if season == "Kharif" and weather == "Heavy Rain":
        st.warning("⚠️ Heavy rainfall risk detected. Avoid irrigation to prevent waterlogging.")

    if weather == "High Temperature":
        st.warning("🔥 High temperature risk. Increase irrigation and protect crops from heat stress.")

    # Crop Advisory
    if season == "Rabi" and crop == "Rice":
        st.info("ℹ️ Rice may not be ideal in Rabi season. Consider wheat or pulses.")

    else:
        st.success(f"✅ {crop} is suitable for the selected season.")

    # Machinery Maintenance Alert
    if machine_days > 30:
        st.error("🚜 Maintenance Alert: Machinery service is overdue. Schedule maintenance soon.")
    else:
        st.success("🛠️ Machinery condition is good.")
    st.subheader("📌 Why this advice?")
    st.write(
        "The agent evaluates seasonal conditions, weather risks, crop suitability, "
        "and machinery usage using predefined decision rules to proactively assist farmers."
        )