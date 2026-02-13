import streamlit as st

# --- DESIGN INJECTION (Minimalist Style) ---
st.set_page_config(page_title="Sellogy", page_icon="🧠", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #fcfcfc; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #eee; }
    h1 { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 700; color: #111; }
    </style>
    """, unsafe_allow_code=True)

st.title("🧠 Sellogy")
st.subheader("Behavioral Pricing for Premium Resale")
st.markdown("---")

# --- 1. THE FINANCIALS (Sidebar) ---
st.sidebar.header("1. Financials")
cost = st.sidebar.number_input("Your Cost ($)", value=50.0, step=5.0)
target_payout = st.sidebar.number_input("Target Payout ($)", value=100.0, step=5.0)
promo = st.sidebar.slider("Promoted Listing %", 0, 15, 2) / 100

# eBay Fee Logic (Clothing: 13.25% + $0.40)
# Reverse-engineering: (Payout + Cost + Fixed Fee) / (1 - Fees)
raw_price = (target_payout + cost + 0.40) / (1 - (0.1325 + promo))

# --- 2. THE PSYCHOLOGY (Main UI) ---
st.header("2. Brand Strategy")
tier = st.selectbox(
    "What category is this item?",
    ["Designer (Khaite/Jeanerica)", "Premium (ReDone/Mother)", "Mid-Tier (J.Crew/Madewell)", "Commodity (Nike/Lulu/Zara)"]
)

if tier == "Designer (Khaite/Jeanerica)":
    # Prestige: Round to nearest $10
    final_price = round(raw_price / 10) * 10
    logic = "Prestige Pricing: Round numbers ($160) increase 'Processing Fluency.' High-end buyers avoid 'cheap' decimal endings."
    
elif tier == "Premium (ReDone/Mother)":
    # Clean: Round to nearest $5
    final_price = round(raw_price / 5) * 5
    logic = "Attribute Framing: Clean $5 increments ($115) signal boutique quality without the mass-market feel of .99."

elif tier == "Mid-Tier (J.Crew/Madewell)":
    # Charm: .99 ending
    final_price = int(raw_price) + 0.99
    logic = "The Left-Digit Effect: Buyers are comparison shopping. .99 anchors the price to the lower digit to win the 'value' battle."

else: # Commodity
    # Clearance: .95 ending
    final_price = int(raw_price) + 0.95
    logic = "Clearance Signaling: .95 is psychological shorthand for 'Final Markdown.' It triggers faster checkout for saturated inventory."

# --- 3. THE RESULTS ---
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.metric(label="List Price", value=f"${final_price:,.2f}")

with col2:
    # Recalculate actual net based on the rounded final price
    actual_profit = (final_price * (1 - (0.1325 + promo)) - 0.40 - cost)
    st.metric(label="Net Profit", value=f"${actual_profit:,.2f}")

st.info(f"**Psychology Insight:** {logic}")

# --- 4. THE LANGUISH FIX ---
st.markdown("---")
if st.button("🆘 Item Languishing? Click for a Psych-Fix"):
    if tier == "Premium (ReDone/Mother)":
        st.warning("**The Satiation Effect:** If ReDone is sitting, shift from price-focus to 'Fit Scarcity.' Emphasize the specific wash or model name in the title.")
    elif tier == "Designer (Khaite/Jeanerica)":
        st.success("**The Trust Gap:** High-end items sit when trust is low. Ensure your description uses 'Dignified Language'—avoid 'Must Sell' or 'Bargain'.")
    else:
        st.info("**The Friction Point:** For Mid-Tier/Commodity, check your shipping cost. Buyers in this tier are highly sensitive to shipping 'surprises'.")
