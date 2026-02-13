import streamlit as st

st.set_page_config(page_title="Sellogy", page_icon="🧠")

st.title("🧠 Sellogy")
st.divider()

# --- 1. THE MODE SWITCH ---
mode = st.radio(
    "What is your starting point?",
    ["I have a List Price in mind", "I have a Profit Goal in mind"],
    horizontal=True
)

st.sidebar.header("1. Financials")
item_cost = st.sidebar.number_input("What you paid (COGS)", value=50.0)
promo_pct = st.sidebar.slider("eBay Promo %", 0, 15, 2) / 100

# Fixed eBay Constants
FEE_PCT = 0.1325 + promo_pct
FIXED_FEE = 0.40

# --- 2. CALCULATIONS ---
if mode == "I have a List Price in mind":
    user_price = st.number_input("Desired List Price ($)", value=150.0)
    # The math for what you keep
    ebay_takes = (user_price * FEE_PCT) + FIXED_FEE
    final_price = user_price # Psychology doesn't apply if you set the price
    net_profit = user_price - ebay_takes - item_cost
    display_logic = "Showing profit based on your custom price."

else:
    target_net = st.number_input("Desired Net Profit ($)", value=100.0)
    # The math for what you must list at
    raw_calc = (target_net + item_cost + FIXED_FEE) / (1 - FEE_PCT)
    
    # Apply Brand Strategy to the raw calculation
    st.header("2. Brand Strategy")
    tier = st.selectbox("Category", ["Designer (Khaite)", "Premium (ReDone)", "Mid-Tier (J.Crew)", "Commodity (Zara)"])
    
    if tier == "Designer (Khaite)":
        final_price = round(raw_calc / 10) * 10
    elif tier == "Premium (ReDone)":
        final_price = round(raw_calc / 5) * 5
    elif tier == "Mid-Tier (J.Crew)":
        final_price = int(raw_calc) + 0.99
    else:
        final_price = int(raw_calc) + 0.95
        
    ebay_takes = (final_price * FEE_PCT) + FIXED_FEE
    net_profit = final_price - ebay_takes - item_cost
    display_logic = f"Targeting ${target_net} profit with {tier} rounding."

# --- 3. THE REVEAL ---
st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("LIST PRICE", f"${final_price:,.2f}")
with c2:
    st.metric("EBAY TAKES", f"${ebay_takes:,.2f}")
with c3:
    st.metric("YOU KEEP", f"${net_profit:,.2f}")

# --- 4. VERIFICATION ---
with st.expander("🔍 Math Verification"):
    st.write(f"Selling Price: ${final_price:,.2f}")
    st.write(f"eBay Fees ({FEE_PCT*100:.2f}% + $0.40): -${ebay_takes:,.2f}")
    st.write(f"Your Cost: -${item_cost:,.2f}")
    st.write(f"**Final Net: ${net_profit:,.2f}**")
