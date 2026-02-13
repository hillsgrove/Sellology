import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Sellogy", page_icon="🧠")

# 2. Basic Header (No custom CSS to avoid errors)
st.title("🧠 Sellogy")
st.write("Behavioral Pricing Engine for Premium Resale")
st.divider()

# 3. Sidebar Financials
st.sidebar.header("1. Financials")
cost = st.sidebar.number_input("Item Cost ($)", value=50.0)
payout = st.sidebar.number_input("Target Payout ($)", value=100.0)
promo = st.sidebar.slider("Promoted Listing %", 0, 15, 2) / 100

# Base Math
raw_price = (payout + cost + 0.40) / (1 - (0.1325 + promo))

# 4. Brand Strategy
st.header("2. Brand Strategy")
tier = st.selectbox(
    "Category",
    ["Designer (Khaite/Jeanerica)", "Premium (ReDone/Mother)", "Mid-Tier (J.Crew/Madewell)", "Commodity (Nike/Zara)"]
)

if tier == "Designer (Khaite/Jeanerica)":
    final_price = round(raw_price / 10) * 10
    logic = "PRESTIGE: Round numbers signal luxury and high equity."
elif tier == "Premium (ReDone/Mother)":
    final_price = round(raw_price / 5) * 5
    logic = "QUALITY: Clean $5 increments signal boutique value."
elif tier == "Mid-Tier (J.Crew/Madewell)":
    final_price = int(raw_price) + 0.99
    logic = "CHARM: .99 anchors the price lower for value-seekers."
else:
    final_price = int(raw_price) + 0.95
    logic = "CLEARANCE: .95 triggers 'deal' impulses in saturated markets."

# 5. The Results
st.divider()
c1, c2 = st.columns(2)
with c1:
    st.metric("LIST PRICE", f"${final_price:,.2f}")
with c2:
    actual_profit = (final_price * (1 - (0.1325 + promo)) - 0.40 - cost)
    st.metric("NET PROFIT", f"${actual_profit:,.2f}")

st.info(f"**Psychology Logic:** {logic}")
