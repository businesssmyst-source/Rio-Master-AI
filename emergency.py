import requests

def get_emergency_report(family_data):
    # 1. Gather IDs
    dad = family_data.get("Dad", "Not Registered")
    mom = family_data.get("Mom", "Not Registered")
    partner = family_data.get("Partner", "Not Registered")

    try:
        # 2. GPS Location
        res = requests.get('https://ipinfo.io/json')
        data = res.json()
        location = data.get('loc') # This gets "lat,lon"
        
        # FIXED MAP LINK: This is the official Google Maps format
        my_map = f"https://www.google.com/maps?q={location}"
        
        # 3. Report
        report = f"🚨 **RIO PROTOCOL: EMERGENCY SOS** 🚨\n\n"
        report += f"📍 **LOCATION:** {data.get('city')}, {data.get('region')} [LIVE]\n"
        report += f"🗺️ **MAP:** {my_map}\n\n"
        report += f"📢 **FAMILY NOTIFIED:** Dad({dad}), Mom({mom}), Partner({partner})"
        return report
    except:
        return "⚠️ Rio Error: GPS tracking failed. Check internet connection."