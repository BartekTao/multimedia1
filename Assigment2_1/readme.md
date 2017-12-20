# Assignment2
> 陶柏年 410225030

文件格式
---
> 由於音樂的節拍有很種種類，像是一拍、半拍、兩拍、三連音等等...在此作業中，只顧及到較常見的**整數節拍**，例如 : 一拍、兩拍、三拍...

> 格式 : 
> 1. 數字1-7代表Do-Si，與簡譜代表意思相同
> 2. 符號 - 代表拉長音
> `EX. 123-`
> 唱名為 : Do(一拍) Re(一拍) Mi(**兩拍**)

>工具:
>python

程序流程圖
---
![](https://upload.cc/i/k9uHLs.png)

運行方式
---
輸入要讀取之檔案的路徑+檔名+副檔名(ex.D:\影像處理\Assigment2\music.txt)

演示
---
![](https://upload.cc/i/nG1d9t.png)
![](https://upload.cc/i/OXKoDP.png)

學習心得
---
這次是第一次使用**python**處理音樂，一開始真的沒什麼頭緒，不知道要從何開始，google了許多資料...那以下大略是我實作的幾個階段

**一.基本演示**
>簡單使用winsound，測試使用python播出指定頻率之聲音，發現是可行的，只是卻不知道如何合併及調整音樂間隔

**二.pyaudio**
>找到另一個工具pyaudio，但是卻不知道該如何使用自己設定的sin函數...

**三.scipy**
>後來使用了scipy函數解決的以上問題，只是在輸出成wav方面卻卡了很久很久，因為type以及編碼的問題，導致我輸出的wav檔案一直有沙沙沙的雜音，最後使用以下方法終於成功導出無沙沙聲的wav檔
>`samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
>newdata = volume*samples.astype(np.float32)
>scipy.io.wavfile.write("output.wav",fs, newdata)`

**四.開始實作**
>一開始的實作寫的程式比較沒有系統，只做出了功能，最後才調整成可以讀取符合格式的txt檔(我還寫了篩選txt的機制，若txt不符合格式，程式碼會自動將他調整成符合的格式)，只是我認為取樣頻率、休息間隔、每一拍持續的時間、主音與伴奏的聲音大小，應該都要改成可以被使用的人調整的方式，也就是如果有個UI可以給使用者去設定會更好，再更好的話或許可以不只輸出wav檔，也可以輸出音樂的樂譜(我有找到類式的資源)，因為我會一些的樂器，所以這次作業讓我有蠻多發想的，有時間可以研究一些製作音樂的軟體，或許會有更多的幫助。

結果
---
音樂取自:聖誕歌的前四小節(前16拍)

* **比較一**
**比較主音與伴奏是否有dalay，會不會導致分辨不出兩個聲音**
#取樣頻率fs = 8000
[samples1.wav](https://drive.google.com/open?id=1mLCM-1j4EuHvLqzi4zzM8d6wUlapFECu)(主音與伴奏無dalay)
![](https://upload.cc/i/l1kBnT.png)
[samples2.wav](https://drive.google.com/open?id=1mLCM-1j4EuHvLqzi4zzM8d6wUlapFECu)(主音與伴奏有dalay)
![](https://upload.cc/i/EcKtjn.png)

>個人認為以上兩個街分辨得出有兩個聲音，以音樂的角度來看，和音(伴奏)是否與主旋律(主音)同時出現是沒有差別的，個別是獨立的。

* **比較二**
**比較取樣頻率不同會導致什麼結果**
#取樣頻率fs = 80
[samples4.wav](https://drive.google.com/open?id=1PL7IWCCVIoi2Q41s7xBugv-ak1Omht0n)
![](https://upload.cc/i/9BkTxV.png)
#取樣頻率fs = 200
[samples5.wav](https://drive.google.com/open?id=1Y_Z-MqXf_5w9H0tJMlUDzKOVCIMnnO7o)
![](https://upload.cc/i/wV3Rus.png)
#取樣頻率fs = 500
[samples6.wav](https://drive.google.com/open?id=1FX-YGvngzQSAFFrLlW3rekLsXQahPjfd)
![](https://upload.cc/i/RoYD2b.png)
#取樣頻率fs = 800
[samples3.wav](https://drive.google.com/open?id=167vgSAV7Oefm1dROX0lfgaqjabHc4awQ)
![](https://upload.cc/i/nWAd8S.png)
#取樣頻率fs = 8000
[samples2.wav](https://drive.google.com/open?id=1mLCM-1j4EuHvLqzi4zzM8d6wUlapFECu)
![](https://upload.cc/i/EcKtjn.png)
#取樣頻率fs = 20000
[samples7.wav](https://drive.google.com/open?id=1A4fvb9J2yr9XHEim2z1xdv-qc_pt_7oK)
![](https://upload.cc/i/U7BPHo.png)
#取樣頻率fs = 80000
[samples7.wav](https://drive.google.com/open?id=1KQME5euhJqDybzRO4ZvdInQ2FcNUmJQf)
![](https://upload.cc/i/YEiql3.png)

>以公式來說:取樣頻率(fs)>2f(音樂頻率)
>以我們這次有使用到的最高頻率f=392Hz為基準:取樣頻率約需要大於800
>我們可以看到:
>1.fs=80時，聽不到任何聲音
>
>2.fs=200、500，大致可以猜出是哪幾個音，但是失真率很大，低音較低沉、抖動，高音也會破音
>
>3.當fs>800時，越大聲音越扎實，但是也間接凸顯了一個問題，在音樂與休息間隔轉換時，出現越來越明顯的雜訊，這個問題聽老師說好像要使用濾波器才能解決，在此就沒有再更深入探討
