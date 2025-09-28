# CRISP-DM 線性迴歸專案開發日誌

## 1.0 CRISP-DM 商業理解階段

### 1.1 分析專案需求
- 建立一個可在Streamlit框架下互動的簡單線性迴歸範例
- 使用者可調整參數：資料點數量(n)、係數(a)、雜訊變異數(var)
- 視覺化資料點、迴歸線和離群值
- 識別並標記前5個離群值

### 1.2 定義專案目標
- 提供教育性的線性迴歸互動體驗
- 讓使用者理解參數對迴歸結果的影響
- 展示離群值檢測的概念

## 2.0 CRISP-DM 資料理解階段

### 2.1 設計資料生成邏輯
- 生成n個資料點，範圍在100-1000之間
- 線性關係：y = ax + b + noise
- 係數a可調整範圍：-10到10
- 雜訊：常態分布N(0, var)，變異數可調整範圍：0到1000

## 3.0 CRISP-DM 資料準備階段

### 3.1 實作資料生成功能
- 使用numpy生成隨機資料點
- 加入可調整的線性關係和雜訊

## 4.0 CRISP-DM 建模階段

### 4.1 實作線性迴歸模型
- 使用sklearn的LinearRegression
- 計算迴歸係數和截距

## 5.0 CRISP-DM 評估階段

### 5.1 實作離群值檢測
- 計算殘差(residuals)
- 識別前5個離群值

### 5.2 實作視覺化
- 使用matplotlib繪製散點圖
- 繪製紅色迴歸線
- 標記離群值

## 6.0 CRISP-DM 部署階段

### 6.1 建立Streamlit互動介面
- 側邊欄參數調整
- 即時更新圖表和結果
- 顯示模型係數和離群值資訊

## 7.0 實作完成

### 7.1 建立主要Streamlit應用程式
- 完成CRISP-DM所有階段的實作
- 實作互動式參數調整
- 實作線性迴歸視覺化
- 實作離群值檢測和標記
- 實作模型結果顯示

### 7.2 應用程式功能
- 使用者可調整資料點數量、係數、截距、雜訊變異數
- 即時更新圖表和模型結果
- 顯示R²分數和離群值資訊
- 完整的CRISP-DM方法論展示

### 7.3 檔案結構
- linear_regression_app.py: 主要Streamlit應用程式
- requirements.txt: 依賴套件清單
- devLog.md: 開發日誌

### 7.4 執行方式
- 安裝依賴: pip install -r requirements.txt
- 執行應用: streamlit run linear_regression_app.py

## 8.0 圖表文字國際化修改

### 8.1 使用者要求修改
- 使用者要求將圖表內部的中文敘述改成英文
- 避免中文字體顯示問題

### 8.2 修改內容
- 將散點圖標籤從 "資料點 (n={n_points})" 改為 "Data Points (n={n_points})"
- 將迴歸線標籤從 "線性迴歸線" 改為 "Linear Regression Line"
- 將離群值標籤從 "離群值 {i+1}" 改為 "Outlier {i+1}"
- 將X軸標籤從 "X 值" 改為 "X Values"
- 將Y軸標籤從 "Y 值" 改為 "Y Values"
- 將圖表標題從 "線性迴歸分析" 改為 "Linear Regression Analysis"

### 8.3 修改完成
- 所有圖表內的中文敘述已成功改為英文
- 保持其他介面元素的中文顯示
- 確保圖表在不同環境下都能正常顯示

## 9.0 多元迴歸延伸開發

### 9.1 使用者需求
- 使用者要求從簡單線性迴歸延伸至多元迴歸
- 特徵數量限制為2個，函數形式：y = ax₁ + bx₂ + c + noise
- 沿用linear_regression_app.py相同架構
- 生成全新的Python檔案，不修改原始檔案

### 9.2 多元迴歸實作
- 建立multiple_regression_app.py檔案
- 實作兩個特徵的多元迴歸模型
- 使用sklearn的LinearRegression處理多維特徵
- 支援係數a、b和截距c的獨立調整

### 9.3 3D視覺化實作
- 使用matplotlib的3D功能繪製散點圖
- 實作迴歸平面視覺化
- 提供2D投影視圖選項（X₁-Y或X₂-Y）
- 標記離群值在3D空間中

### 9.4 功能特色
- 3D散點圖顯示資料點分布
- 紅色迴歸平面展示模型擬合
- 紫色標記前5個離群值
- 2D投影視圖便於理解
- 調整後R²分數計算
- 詳細的資料統計資訊

### 9.5 參數控制
- 資料點數量：100-1000
- 係數a (x₁)：-10到10
- 係數b (x₂)：-10到10
- 截距c：-20到20
- 雜訊變異數：0到1000
- 隨機種子：確保結果可重現

### 9.6 評估指標
- R²分數：模型解釋變異的能力
- 調整後R²：考慮特徵數量的修正R²
- 殘差分析：離群值檢測
- 資料統計：範圍和分布資訊

### 9.7 檔案結構更新
- multiple_regression_app.py: 多元迴歸Streamlit應用程式
- linear_regression_app.py: 原始簡單線性迴歸應用程式
- requirements.txt: 依賴套件清單（已包含3D繪圖支援）
- devLog.md: 開發日誌
- README.md: 專案說明文件

### 9.8 執行方式
- 安裝依賴: pip install -r requirements.txt
- 執行簡單迴歸: streamlit run linear_regression_app.py
- 執行多元迴歸: streamlit run multiple_regression_app.py

## 10.0 README.md 重新改寫

### 10.1 使用者要求
- 使用者要求重新改寫README.md檔案
- 內容分為四大項：Project介紹、Demo Site、Project Summary、Development Log
- 每個內容精簡不超過50字

### 10.2 改寫內容
- Project介紹：基於CRISP-DM方法論的互動式線性迴歸範例說明
- Demo Site：兩個應用程式的執行方式和功能簡介
- Project Summary：技術框架、模型類型、視覺化工具等核心資訊
- Development Log：開發日誌檔案說明

### 10.3 改寫完成
- README.md已重新改寫為精簡版本
- 四大項目內容均控制在50字以內
- 保持重要資訊的完整性

- 提供清晰的專案概覽
