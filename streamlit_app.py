# Streamlit 線性回歸互動演示
# 透過滑桿調整模型參數並即時可視化

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# 設定頁面配置
st.set_page_config(
    page_title="線性回歸互動演示",
    page_icon="📊",
    layout="wide"
)

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

def generate_data(n_points, coefficient, noise_level):
    """生成線性回歸數據"""
    np.random.seed(42)  # 固定種子確保可重現性
    
    # 生成X數據 (1-8秒的載入時間)
    X = np.random.uniform(1, 8, n_points).reshape(-1, 1)
    
    # 生成Y數據: y = ax + b + noise
    intercept = 0.1  # 固定截距
    y = intercept + coefficient * X.flatten() + np.random.normal(0, noise_level, n_points)
    
    # 限制Y在合理範圍內
    y = np.clip(y, 0.05, 0.9)
    
    return X, y

def train_model(X, y):
    """訓練線性回歸模型"""
    model = LinearRegression()
    model.fit(X, y)
    return model

def create_plot(X, y, model, coefficient, noise_level):
    """創建可視化圖表"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # 左圖：數據點和回歸線
    ax1.scatter(X, y, alpha=0.6, color='blue', s=30, label='數據點')
    
    # 繪製回歸線
    X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    y_range = model.predict(X_range)
    ax1.plot(X_range, y_range, color='red', linewidth=2, label='回歸線')
    
    ax1.set_xlabel('載入時間 (秒)')
    ax1.set_ylabel('跳出率')
    ax1.set_title(f'線性回歸模型\n(係數={coefficient:.2f}, 噪聲={noise_level:.2f})')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 右圖：殘差圖
    y_pred = model.predict(X)
    residuals = y - y_pred
    ax2.scatter(y_pred, residuals, alpha=0.6, color='green', s=30)
    ax2.axhline(y=0, color='red', linestyle='--')
    ax2.set_xlabel('預測值')
    ax2.set_ylabel('殘差')
    ax2.set_title('殘差分布')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

# 主應用程式
def main():
    st.title("📊 線性回歸互動演示")
    st.markdown("---")
    
    # 側邊欄 - 參數調整
    st.sidebar.header("🎛️ 模型參數調整")
    
    # 滑桿1：數據點數量
    n_points = st.sidebar.slider(
        "數據點數量",
        min_value=50,
        max_value=500,
        value=200,
        step=10,
        help="調整數據集的樣本數量"
    )
    
    # 滑桿2：係數a
    coefficient = st.sidebar.slider(
        "係數 a (y=ax+b+noise)",
        min_value=0.05,
        max_value=0.25,
        value=0.12,
        step=0.01,
        help="調整線性關係的斜率"
    )
    
    # 滑桿3：噪聲水平
    noise_level = st.sidebar.slider(
        "噪聲水平",
        min_value=0.01,
        max_value=0.15,
        value=0.05,
        step=0.01,
        help="調整數據的隨機噪聲"
    )
    
    # 生成數據
    X, y = generate_data(n_points, coefficient, noise_level)
    
    # 訓練模型
    model = train_model(X, y)
    
    # 計算模型指標
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    
    # 顯示模型資訊
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("R² 分數", f"{r2:.3f}")
    
    with col2:
        st.metric("RMSE", f"{rmse:.3f}")
    
    with col3:
        st.metric("數據點數", n_points)
    
    # 顯示回歸方程式
    slope = model.coef_[0]
    intercept = model.intercept_
    st.info(f"**回歸方程式**: y = {intercept:.3f} + {slope:.3f}x")
    
    # 顯示圖表
    fig = create_plot(X, y, model, coefficient, noise_level)
    st.pyplot(fig)
    
    # 預測示範
    st.subheader("🔮 預測示範")
    col1, col2, col3 = st.columns(3)
    
    test_values = [2, 4, 6]
    for i, val in enumerate(test_values):
        pred = model.predict([[val]])[0]
        with [col1, col2, col3][i]:
            st.metric(f"載入時間 {val}秒", f"{pred:.3f}")
    
    # 說明
    st.markdown("---")
    st.markdown("""
    ### 📝 使用說明
    - **數據點數量**: 調整數據集的樣本數量，影響模型的穩定性
    - **係數 a**: 調整線性關係的強度，數值越大表示載入時間對跳出率的影響越明顯
    - **噪聲水平**: 調整數據的隨機性，噪聲越大模型越難擬合
    """)

if __name__ == "__main__":
    main()
