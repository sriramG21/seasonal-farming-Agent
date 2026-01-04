
def risk(weather,current_season):
    temp=weather["Temperature"]
    rainfall=weather['Rainfall']
    season=current_season
    alerts=[]
    recommendations=[]
    if rainfall > 30:
        alerts.append("⚠️ Heavy rainfall detected. Risk of waterlogging.")
        recommendations.append("Avoid irrigation and ensure proper drainage.")

    if temp > 35:
        alerts.append("🔥 High temperature detected. Heat stress risk.")
        recommendations.append("Increase watering and protect crops from heat.")

    # --- Season + weather risks ---
    if season == "Kharif" and rainfall > 20:
        alerts.append("🐛 High pest and disease risk during monsoon.")
        recommendations.append("Apply preventive pest control measures.")

    if season == "Rabi" and rainfall > 15:
        alerts.append("🍄 Fungal disease risk due to moisture.")
        recommendations.append("Ensure good field drainage.")

    # If no risks found
    if not alerts:
        alerts.append("✅ No major risks detected.")
        recommendations.append("Farming conditions are normal.CHECK THE CURRENT SEASON BEFOR SOWN")

    return alerts, recommendations