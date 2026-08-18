import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Founder Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to mimic modern SaaS padding and card look
st.markdown("""
    <style>
        .main { background-color: #0e1117; }
        .metric-card {
            background-color: #161b22;
            border: 1px solid #30363d;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation & filters
st.sidebar.title("🚀 SaaS Control")
st.sidebar.markdown("---")
time_range = st.sidebar.selectbox("Timeframe", ["Last 30 Days", "QTD", "YTD"])
st.sidebar.markdown("### Founder Quick Links")
st.sidebar.markdown("- [Billing & Stripe](https://stripe.com)")
st.sidebar.markdown("- [Analytics Provider](https://mixpanel.com)")

# Main Header
st.title("Executive Overview")
st.markdown(f"Showing performance metrics for **{time_range}**.")

# Top Metrics Row (MRR, Churn, Signups)
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Monthly Recurring Revenue", value="$48,250", delta="+12%")
col2.metric(label="Net Revenue Retention", value="108%", delta="+2%")
col3.metric(label="User Churn Rate", value="2.1%", delta="-0.4%")
col4.nic = col4.metric(label="New Signups", value="1,240", delta="+185")

st.markdown("---")

# Charts / Detailed Data Section
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("MRR Growth Trajectory")
    chart_data = pd.DataFrame(
        np.random.randn(10, 2).cumsum() + [20, 40],
        columns=['Actual MRR', 'Projected Target']
    )
    st.line_chart(chart_data)

with col_right:
    st.subheader("Conversion by Plan")
    source_data = pd.DataFrame({
        'Plan': ['Free Trial', 'Pro Tier', 'Enterprise'],
        'Users': [850, 320, 70]
    })
    st.bar_chart(source_data, x='Plan', y='Users')

# Footer / Action Area
st.markdown("---")
st.caption("Founder Dashboard v1.0 • Built with pure Python and Streamlit")
