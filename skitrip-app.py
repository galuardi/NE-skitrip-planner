import streamlit as st
import pandas as pd
from geopy.distance import geodesic
import urllib.parse

# 1. Comprehensive New England Dataset (Indy, Allied, Epic, Ikon)
resorts_data = [
    # --- VERMONT ---
    {"Name": "Jay Peak", "State": "VT", "Pass": "Indy", "Coords": (44.9379, -72.5047), "Report": "https://jaypeakresort.com/skiing-riding/snow-report-maps/snow-report"},
    {"Name": "Burke Mountain", "State": "VT", "Pass": "Indy", "Coords": (44.5878, -71.8942), "Report": "https://www.skiburke.com/the-mountain/weather-conditions"},
    {"Name": "Bolton Valley", "State": "VT", "Pass": "Indy", "Coords": (44.4300, -72.8490), "Report": "https://www.boltonvalley.com/winter/trail-maps-snow-reports/"},
    {"Name": "Magic Mountain", "State": "VT", "Pass": "Indy", "Coords": (43.2017, -72.7725), "Report": "https://www.magicmtn.com/snow-report"},
    {"Name": "Saskadena Six", "State": "VT", "Pass": "Indy", "Coords": (43.6264, -72.5414), "Report": "https://www.saskadenasix.com/winter/conditions"},
    {"Name": "Middlebury Snow Bowl", "State": "VT", "Pass": "Indy", "Coords": (43.9392, -72.9558), "Report": "https://www.middleburysnowbowl.com/mountain-report/"},
    {"Name": "Stowe", "State": "VT", "Pass": "Non-Indy", "Coords": (44.5274, -72.7839), "Report": "https://www.stowe.com/the-mountain/mountain-conditions/snow-and-weather-report.aspx"},
    {"Name": "Killington", "State": "VT", "Pass": "Non-Indy", "Coords": (43.6094, -72.7967), "Report": "https://www.killington.com/the-mountain/conditions-weather/current-conditions-weather/"},
    {"Name": "Sugarbush", "State": "VT", "Pass": "Non-Indy", "Coords": (44.1360, -72.8950), "Report": "https://www.sugarbush.com/mountain/conditions"},
    {"Name": "Mad River Glen", "State": "VT", "Pass": "Non-Indy", "Coords": (44.2025, -72.9175), "Report": "https://www.madriverglen.com/mountain-report/"},
    
    # --- NEW HAMPSHIRE ---
    {"Name": "Cannon Mountain", "State": "NH", "Pass": "Indy", "Coords": (44.1773, -71.7018), "Report": "https://www.cannonmt.com/mountain-report"},
    {"Name": "Waterville Valley", "State": "NH", "Pass": "Indy", "Coords": (43.9651, -71.5279), "Report": "https://www.waterville.com/snow-report-maps"},
    {"Name": "Ragged Mountain", "State": "NH", "Pass": "Indy", "Coords": (43.4854, -71.8422), "Report": "https://www.raggedmountainresort.com/mountain-report-cams/"},
    {"Name": "Black Mountain (NH)", "State": "NH", "Pass": "Indy", "Coords": (44.1666, -71.1637), "Report": "https://www.blackmt.com/conditions"},
    {"Name": "Pats Peak", "State": "NH", "Pass": "Indy", "Coords": (43.1610, -71.7972), "Report": "https://www.patspeak.com/the-mountain/snow-report/"},
    {"Name": "McIntyre Ski Area", "State": "NH", "Pass": "Indy", "Coords": (43.0065, -71.4418), "Report": "https://www.mcintyreskiarea.com/mountain-report/"},
    {"Name": "King Pine", "State": "NH", "Pass": "Allied", "Coords": (43.8742, -71.0911), "Report": "https://www.kingpine.com/the-mountain/snow-report/"},
    {"Name": "Loon Mountain", "State": "NH", "Pass": "Non-Indy", "Coords": (44.0360, -71.6320), "Report": "https://www.loonmtn.com/mountain-report"},
    {"Name": "Bretton Woods", "State": "NH", "Pass": "Non-Indy", "Coords": (44.2588, -71.4420), "Report": "https://www.brettonwoods.com/snow-trail-report/"},

    # --- MAINE ---
    {"Name": "Saddleback Maine", "State": "ME", "Pass": "Indy", "Coords": (44.9462, -70.5270), "Report": "https://www.saddlebackmaine.com/mountain-report/"},
    {"Name": "Black Mountain of ME", "State": "ME", "Pass": "Indy", "Coords": (44.5775, -70.6128), "Report": "https://skiblackmountain.org/mountain-report"},
    {"Name": "Sugarloaf", "State": "ME", "Pass": "Non-Indy", "Coords": (45.0315, -70.3130), "Report": "https://www.sugarloaf.com/mountain-report"},
    {"Name": "Sunday River", "State": "ME", "Pass": "Non-Indy", "Coords": (44.4730, -70.8570), "Report": "https://www.sundayriver.com/mountain-report"},

    # --- MA / CT ---
    {"Name": "Berkshire East", "State": "MA", "Pass": "Indy", "Coords": (42.6174, -72.8795), "Report": "https://berkshireeast.com/winter/mountain-conditions"},
    {"Name": "Wachusett", "State": "MA", "Pass": "Non-Indy", "Coords": (42.5080, -71.8850), "Report": "https://www.wachusett.com/mountain-info/snow-report/"},
    {"Name": "Mohawk Mountain", "State": "CT", "Pass": "Indy", "Coords": (41.8340, -73.2954), "Report": "https://www.mohawkmtn.com/the-mountain/trails-and-conditions/"}
]

st.set_page_config(page_title="NE Ski Master 2026", layout="wide")
st.title("🏔️ New England Ski Trip Planner")

# 2. Sidebar Search and Filters
st.sidebar.header("🔍 Find Your Mountain")

# NEW: Search Bar Logic
search_query = st.sidebar.text_input("Search by Name", "").lower()

st.sidebar.markdown("---")
st.sidebar.header("📍 Filter Settings")
view_states = st.sidebar.multiselect("States", ["VT", "NH", "ME", "MA", "CT"], default=["VT", "NH"])
view_passes = st.sidebar.multiselect("Pass Status", ["Indy", "Allied", "Non-Indy"], default=["Indy", "Allied"])

# Apply Filters + Search
filtered = [
    r for r in resorts_data 
    if r["State"] in view_states 
    and r["Pass"] in view_passes
    and (search_query in r["Name"].lower())
]

resort_names = [r["Name"] for r in filtered]
selected = st.sidebar.multiselect("Add to Trip Plan", resort_names, default=resort_names[:5] if resort_names else [])

# 3. Sidebar Fuel Calculator
st.sidebar.markdown("---")
st.sidebar.header("⛽ Fuel Calculator")
mpg = st.sidebar.slider("Vehicle MPG", 10, 50, 22)
gas_price = st.sidebar.number_input("Gas Price ($/gal)", 1.0, 5.0, 3.10)

# 4. App Functions
def get_path(names):
    lookup = {r["Name"]: r["Coords"] for r in resorts_data}
    unvisited = names.copy()
    path = [unvisited.pop(0)]
    while unvisited:
        nxt = min(unvisited, key=lambda x: geodesic(lookup[path[-1]], lookup[x]).miles)
        path.append(nxt)
        unvisited.remove(nxt)
    return path

def build_gmaps_url(route):
    origin = urllib.parse.quote(route[0])
    destination = urllib.parse.quote(route[-1])
    if len(route) > 2:
        waypts = "|".join([urllib.parse.quote(r) for r in route[1:-1]])
        return f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}&waypoints={waypts}&travelmode=driving"
    return f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}&travelmode=driving"

# 5. Main UI Logic
if not selected:
    st.info("👈 Use the search bar or filters in the sidebar to select resorts for your trip.")
else:
    # --- ROW 1: SNOW LINKS ---
    st.subheader("❄️ Official Snow & Condition Reports")
    cols = st.columns(3)
    for idx, name in enumerate(selected):
        resort = next(r for r in resorts_data if r["Name"] == name)
        with cols[idx % 3]:
            st.link_button(f"🔗 {name} Report", resort["Report"], use_container_width=True)

    st.markdown("---")

    # --- ROW 2: DISTANCE MATRIX ---
    st.subheader("📊 Driving Distance Matrix (Road Miles)")
    lookup_coords = {r["Name"]: r["Coords"] for r in resorts_data}
    matrix_df = pd.DataFrame(index=selected, columns=selected)
    for s in selected:
        for e in selected:
            matrix_df.loc[s,e] = f"{(geodesic(lookup_coords[s], lookup_coords[e]).miles * 1.3):.1f}" if s != e else "-"
    st.dataframe(matrix_df, use_container_width=True)

    # --- ROW 3: ROUTE OPTIMIZER ---
    st.subheader("🗺️ Optimized Trip Planner")
    path = get_path(selected)
    total_mi = sum(geodesic(lookup_coords[path[i]], lookup_coords[path[i+1]]).miles * 1.3 for i in range(len(path)-1))
    total_cost = (total_mi / mpg) * gas_price

    c1, c2, c3 = st.columns(3)
    c1.metric("Trip Distance", f"{total_mi:.1f} Miles")
    c2.metric("Fuel Budget", f"${total_cost:.2f}")
    c3.markdown(f"### [🚀 Open Directions]({build_gmaps_url(path)})")
    
    st.write(f"**Best Order:** {' ➔ '.join(path)}")
    st.map(pd.DataFrame([{"lat": lookup_coords[n][0], "lon": lookup_coords[n][1]} for n in path]))

st.caption("Intelligence based on 2026 Season Data. Distances include a 30% winding factor for New England roads.")