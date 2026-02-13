import streamlit as st

st.set_page_config(page_title="Sellogy", page_icon="🧠")

st.title("🧠 Sellogy")
st.write("Target-Based Pricing Engine")
st.divider()

# --- 1. CLEAR INPUTS ---
st.sidebar.header("1. YOUR DATA")
# This is where you enter what you actually paid
item_cost = st.sidebar.number_input("What did you pay? (COGS)", value=50.0, step=1.0)
# This is the profit you WANT to put in your pocket
target_profit = st.sidebar.number_input("Desired Net Profit", value=100.0, step=1.0)
# Optional marketing fee
promo_fee_pct = st.sidebar.slider("eBay Promo %", 0, 15, 2) / 100

# --- 2. THE MATH (eBay Clothing Standards) ---
# Total Fees = 13.25% + Promo % + $0.40 fixed
platform_fee_pct = 0.1325 + promo_fee_pct

# TO GET YOUR PROFIT: We need to cover Cost + Target + Fixed Fee
# Price = (Cost + Target + 0.40) / (1 - Fees)
raw_price = (item_cost + target_profit + 0.40) / (1 - platform_fee_pct)

# --- 3. BRAND STRATEGY ---
st.header("2. Brand Strategy")
tier = st.selectbox(
    "Select Brand Category",
    ["Designer (Khaite)", "Premium (ReDone)", "Mid-Tier (J.Crew)", "Commodity (Zara)"]
)

if tier == "Designer (Khaite)":
    final_price = round(raw_price / 10) * 10
elif tier == "Premium (ReDone)":
    final_price = round(raw_price / 5) * 5
elif tier == "Mid-Tier (J.Crew)":
    final_price = int(raw_price) + 0.99
else:
    final_price = int(raw_price) + 0.95

# --- 4. THE BREAKDOWN ---
st.divider()
col1, col2, col3 = st.columns(3)

# Real-time calculation based on the ROUNDED final price
ebay_cut = (final_price * platform_fee_pct) + 0.40
actual_payout = final_price - ebay_cut
actual_profit = actual_payout - item_cost

with col1:
    st.metric("LIST AT", f"${final_price:,.2f}")
with col2:
    st.metric("EBAY TAKES", f"${ebay_cut:,.2f}")
with col3:
    st.metric("YOU KEEP", f"${actual_profit:,.2f}")

# --- 5. THE AUDIT TRAIL ---
st.info(f"**Audit Trail:** To net **${actual_profit:,.2f}**, you must list at **${final_price:,.2f}** because eBay takes a **{platform_fee_pct*100:.2f}%** cut plus a $0.40 transaction fee.")
