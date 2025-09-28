# CRISP-DM 線性迴歸專案

## 1. Project 介紹

本專案是一個應用Cursor AI + Prompt生成的專案。
基於CRISP-DM 方法論開發的互動式線性迴歸教學範例。專案使用Streamlit框架建立現代化的網頁應用程式，提供線性回歸模型建立流程體驗。

專案包含兩個主要應用程式：簡單線性迴歸和多元迴歸。簡單線性迴歸展示單一特徵的迴歸分析 (y = ax + b + noise)，而多元迴歸則擴展至雙特徵模型 (y = ax₁ + bx₂ + c + noise)。每個應用程式都提供即時的參數調整、視覺化圖表和模型評估功能，讓使用者能夠深入理解線性迴歸的原理和應用。

## 2. Demo Site

**簡單線性迴歸**: https://aiothw1-123.streamlit.app/
- 單一特徵迴歸模型 (y = ax + b + noise)
- 2D散點圖與迴歸線視覺化

**多元迴歸**: https://aiothw1-1231.streamlit.app/
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

## 5. Prompt
prompt 1.
```text
以CRISP_DM方式, 建立可在streamlit框架下的可互動simple linear regression example. 
請勿將問題複雜化, 以簡易可懂方式生成程序碼. 
建立過程需紀錄每個步驟的log. 所有生成檔案放在HW1\folder下.
code詳細規則如下:
1.  **Data Generation:**
    -   Generate `n` data points (x, y) where `n` is a user-selectable value between 100 and 1000.
    -   The relationship between x and y will be defined by `y = ax + b + noise`.
    -   `a`: User-selectable coefficient between -10 and 10.
    -   `noise`: Normally distributed noise `N(0, var)`, where `var` (variance) is user-selectable between 0 and 1000.

2.  **Linear Regression Visualization:**
    -   Plot the generated data points.
    -   Draw the calculated linear regression line in **red**.

3.  **Outlier Identification:**
    -   Identify and label the top 5 outliers (points furthest from the regression line).

4.  **User Interface:**
    -   Implement the application using **Streamlit** for an interactive web interface.
    -   Allow users to adjust parameters (`n`, `a`, `var`) via sliders or input fields.
    -   Display the generated plot and regression results.
```
prompt 2.
```text
現在我想往下延伸, 從simple linear regression變成multiple regression, feature只需要兩個, 因此function = ax1+bx2+c + noise, 沿用linear_regression_app.py相同架構, 生成一份全新的python file. 不要更改原本的python file
```
prompt 3.
```text
幫我重新改寫README.md, 內容分為下面幾大項, 每個內容盡量不超過50字, 精簡說明即可
1. project介紹
2. demo site (內含兩個site, simple linear regression & multiple regression)
3. project summary
4. devlopment Log
```
