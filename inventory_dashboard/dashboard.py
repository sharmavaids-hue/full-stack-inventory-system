import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import requests
import plotly.express as px  # NEW: For beautiful charts

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Enterprise Inventory Master",
    page_icon="🏢",
    layout="wide"
)

st.title("🏢 Enterprise Inventory Master")
st.markdown("---")

# --- SIDEBAR: CONTROLS (SAME AS BEFORE) ---
with st.sidebar:
    st.header("⚙️ Control Panel")
    
    # A. Manual Add
    with st.expander("➕ Add New Item", expanded=False):
        with st.form("add_product_form"):
            new_name = st.text_input("Product Name")
            new_category = st.selectbox("Category", ["Electronics", "Furniture", "Luxury", "Office", "Accessories"])
            new_price = st.number_input("Price ($)", min_value=0.0, format="%.2f")
            new_stock = st.number_input("Stock Level", min_value=0, step=1)
            if st.form_submit_button("Add Item"):
                try:
                    requests.get(f"http://localhost:8080/api/products/add?name={new_name}&price={new_price}")
                    st.success(f"Added {new_name}!")
                    st.rerun()
                except:
                    st.error("Connection Failed")

    # B. Bulk Upload
    with st.expander("📂 Bulk Upload", expanded=False):
        uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
        if uploaded_file and st.button("Process Upload"):
            csv_data = pd.read_csv(uploaded_file)
            progress = st.progress(0)
            for i, row in csv_data.iterrows():
                try:
                    payload = {"name": row['name'], "category": row['category'], "price": row['price'], "stockLevel": row['stock_level']}
                    requests.post("http://localhost:8080/api/products/add", json=payload)
                except: pass
                progress.progress((i + 1) / len(csv_data))
            st.success("Upload Complete!")
            st.rerun()

    # C. Delete
    with st.expander("🗑️ Delete Item", expanded=False):
        del_id = st.number_input("ID to Delete", min_value=1, step=1)
        if st.button("Delete"):
            requests.delete(f"http://localhost:8080/api/products/{del_id}")
            st.success(f"Deleted ID {del_id}")
            st.rerun()

# --- LOAD DATA ---
db_str = 'postgresql+psycopg2://postgres:secret@localhost:5432/inventory_system'
conn = create_engine(db_str)
try:
    df = pd.read_sql("SELECT * FROM product", conn)
    # Rename columns for cleaner display if needed (Java uses camelCase, SQL uses snake_case)
    if 'stockLevel' in df.columns:
        df.rename(columns={'stockLevel': 'stock_level'}, inplace=True)
except:
    st.error("⚠️ Database Disconnected. Is Docker running?")
    df = pd.DataFrame()

# --- MAIN DASHBOARD UI ---
if not df.empty:
    
    # SEARCH BAR (Global)
    col_search, col_padding = st.columns([1, 2])
    with col_search:
        search = st.text_input("🔍 Search Products...", placeholder="Type 'MacBook'...")
        if search:
            df = df[df['name'].str.contains(search, case=False, na=False)]

    # TABS FOR ORGANIZATION
    tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Advanced Analytics", "📝 Data & Export"])

    # === TAB 1: OVERVIEW ===
    with tab1:
        # Top KPI Row
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        
        total_val = (df['price'] * df['stock_level']).sum()
        avg_price = df['price'].mean()
        
        kpi1.metric("Total Inventory Value", f"${total_val:,.0f}", delta="Asset Value")
        kpi2.metric("Total Products", len(df), delta="Count")
        kpi3.metric("Avg Unit Price", f"${avg_price:,.0f}")
        kpi4.metric("Low Stock Alerts", len(df[df['stock_level'] < 5]), delta_color="inverse")

        st.markdown("###") # Spacer
        
        # Chart: Stock Levels
        st.subheader("📦 Current Stock Levels")
        fig_stock = px.bar(
            df, 
            x='name', 
            y='stock_level', 
            color='stock_level', # Color changes based on stock amount
            color_continuous_scale='Bluered_r', # Red = Low stock, Blue = High
            title="Real-time Stock Count"
        )
        st.plotly_chart(fig_stock, use_container_width=True)

    # === TAB 2: ADVANCED ANALYTICS (The "Resume Booster") ===
    with tab2:
        col_charts_1, col_charts_2 = st.columns(2)
        
        with col_charts_1:
            st.subheader("💰 Value by Category")
            # Create a "Category Value" dataframe
            cat_group = df.groupby('category').apply(
                lambda x: (x['price'] * x['stock_level']).sum()
            ).reset_index(name='total_value')
            
            fig_pie = px.pie(
                cat_group, 
                values='total_value', 
                names='category', 
                title="Where is our money tied up?",
                hole=0.4 # Makes it a donut chart (Modern look)
            )
            st.plotly_chart(fig_pie, use_container_width=True)

        with col_charts_2:
            st.subheader("📉 Price vs. Stock Strategy")
            # Scatter plot to show correlation
            fig_scatter = px.scatter(
                df, 
                x='price', 
                y='stock_level', 
                size='price', # Bubble size = Price
                color='category', 
                hover_name='name',
                title="Are we overstocking expensive items?"
            )
            st.plotly_chart(fig_scatter, use_container_width=True)

    # === TAB 3: RAW DATA ===
    with tab3:
        st.subheader("🗄️ Database Records")
        st.dataframe(df, use_container_width=True)
        
        # Export Button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "📥 Download Full Report", 
            data=csv, 
            file_name="inventory_report.csv", 
            mime="text/csv"
        )