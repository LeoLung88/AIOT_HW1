import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 設定頁面配置
st.set_page_config(
    page_title="CRISP-DM 線性迴歸範例", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 標題
st.title("🔬 CRISP-DM 線性迴歸互動範例")
st.markdown("---")

# 側邊欄 - 參數設定
st.sidebar.header("📊 資料參數設定")

# 1. 資料生成參數
n_points = st.sidebar.slider(
    "資料點數量 (n)", 
    min_value=100, 
    max_value=1000, 
    value=500, 
    step=50,
    help="生成多少個資料點"
)

coefficient_a = st.sidebar.slider(
    "線性係數 (a)", 
    min_value=-10.0, 
    max_value=10.0, 
    value=2.0, 
    step=0.1,
    help="y = ax + b + noise 中的係數 a"
)

intercept_b = st.sidebar.slider(
    "截距 (b)", 
    min_value=-20.0, 
    max_value=20.0, 
    value=5.0, 
    step=0.5,
    help="y = ax + b + noise 中的截距 b"
)

noise_variance = st.sidebar.slider(
    "雜訊變異數 (var)", 
    min_value=0, 
    max_value=1000, 
    value=100, 
    step=10,
    help="雜訊的變異數，影響資料的分散程度"
)

# 設定隨機種子以確保結果可重現
random_seed = st.sidebar.number_input(
    "隨機種子", 
    min_value=0, 
    max_value=9999, 
    value=42,
    help="設定隨機種子以確保結果可重現"
)

# CRISP-DM 階段標示
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔄 CRISP-DM 階段")
st.sidebar.markdown("✅ 1. 商業理解")
st.sidebar.markdown("✅ 2. 資料理解") 
st.sidebar.markdown("✅ 3. 資料準備")
st.sidebar.markdown("✅ 4. 建模")
st.sidebar.markdown("✅ 5. 評估")
st.sidebar.markdown("✅ 6. 部署")

# 主要內容區域
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📈 線性迴歸視覺化")
    
    # 生成資料 (CRISP-DM 3.0 資料準備)
    np.random.seed(random_seed)
    x = np.random.rand(n_points) * 20 - 10  # x範圍：-10到10
    y_true = coefficient_a * x + intercept_b
    noise = np.random.normal(0, np.sqrt(noise_variance), n_points)
    y = y_true + noise
    
    # 建立DataFrame
    df = pd.DataFrame({'x': x, 'y': y})
    
    # 執行線性迴歸 (CRISP-DM 4.0 建模)
    model = LinearRegression()
    model.fit(x.reshape(-1, 1), y)
    y_pred = model.predict(x.reshape(-1, 1))
    
    # 計算殘差用於離群值檢測 (CRISP-DM 5.0 評估)
    residuals = np.abs(y - y_pred)
    df['residuals'] = residuals
    
    # 識別前5個離群值
    outliers = df.nlargest(5, 'residuals')
    
    # 繪製圖表
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 繪製資料點
    ax.scatter(df['x'], df['y'], 
               alpha=0.6, 
               s=30, 
               color='blue', 
               label=f'資料點 (n={n_points})')
    
    # 繪製迴歸線 (紅色)
    ax.plot(df['x'], y_pred, 
            color='red', 
            linewidth=3, 
            label='線性迴歸線')
    
    # 標記離群值
    for i, (idx, row) in enumerate(outliers.iterrows()):
        ax.annotate(f'離群值 {i+1}', 
                   (row['x'], row['y']), 
                   textcoords="offset points", 
                   xytext=(0, 15), 
                   ha='center', 
                   color='purple',
                   fontweight='bold')
        ax.scatter(row['x'], row['y'], 
                  color='purple', 
                  s=150, 
                  edgecolors='black', 
                  linewidth=2,
                  zorder=5)
    
    ax.set_xlabel("X 值", fontsize=12)
    ax.set_ylabel("Y 值", fontsize=12)
    ax.set_title(f"線性迴歸分析 (y = {coefficient_a:.1f}x + {intercept_b:.1f} + noise)", 
                fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    st.pyplot(fig)

with col2:
    st.subheader("📊 模型結果")
    
    # 顯示模型係數
    st.markdown("### 🎯 迴歸係數")
    st.metric("斜率 (a)", f"{model.coef_[0]:.3f}")
    st.metric("截距 (b)", f"{model.intercept_:.3f}")
    
    # 計算R²分數
    from sklearn.metrics import r2_score
    r2 = r2_score(y, y_pred)
    st.metric("R² 分數", f"{r2:.3f}")
    
    # 顯示離群值資訊
    st.markdown("### 🔍 前5個離群值")
    outliers_display = outliers[['x', 'y', 'residuals']].copy()
    outliers_display.columns = ['X值', 'Y值', '殘差']
    outliers_display.index = [f'離群值 {i+1}' for i in range(len(outliers_display))]
    st.dataframe(outliers_display.round(3), use_container_width=True)

# 底部資訊
st.markdown("---")
st.markdown("### 📋 CRISP-DM 方法論說明")
st.markdown("""
**CRISP-DM (Cross-Industry Standard Process for Data Mining)** 是資料探勘的標準流程：

1. **商業理解** - 定義專案目標和需求
2. **資料理解** - 收集和探索資料
3. **資料準備** - 清理和轉換資料
4. **建模** - 建立預測模型
5. **評估** - 評估模型效果
6. **部署** - 部署和監控模型

本範例展示了完整的CRISP-DM流程，從資料生成到模型部署的互動式體驗。
""")
