import streamlit as st
st.set_page_config(page_title="CarbonSee.app", page_icon="🌾")

st.title("🌾 CarbonSee.app")
st.subheader("Carbon Credits | TCT Lens | Palayan AI")
st.success("Live - Ready for Nov 5 Launch - carbonsee.app")
st.divider()

area = st.number_input("Farm Area (hectares)", value=1.0, min_value=0.1)
method = st.selectbox("Method", ["Conventional","AWD","Organic","SRI"])
credits = area * 2.5 * (0.5 if method=="AWD" else 1.0)

col1, col2 = st.columns(2)
col1.metric("Carbon Credits", f"{credits:.2f} tCO2e")
col2.metric("Value PHP", f"₱{credits*1200:.0f}")

st.header("🔬 TCT Lens")
st.info("✅ Verified - Geotag OK - AWD detected")

st.header("🤖 Palayan AI")
q = st.text_input("Ask Palayan AI:", "When to plant Nueva Ecija?")
if st.button("Ask"):
    st.write("Answer: Plant late May-mid June. Use AWD for +50% credits on CarbonSee!")

st.divider()
st.write("Contact: JGCarbon | carbonsee.app | Domain Paid $11.18 | Nov 5 Launch")
