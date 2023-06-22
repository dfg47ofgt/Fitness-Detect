## 專案名稱 
**Fitness-detect健身偵探**

## 專案介紹
Fitness-detect健身偵探是一款專為自主重量訓練使用者設計的健身系統，採用深度學習與影像辨識技術開發，並同時優化了使用者介面，讓使用者可以清楚追蹤自己的訓練情況，包括訓練次數、運動狀況、日期及身體組成等紀錄。系統能透過使用者掃描QR Code連結我們的伺服器，進行即時運動姿勢辨識並將結果顯示在網頁上，並將訓練數據保存在資料庫中。我們的目標是提供使用者更輕鬆且優化的運動體驗。

> 注意：由於部分文件需要連接資料庫和伺服器，直接下載可能無法正常運行。

## 專案檔案說明
**Front end:** 包含網頁前端的HTML、CSS、JS、PHP檔案。採用RWD網頁架構，優化不同裝置的使用者體驗。網頁主要功能包括掃描QR Code開始運動、查看運動歷程的日曆、計算BMI的小工具、遊戲QR Code、使用者登入介面、設定運動目標及主畫面等。

**PoseEstimationProject:** 系統的後端部分，採用Python語言開發，以BlazePose模型為主進行健身影像辨識。主要功能包括掃描QR Code進行使用者登入、識別健身姿勢、健身小遊戲及連接SQL資料庫等。

**Demo:** 展示BlazePose模型應用於我們系統的實際使用歷程、運動動作辨識及運動小遊戲等影片。

## 開發工具與環境
- Anaconda3（Python）
- Visual Studio Code (CSS、HTML、JS、PHP)
- SQL Server、IIS
- Adobe XD、Adobe Illustrate
- 使用到的技術包括:
  - BlazePose模型
  - Fitness Det. 姿勢辨識 (我們自主開發的運動影像姿勢辨識的方法)
  - WebSocket API (應用於即時接收使用者運動影像進行姿勢辨識)
  - Flask Web API (將辨識結果即時顯示於Web介面)
  - RWD網頁架構

## 技術介紹與系統架構
我們的系統主要以BlazePose模型作為人體姿勢感測的工具，這個模型能推測人體的33個2D特徵點，提供人體姿勢的詳細資訊。與其他人體特徵點提取的模型（例如AlphaPose、OpenPose）相比，BlazePose的優點在於它是一個輕量化模型，僅需CPU即可達到每秒30幀以上的處理效率。

我們的系統首先會透過Webcam即時接收影像，進一步透過AI server辨識使用者的運動狀態。這包括使用BlazePose提取人體關節點，並使用我們自主開發的Fitness Det. 姿勢辨識技術。系統將即時結果記錄在資料庫中並顯示於Web介面，使用者可以隨時停止運動並儲存訓練紀錄。之後，使用者可以登入帳號查看先前的運動影像、運動次數、運動歷程等資訊。


## Demo
運動姿態辨識

![1_AdobeExpress](https://github.com/dfg47ofgt/fitness-detect/assets/79782178/84270300-9a8c-4255-a8a6-19fe3762c578)
![運動姿態辨識_AdobeExpress](https://github.com/dfg47ofgt/fitness-detect/assets/79782178/fd0d3ab1-dc10-4f00-8a9e-d2643464ffb1)

健身挑戰小遊戲

![60秒挑戰_Trim_AdobeExpress](https://github.com/dfg47ofgt/fitness-detect/assets/79782178/65225010-3c86-4a78-b070-1bf68f40f40f)
![極限挑戰new_Trim_AdobeExpress](https://github.com/dfg47ofgt/fitness-detect/assets/79782178/d6c98fc7-0b79-43d8-b92b-77d3e8d8a519)



















