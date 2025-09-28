# AIOT_HW1
# CRISP-DM 線性迴歸專案

## 1. Project 介紹

本專案是一個基於CRISP-DM 方法論開發的互動式線性迴歸教學範例。專案使用Streamlit框架建立現代化的網頁應用程式，提供線性回歸模型建立流程體驗。

專案包含兩個主要應用程式：簡單線性迴歸和多元迴歸。簡單線性迴歸展示單一特徵的迴歸分析 (y = ax + b + noise)，而多元迴歸則擴展至雙特徵模型 (y = ax₁ + bx₂ + c + noise)。每個應用程式都提供即時的參數調整、視覺化圖表和模型評估功能，讓使用者能夠深入理解線性迴歸的原理和應用。

## 2. Demo Site

**簡單線性迴歸**: `streamlit run linear_regression_app.py`
- 單一特徵迴歸模型 (y = ax + b + noise)
- 2D散點圖與迴歸線視覺化

**多元迴歸**: `streamlit run multiple_regression_app.py`
- 雙特徵迴歸模型 (y = ax₁ + bx₂ + c + noise)
- 3D散點圖與迴歸平面視覺化

## 3. Project Summary

**程式架構**:
- `linear_regression_app.py`: 簡單線性迴歸應用程式，使用2D matplotlib視覺化
- `multiple_regression_app.py`: 多元迴歸應用程式，使用3D matplotlib視覺化
- `requirements.txt`: Python依賴套件清單
- `devLog.md`: 詳細開發日誌記錄

**使用工具**:
- **Streamlit**: 網頁應用程式框架，提供互動式使用者介面
- **NumPy**: 數值計算和資料生成
- **Pandas**: 資料處理和DataFrame操作
- **Matplotlib**: 2D/3D圖表繪製和視覺化
- **Scikit-learn**: 機器學習模型 (LinearRegression)
- **mpl_toolkits.mplot3d**: 3D繪圖支援

## 4. Development Log

1.0-2.0: 初始設定，包括建立開發日誌 (devLog.md) 和 requirements.txt 檔案。
3.0-6.0: CRISP-DM 方法論實作，涵蓋商業理解、資料理解、資料準備、建模、評估和部署階段。
7.0: 完成主要 Streamlit 應用程式，包含互動式參數調整和視覺化功能。
8.0: 圖表文字國際化修改，將中文標籤轉換為英文以避免顯示問題。
9.0: 多元迴歸延伸開發，建立具有 3D 視覺化功能的新應用程式。
10.0: README.md 重新改寫和重構，以提供更好的專案文檔。
