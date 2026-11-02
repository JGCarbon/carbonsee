import streamlit as st

# --- PAGE CONFIGURATION (Must be first) ---
st.set_page_config(page_title="CarbonSee.app", page_icon="🌱", layout="wide")

# --- CUSTOM CSS FOR NAVY & GOLD BRANDING ---
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #0a1931;
        color: #ffffff;
    }
    /* Headers in Gold */
    h1, h2, h3 {
        color: #d4af37 !important;
    }
    /* Metrics (The big numbers) */
    div[data-testid="stMetricValue"] {
        color: #d4af37;
        font-size: 2rem;
    }
    div[data-testid="stMetricLabel"] {
        color: #ffffff;
    }
    /* Buttons */
    .stButton>button {
        background-color: #d4af37;
        color: #0a1931;
        font-weight: bold;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #b8962e;
        color: #ffffff;
    }
    /* Tabs */
    .stTabs [data-baseweb="tab"] {
        color: #d4af37;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🌱 CARBONSEE.app")
st.markdown("**Climate Law & Legal Engineering • JG Climate Law**")
st.success("🎉 **FIRST BATCH LAUNCH** - Free Testing until Nov 5!")

st.divider()

# --- MAIN TABS ---
tab_carbon, tab_solar, tab_pro = st.tabs([
    "🌱 Carbon Calculator", 
    "☀️ Solar Lease Calculator", 
    "💼 Pro Tools (TCT & AI)"
])

# ==========================================
# TAB 1: CARBON CALCULATOR
# ==========================================
with tab_carbon:
    st.subheader("Carbon Credit Projection")
    st.write("Calculate conservative carbon credits for your land.")
    
    col1, col2 = st.columns(2)
    with col1:
        area = st.number_input("Farm Area (Hectares)", min_value=1.0, value=18.7, step=0.1)
        method = st.selectbox("Farming Method", ["Conventional", "Alternate Wetting and Drying (AWD)"])
    with col2:
        st.write("")
        st.write("")
        calculate_carbon = st.button("Calculate Carbon Value", use_container_width=True)

    if calculate_carbon:
        # Logic: Base is 2.5 credits/ha. AWD adds a 20% premium (conservative)
        base_credits = 2.5
        multiplier = 1.2 if "AWD" in method else 1.0
        
        annual_credits = area * base_credits * multiplier
        price_per_credit_php = 1200 # Approx $20 USD
        
        annual_value_php = annual_credits * price_per_credit_php
        total_30yr_value = annual_value_php * 30
        
        st.divider()
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.metric("Annual Carbon Credits", f"{annual_credits:,.2f} tCO2e")
            st.metric("Annual Gross Value", f"₱{annual_value_php:,.2f}")
        with res_col2:
            st.metric("30-Year Total Projection", f"₱{total_30yr_value:,.0f}", "Conservative Estimate")
            st.info("💡 *Note: This is a baseline estimate. Premium JCM/Verra markets can yield higher rates.*")

# ==========================================
# TAB 2: SOLAR LEASE CALCULATOR
# ==========================================
with tab_solar:
    st.subheader("Solar Lease Calculator")
    st.write("Calculate guaranteed baseline revenue from leasing land to solar developers.")
    
    col1, col2 = st.columns(2)
    with col1:
        solar_ha = st.number_input("Lease Area (Hectares)", min_value=1.0, value=12.0, step=1.0)
        lease_rate = st.number_input("Lease Rate per Ha/Year (PHP)", value=1000000, step=100000)
    with col2:
        upfront = st.number_input("Upfront Payment (PHP)", value=18000000, step=1000000)
        lease_years = st.number_input("Lease Term (Years)", value=15, step=1)
        
    if st.button("Calculate Solar Revenue", use_container_width=True):
        annual_lease = solar_ha * lease_rate
        total_lease = annual_lease * lease_years
        total_baseline = upfront + total_lease
        
        st.divider()
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.metric("Annual Lease Revenue", f"₱{annual_lease:,.0f}")
            st.metric(f"Total {lease_years}-Year Lease", f"₱{total_lease:,.0f}")
        with res_col2:
            st.metric("Upfront Cash", f"₱{upfront:,.0f}", "Direct to Lessor")
            st.metric("Total Guaranteed Baseline", f"₱{total_baseline:,.0f}")
            
        st.success("💡 *Plus 7-10% Royalty on Gross Revenue (NGCP Meter)*")

# ==========================================
# TAB 3: PRO TOOLS (TCT & PALAYAN)
# ==========================================
with tab_pro:
    st.subheader("Pro Tools Dashboard")
    
    tct_tab, ai_tab = st.tabs(["📄 TCT Lens", "🌾 Palayan AI"])
    
    with tct_tab:
        st.write("Upload TCT to verify boundaries and encumbrances.")
        tct_files = st.file_uploader("Upload TCT PDFs or Images", accept_multiple_files=True)
        if tct_files:
            st.success(f"✅ {len(tct_files)} TCTs uploaded successfully!")
            st.info("🟢 **Verified - Geotag OK - AWD detected** (Demo Logic)")
            
    with ai_tab:
        st.write("Scan rice leaves for disease or ask agricultural questions.")
        leaf = st.file_uploader("Upload Rice Leaf Image", type=["jpg", "png"])
        if leaf:
            st.image(leaf, width=200)
            st.success("✅ Leaf scanned - No disease detected (Demo Logic)")
            
        st.chat_input("Ask Palayan AI: When is the best time to plant?")
        st.caption("*(Chat interface coming soon)*")

st.divider()

# --- FOOTER / UPGRADE ---
col_up1, col_up2, col_up3 = st.columns([1, 2, 1])
with col_up2:
st.link_button("🔓 Unlock Pro (P499/mo) via GCash"    https://forms.gle/MMsz9Bjj8t7pBhTGA use_container_width=True)
    st.caption("Once live, scan QR to download PDF Report & verify 10 TCTs/month.")

st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Palayan AI Labs • Division of JG Climate Law</p>", unsafe_allow_html=True)
