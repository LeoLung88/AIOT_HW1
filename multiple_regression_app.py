import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 設定頁面配置
st.set_page_config(
    page_title="CRISP-DM 多元迴歸範例", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 標題
st.title("🔬 多元迴歸互動範例")
st.markdown("**Multiple Linear Regression: y = ax₁ + bx₂ + c + noise**")
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

# 多元迴歸係數
coefficient_a = st.sidebar.slider(
    "係數 a (x₁)", 
    min_value=-10.0, 
    max_value=10.0, 
    value=2.0, 
    step=0.1,
    help="y = ax₁ + bx₂ + c + noise 中的係數 a"
)

coefficient_b = st.sidebar.slider(
    "係數 b (x₂)", 
    min_value=-10.0, 
    max_value=10.0, 
    value=1.5, 
    step=0.1,
    help="y = ax₁ + bx₂ + c + noise 中的係數 b"
)

intercept_c = st.sidebar.slider(
    "截距 c", 
    min_value=-20.0, 
    max_value=20.0, 
    value=5.0, 
    step=0.5,
    help="y = ax₁ + bx₂ + c + noise 中的截距 c"
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
    st.subheader("📈 多元迴歸視覺化")
    
    # 生成資料 (CRISP-DM 3.0 資料準備)
    np.random.seed(random_seed)
    x1 = np.random.rand(n_points) * 20 - 10  # x1範圍：-10到10
    x2 = np.random.rand(n_points) * 20 - 10  # x2範圍：-10到10
    y_true = coefficient_a * x1 + coefficient_b * x2 + intercept_c
    noise = np.random.normal(0, np.sqrt(noise_variance), n_points)
    y = y_true + noise
    
    # 建立DataFrame
    df = pd.DataFrame({'x1': x1, 'x2': x2, 'y': y})
    
    # 執行多元迴歸 (CRISP-DM 4.0 建模)
    model = LinearRegression()
    X = df[['x1', 'x2']]
    model.fit(X, y)
    y_pred = model.predict(X)
    
    # 計算殘差用於離群值檢測 (CRISP-DM 5.0 評估)
    residuals = np.abs(y - y_pred)
    df['residuals'] = residuals
    
    # 識別前5個離群值
    outliers = df.nlargest(5, 'residuals')
    
    # 建立3D圖表
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 繪製資料點
    ax.scatter(df['x1'], df['x2'], df['y'], 
               alpha=0.6, 
               s=30, 
               color='blue', 
               label=f'Data Points (n={n_points})')
    
    # 建立迴歸平面網格
    x1_range = np.linspace(df['x1'].min(), df['x1'].max(), 20)
    x2_range = np.linspace(df['x2'].min(), df['x2'].max(), 20)
    X1_grid, X2_grid = np.meshgrid(x1_range, x2_range)
    Y_grid = model.coef_[0] * X1_grid + model.coef_[1] * X2_grid + model.intercept_
    
    # 繪製迴歸平面
    ax.plot_surface(X1_grid, X2_grid, Y_grid, 
                    alpha=0.3, 
                    color='red', 
                    label='Regression Plane')
    
    # 標記離群值
    for i, (idx, row) in enumerate(outliers.iterrows()):
        ax.scatter(row['x1'], row['x2'], row['y'], 
                  color='purple', 
                  s=200, 
                  edgecolors='black', 
                  linewidth=2,
                  zorder=5)
        ax.text(row['x1'], row['x2'], row['y'], 
               f'Outlier {i+1}', 
               fontsize=8, 
               color='purple',
               fontweight='bold')
    
    ax.set_xlabel("X₁ Values", fontsize=12)
    ax.set_ylabel("X₂ Values", fontsize=12)
    ax.set_zlabel("Y Values", fontsize=12)
    ax.set_title(f"Multiple Linear Regression (y = {coefficient_a:.1f}x₁ + {coefficient_b:.1f}x₂ + {intercept_c:.1f} + noise)", 
                fontsize=14, fontweight='bold')
    
    st.pyplot(fig)
    
    # 2D投影圖表
    st.subheader("📊 2D 投影視圖")
    
    # 選擇投影軸
    projection_axis = st.selectbox("選擇投影軸", ["X₁-Y", "X₂-Y"])
    
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    
    if projection_axis == "X₁-Y":
        ax2.scatter(df['x1'], df['y'], alpha=0.6, s=30, color='blue', label='Data Points')
        
        # 繪製投影迴歸線
        x1_sorted = np.sort(df['x1'])
        y_proj = model.coef_[0] * x1_sorted + model.coef_[1] * df['x2'].mean() + model.intercept_
        ax2.plot(x1_sorted, y_proj, color='red', linewidth=3, label='Projected Regression Line')
        
        # 標記離群值
        for i, (idx, row) in enumerate(outliers.iterrows()):
            ax2.scatter(row['x1'], row['y'], color='purple', s=150, edgecolors='black', linewidth=2, zorder=5)
            ax2.annotate(f'Outlier {i+1}', (row['x1'], row['y']), 
                        textcoords="offset points", xytext=(0, 15), ha='center', color='purple', fontweight='bold')
        
        ax2.set_xlabel("X₁ Values", fontsize=12)
        ax2.set_ylabel("Y Values", fontsize=12)
        ax2.set_title("X₁-Y Projection", fontsize=14, fontweight='bold')
        
    else:  # X₂-Y
        ax2.scatter(df['x2'], df['y'], alpha=0.6, s=30, color='blue', label='Data Points')
        
        # 繪製投影迴歸線
        x2_sorted = np.sort(df['x2'])
        y_proj = model.coef_[0] * df['x1'].mean() + model.coef_[1] * x2_sorted + model.intercept_
        ax2.plot(x2_sorted, y_proj, color='red', linewidth=3, label='Projected Regression Line')
        
        # 標記離群值
        for i, (idx, row) in enumerate(outliers.iterrows()):
            ax2.scatter(row['x2'], row['y'], color='purple', s=150, edgecolors='black', linewidth=2, zorder=5)
            ax2.annotate(f'Outlier {i+1}', (row['x2'], row['y']), 
                        textcoords="offset points", xytext=(0, 15), ha='center', color='purple', fontweight='bold')
        
        ax2.set_xlabel("X₂ Values", fontsize=12)
        ax2.set_ylabel("Y Values", fontsize=12)
        ax2.set_title("X₂-Y Projection", fontsize=14, fontweight='bold')
    
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    st.pyplot(fig2)

with col2:
    st.subheader("📊 模型結果")
    
    # 顯示模型係數
    st.markdown("### 🎯 迴歸係數")
    st.metric("係數 a (x₁)", f"{model.coef_[0]:.3f}")
    st.metric("係數 b (x₂)", f"{model.coef_[1]:.3f}")
    st.metric("截距 c", f"{model.intercept_:.3f}")
    
    # 計算R²分數
    r2 = r2_score(y, y_pred)
    st.metric("R² 分數", f"{r2:.3f}")
    
    # 計算調整後R²
    n = len(y)
    p = 2  # 特徵數量
    adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
    st.metric("調整後 R²", f"{adj_r2:.3f}")
    
    # 顯示離群值資訊
    st.markdown("### 🔍 前5個離群值")
    outliers_display = outliers[['x1', 'x2', 'y', 'residuals']].copy()
    outliers_display.columns = ['X₁值', 'X₂值', 'Y值', '殘差']
    outliers_display.index = [f'離群值 {i+1}' for i in range(len(outliers_display))]
    st.dataframe(outliers_display.round(3), use_container_width=True)
    
    # 顯示資料統計
    st.markdown("### 📈 資料統計")
    st.write(f"資料點總數: {n_points}")
    st.write(f"X₁ 範圍: [{df['x1'].min():.2f}, {df['x1'].max():.2f}]")
    st.write(f"X₂ 範圍: [{df['x2'].min():.2f}, {df['x2'].max():.2f}]")
    st.write(f"Y 範圍: [{df['y'].min():.2f}, {df['y'].max():.2f}]")

# 底部資訊
st.markdown("---")
st.markdown("### 📋 多元迴歸說明")
st.markdown("""
**多元線性迴歸 (Multiple Linear Regression)** 是簡單線性迴歸的延伸：

- **模型公式**: y = ax₁ + bx₂ + c + noise
- **特徵數量**: 2個獨立變數 (x₁, x₂)
- **視覺化**: 3D散點圖 + 迴歸平面
- **評估指標**: R²、調整後R²、殘差分析

**與簡單線性迴歸的差異**：
- 簡單迴歸: y = ax + b + noise (1個特徵)
- 多元迴歸: y = ax₁ + bx₂ + c + noise (2個特徵)

本範例展示了完整的CRISP-DM流程在多元迴歸中的應用。
""")
