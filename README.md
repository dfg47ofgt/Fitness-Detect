## 專案名稱 
Fitness-detect健身偵探

## 專案介紹
一款屬於自主重量訓練使用者專用的健身系統，主要經由「深度學習」、「影像辨識」技術開發，同時開發使用者介面，好讓使用者觀察自己的重訓次數、運動狀況、日期、身體組成等紀錄，提升優化使用體驗。透過使用者顯示 QR Code，以登入連結我們的伺服器，再由雲端運算的架構，即時辨識使用者不同的運動姿勢，並在 Web 上做顯示，同時也將運動次數紀錄在資料庫中，並回傳至該使用者的行動裝置中。使用者能透過「Fitness Det.健身偵探 」中的運動記錄圖表功能、日曆影像檢閱功能，得知該使用者過去的運動狀況變化及過去運動影像。我們希望透過此系統能夠帶給使用者更輕省且優化的運動體驗。
但由於部分檔案都有連接資料庫與server，所以直接下載無法完全跑起來。

## 檔案為Front end(前端code),PoseEstimationProject,Demo
Front end 部分為網頁前端，包括html、css、js、php檔案。主要內容是使用者介面，我們採用RWD網頁架構，讓不同裝置的使用者都可以去使用。網頁的頁面包刮開始運動QRODE、日歷(可以去看過往的運動歷程、次數、影片)、計算BMI小工具、遊玩遊戲QRCODE、使用者登入介面、設定運動目標、主畫面。
PoseEstimationProject 部分為系統的後端。使用python語言做開發，透過blazePose模型為主軸應用在健身的影像辨識中。檔案包誇掃描QRCODE做使用者登入、識別健身姿勢、健身小遊戲、連接SQL。
Demo 為一些blazePose模型應用於我們系統後的一些影片展示。包括實際使用歷程、辨識運動的動作、運動小遊戲。

## 開發工具、環境
Anaconda3（Python）
Visual Studio Code (CSS、HTML、JS、PHP)
SQL Server、llS
Adobe XD、Adobe Illustrate
使用到的技術包誇:
BlazePose
Fitness Det. 姿勢辨識 (我們自主開發的運動影像姿勢辨識的方法)
WebSocket API (應用於即時接收使用者運動影像來做姿勢辨識)
Flask Web API (將辨識結果即時呈現在Web上做觀看)
RWD 網頁架構


## 技術介紹、系統架構
blazePose模型為一款人體姿勢感測方法，是利用機器學習推測人體33個2D特徵點，在單個影格標記人體姿勢。相比於其他應用於人體特徵點提取的模型像是AlphaPose、OpenPose，它的優點在於它是一個輕量化模型，透過CPU就可以跑出30禎以上的數據。我們透過這些2D特徵點去計算使用者的面相、移動軌跡、運動角度、關節角度來達到識別目前使用者的運動狀態。整個系統的流程主要會先透過Webcame即時接收影像，再透過AI server去辨識使用者的運動狀態(blazepose提取人體關節點、Fitness Det. 姿勢辨識)，同時也將即時結果記錄在資料庫並顯示於Web上觀看，當使用者要停止運動即可在網頁上點選終止運動按鈕，系統就會自動儲存運動的所有歷程於我們的資料庫中，使用者可以透過登入自己的帳號來觀看先前的運動影像、運動次數、運動歷程等等。

## Demo
運動姿態辨識

![1_AdobeExpress](https://github.com/dfg47ofgt/fitness-detect/assets/79782178/84270300-9a8c-4255-a8a6-19fe3762c578)
![運動姿態辨識_AdobeExpress](https://github.com/dfg47ofgt/fitness-detect/assets/79782178/fd0d3ab1-dc10-4f00-8a9e-d2643464ffb1)

健身挑戰小遊戲

![60秒挑戰_Trim_AdobeExpress](https://github.com/dfg47ofgt/fitness-detect/assets/79782178/65225010-3c86-4a78-b070-1bf68f40f40f)
![極限挑戰new_Trim_AdobeExpress](https://github.com/dfg47ofgt/fitness-detect/assets/79782178/d6c98fc7-0b79-43d8-b92b-77d3e8d8a519)



















