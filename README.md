# ⛷️ New England Ski Master: Route & Snow Intelligence

[![Streamlit App](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

The **New England Ski Indy** is an interactive web dashboard built for Indy Pass holders and Northeast ski enthusiasts. It solves the "Traveler Salesperson Problem" for your next ski trip by calculating optimized driving routes, fuel costs, and providing instant access to official snow reports for over 50 resorts across VT, NH, ME, MA, and CT.



---

## 🌟 Key Features

* **🔍 Advanced Search & Filter**: Instantly find resorts by name, state, or pass affiliation (Indy, Allied, or Non-Indy).
* **📊 Dynamic Distance Matrix**: View an $N \times N$ grid of driving distances between all selected resorts, including a **30% Mountain Winding Factor** for realistic travel times.
* **🗺️ Route Optimizer**: Uses a "Nearest Neighbor" algorithm to suggest the most efficient order to visit your selected mountains.
* **⛽ Fuel Budgeting**: Real-time gas cost estimation based on your vehicle's MPG and current fuel prices.
* **❄️ Official Snow Reports**: Direct one-click access to the live trail and weather reports for every resort.
* **🚀 Google Maps Integration**: One-click to export your entire optimized itinerary directly into Google Maps for turn-by-turn navigation.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.9 or higher
* An internet connection (to fetch map tiles and external links)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/galuardi/NE-skitrip-planner.git
    cd NE-skitrip-planner

    ```

2.  **Install dependencies:**
    ```bash
    pip install streamlit pandas geopy
    ```

3.  **Run the application:**
    ```bash
    streamlit run skitrip-app.py
    ```

---

## 🛠️ Built With

* **[Streamlit](https://streamlit.io/)** - The fastest way to build and share data apps.
* **[GeoPy](https://geopy.readthedocs.io/)** - For high-precision geodesic distance calculations.
* **[Pandas](https://pandas.pydata.org/)** - For data manipulation and matrix generation.

---

## 📈 Data Insights

The app currently tracks nearly **50 mountains**, categorized by:
* **Indy Pass Partners**: Jay Peak, Cannon, Saddleback, etc.
* **Indy Allied**: King Pine, Whaleback.
* **Non-Indy Giants**: Stowe, Killington, Sugarloaf (Epic/Ikon).

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create.
1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Built by [Your Business Name/Name]** *Helping you find the best turns in the Northeast.*
