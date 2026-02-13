import streamlit as st

# 1. Page Config (Browser Tab Info)
st.set_page_config(page_title="Sellogy", page_icon="🧠")

# 2. THE CSS INJECTION (The "Design" part)
# We use a simple string here to avoid the triple-quote error you hit.
st.markdown("<style> @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap'); html, body, [class*='st-'] { font-family: 'Inter', sans-serif; background-color: #fdfdfb; } .stMetric { border: 1px solid #f0f0ec; padding: 15px; border-radius: 8px; background-color: #ffffff; } </style>", unsafe_allow_code=True)

st.title("🧠 Sellogy")
st.caption("Behavioral Pricing Engine for Premium Resale")
st.markdown("---")

# 3. SIDEBAR FINANCIALS
st.sidebar.header("1. Financials")
cost = st.sidebar.number_input("Item Cost ($)", value=50.0)
target_payout = st.sidebar.number_input("Target Payout ($)", value=100.0)
promo = st.sidebar.slider("Promoted Listing %", 0, 15, 2) / 100

# Logic: Calculate price before psychology
raw_price = (target_payout + cost + 0.40) / (1 - (0.1325 + promo))

# 4. BRAND STRATEGY
st.header("2. Brand Strategy")
tier = st.selectbox(
    "Category",
    ["Designer (Khaite/Jeanerica)", "Premium (ReDone/Mother)", "Mid-Tier (J.Crew/Madewell)", "Commodity (Nike/Zara)"]
)

if tier == "Designer (Khaite/Jeanerica)":
    final_price = round(raw_price / 10) * 10
    logic = "Prestige Pricing: Round numbers ($160) signal luxury equity."
elif tier == "Premium (ReDone/Mother)":
    final_price = round(raw_price / 5) * 5
    logic = "Attribute Framing: Clean $5 increments ($115) signal boutique quality."
elif tier == "Mid-Tier (J.Crew/Madewell)":
    final_price = int(raw_price) + 0.99
    logic = "Left-Digit Effect: .99 anchors the price lower for value-seekers."
else:
    final_price = int(raw_price) + 0.95
    logic = "Clearance Signaling: .95 triggers 'deal' impulses in saturated markets."

# 5. THE RESULTS
st.divider()
c1, c2 = st.columns(2)
with c1:
    st.metric("List Price", f"${final_price:,.2f}")
with c2:
    net = (final_price * (1 - (0.1325 + promo)) - 0.40 - cost)
    st.metric("Net Profit", f"${net:,.2f}")

st.info(f"**Strategy:** {logic}")
