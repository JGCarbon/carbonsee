import streamlit as st
import openai
import base64
import re

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="CarbonSee.app", page_icon="🌱", layout="wide")

# --- CUSTOM CSS FOR NAVY & GOLD BRANDING ---
st.markdown("""
<style>
    .stApp { background-color: #0a1931; color: #ffffff; }
    h1, h2, h3 { color: #d4af37 !important; }
    div[data-testid="stMetricValue"] { color: #d4af37; font-size: 2rem; }
    div[data-testid="stMetricLabel"] { color: #ffffff; }
    .stButton>button { background-color: #d4af37; color: #0a1931; font-weight: bold; border-radius: 8px; }
    .stButton>button:hover { background-color: #b8962e; color: #ffffff; }
    .stTabs [data-baseweb="tab"] { color: #d4af37; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- PRO LOGIC ---
if 'is_pro' not in st.session_state:
    st.session_state.is_pro = False

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3302/3302758.png", width=100) 
    st.header("Pro Access")
    if not st.session_state.is_pro:
        pro_code = st.text_input("Enter Pro Access Code", type="password")
        if st.button("Unlock Pro"):
            if pro_code == "JGPRO2026":
                st.session_state.is_pro = True
                st.success("Pro Unlocked!")
                st.rerun()
            else:
                st.error("Invalid Code. Pay via GCash below.")
        
        st.markdown("---")
        st.write("**Upgrade to Pro (P499/mo)**")
        st.write("Get unlimited PDF reports, TCT checks, and AI scans.")
        st.link_button("🔓 Pay via GCash", "https://forms.gle/MMsz9Bj8t7pBhTGA", use_container_width=True)
    else:
        st.success("🌟 Pro Version Active")
        if st.button("Log Out"):
            st.session_state.is_pro = False
            st.rerun()

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
        base_credits = 2.5
        multiplier = 1.2 if "AWD" in method else 1.0
        annual_credits = area * base_credits * multiplier
        price_per_credit_php = 1200
        annual_value_php = annual_credits * price_per_credit_php
        total_30yr_value = annual_value_php * 30
        
        st.divider()
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.metric("Annual Carbon Credits", f"{annual_credits:,.2f} tCO2e")
            st.metric("Annual Gross Value", f"₱{annual_value_php:,.2f}")
        with res_col2:
            st.metric("30-Year Total Projection", f"₱{total_30yr_value:,.0f}", "Conservative Estimate")
            st.info("💡 *Note: This is a baseline estimate.*")
        
        if st.session_state.is_pro:
            report_text = f"CARBONSEE REPORT\nArea: {area} ha\nMethod: {method}\n30-Yr Value: PHP {total_30yr_value:,.0f}"
            st.download_button("📥 Download Official PDF Report", data=report_text, file_name="Carbonsee_Report.txt", mime="text/plain")
        else:
            st.warning("🔒 **Upgrade to Pro** to download the official PDF Report for your bank/developer.")

        # --- LEAD GENERATION BUTTONS ---
        st.divider()
        st.markdown("### 🚀 Next Steps")
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            # Replace with your actual Land Submission Google Form
            st.link_button("🤝 Submit Land for Aggregation", "https://forms.gle/YOUR_NEW_LAND_FORM_LINK", use_container_width=True)
            
        with col_btn2:
            # Replace with your actual Viber Chat Link
            st.link_button("💬 Talk to Atty. Grace", "https://viber.me/YOUR_VIBER_LINK", use_container_width=True)
            
        st.info("💡 **Tip:** Want a bankable report to show to a solar developer? Upgrade to Pro to download the official PDF.")

# ==========================================
# TAB 2: SOLAR LEASE CALCULATOR
# ==========================================
with tab_solar:
    st.subheader("Solar Lease Calculator")
    st.write("Calculate guaranteed baseline revenue from leasing land.")
    
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

# ==========================================
# TAB 3: PRO TOOLS
# ==========================================
with tab_pro:
    st.subheader("Pro Tools Dashboard")
    
    if not st.session_state.is_pro:
        st.warning("🔒 **Pro Access Required.** Please enter your access code in the sidebar to unlock TCT Lens and Palayan AI.")
    else:
        tct_tab, ai_tab = st.tabs(["📄 TCT Lens", "🌾 Palayan AI"])
        
        # --- TCT LENS (WITH MANUAL FALLBACK) ---
        with tct_tab:
            st.write("Upload TCT to extract legal data and calculate Carbon Potential.")
            tct_file = st.file_uploader("Upload TCT Image (JPG/PNG)", type=["jpg", "png"])
            
            if tct_file is not None:
                st.image(tct_file, width=300, caption="Uploaded TCT")
                if st.button("🔍 Run TCT Lens Analysis"):
                    with st.spinner("Reading Title and calculating value..."):
                        try:
                            image_bytes = tct_file.read()
                            base64_image = base64.b64encode(image_bytes).decode('utf-8')
                            client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
                            
                            prompt = """
                            You are a meticulous Philippine Legal Engineer. Analyze this Transfer Certificate of Title (TCT).
                            Extract: 1. TCT Number, 2. Registered Owner(s), 3. Total Area in hectares (convert sqm to hectares if needed), 4. Location (Lot, Barangay, Municipality), 5. Encumbrances / Annotations.
                            If a field is blurry or missing, state "Not clearly readable". Use Markdown to format beautifully.
                            At the very end of your response, you MUST output ONLY the numerical area in hectares formatted exactly like this: [AREA_HA: X.XX]
                            If you cannot read the area, output [AREA_HA: 0].
                            """
                            
                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=[{"role": "user", "content": [{"type": "text", "text": prompt}, {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}]}],
                                max_tokens=500
                            )
                            
                            result_text = response.choices[0].message.content
                            st.success("✅ Analysis Complete!")
                            st.markdown(result_text)
                            
                            # Extract area
                            area_match = re.search(r'\[AREA_HA:\s*([\d\.]+)\]', result_text)
                            extracted_area = float(area_match.group(1)) if area_match else 0.0
                            
                            st.divider()
                            
                            # --- MANUAL FALLBACK LOGIC ---
                            final_area = extracted_area
                            
                            if extracted_area == 0:
                                st.warning("⚠️ **AI could not read the land area clearly.** Please type the area manually below to calculate the carbon potential.")
                                manual_area = st.number_input("Enter Area (Hectares) manually:", min_value=0.1, value=1.0, step=0.1)
                                final_area = manual_area
                            
                            if final_area > 0:
                                base_credits = 2.5
                                price_php = 1200
                                annual_val = final_area * base_credits * price_php
                                total_30yr = annual_val * 30
                                
                                st.info(f"🌱 **Carbon Potential Found!** Based on an area of **{final_area} hectares**, this land could generate an estimated **₱{total_30yr:,.0f}** over 30 years in carbon credits.")
                                
                                if not st.session_state.is_pro:
                                    st.warning("🔒 Upgrade to Pro to download the full legal and financial report.")
                                else:
                                    report_text = f"CARBONSEE TCT REPORT\nArea: {final_area} ha\n30-Yr Carbon Value: PHP {total_30yr:,.0f}"
                                    st.download_button("📥 Download Full TCT & Carbon Report", data=report_text, file_name="TCT_Carbon_Report.txt")
                                    
                        except Exception as e:
                            st.error(f"Error: {e}")
                            
        # --- PALAYAN AI v2.0 ---
        with ai_tab:
            st.info("⚠️ **PAALALA:** Para sa tumpak na resulta, mag-upload ng malinaw at malapit na litrato (close-up). Iwasan ang pag-upload ng malawak na tanawin ng bukid.")
            
            analysis_type = st.selectbox(
                "Ano ang gusto mong i-check? (What do you want to check?)",
                [
                    "🌾 Sakit at Peste sa Dahon (Leaf Disease & Pest)",
                    "🍚 Handa na ba Anihin? (Harvest Readiness - Grains)",
                    "🐛 Anong Insekto Ito? (Insect Identification)"
                ]
            )
            
            leaf = st.file_uploader("Upload Image here (JPG/PNG)", type=["jpg", "png"])
            
            if leaf is not None:
                st.image(leaf, width=300, caption="Uploaded Image")
                if st.button("🔍 Run Palayan AI Scan"):
                    with st.spinner("Sinusuri ng Palayan AI..."):
                        try:
                            image_bytes = leaf.read()
                            base64_image = base64.b64encode(image_bytes).decode('utf-8')
                            client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
                            
                            if "Sakit" in analysis_type:
                                prompt = "You are Palayan AI. Look closely at this single leaf. Identify the specific disease or pest. Rate severity 1-10. Provide a simple, actionable treatment plan. Speak directly to the farmer in a mix of Tagalog and English."
                            elif "Harvest" in analysis_type:
                                prompt = "You are Palayan AI. Look at the rice grains in this image. Determine harvest readiness. Are they golden and ready, or still too green? Give a clear recommendation (e.g., 'Hintayin pa ng X days' or 'Pwede nang anihin'). Speak directly to the farmer in Taglish."
                            else:
                                prompt = "You are Palayan AI. Identify the insect in this image. Tell the farmer if it is a pest or beneficial. If it's a pest, provide a safe way to eliminate it. Speak directly to the farmer in Taglish."

                            response = client.chat.completions.create(
                                model="gpt-4o",
                                messages=[{"role": "user", "content": [{"type": "text", "text": prompt}, {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}]}],
                                max_tokens=400
                            )
                            st.success("✅ Analysis Complete!")
                            st.markdown(response.choices[0].message.content)
                        except Exception as e:
                            st.error(f"Error: {e}")
            
            st.divider()
            
            # Text Advisory for Planting
            st.write("**Ask Palayan AI about planting schedules:**")
            question = st.text_input("Halimbawa: Kailan magandang magtanim ng palay ngayong tag-ulan?")
            if st.button("Ask Palayan AI"):
                if question:
                    with st.spinner("Nag-iisip..."):
                        client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
                        response = client.chat.completions.create(
                            model="gpt-4o",
                            messages=[{"role": "user", "content": [{"type": "text", "text": f"You are Palayan AI. Answer this farmer's question clearly and briefly in Taglish (Tagalog/English): {question}"}]}],
                            max_tokens=300
                        )
                        st.info(response.choices[0].message.content)

st.divider()
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Palayan AI Labs • Division of JG Climate Law</p>", unsafe_allow_html=True)
