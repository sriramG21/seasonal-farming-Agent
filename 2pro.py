import season as s
import climate as a
import streamlit as st
import logical as l
st.title("Seasonal-Farming-Agent")
st.subheader("An Assistant for Farmer")
st.markdown("""
### 🌾 Seasonal Farm Planner & Risk Alert Agent  
**This system automatically analyzes current weather and season
to generate risk alerts and farming recommendations**.
""")
city=st.selectbox(
    "select your city",
    ['Chennai','Coimbatore','Erode','karaikudi']
)
if st.button("check current data"):
    season=s.detc_season()
    weather=a.curr_weather(city,api_key='a0f00065d170f9e13f00f9b573228213')
    
    
    alerts,recommendations=l.risk(weather,season)
    st.subheader("🌱 Detected Season")
    st.warning(season)

    st.subheader("🌦 Current Weather")
    st.write(weather)

    st.subheader("🚨 Risk Alerts")
    for i in alerts:
        st.warning(i)

    st.subheader("💡 Recommendations")
    for r in recommendations:
        st.success(r)
    