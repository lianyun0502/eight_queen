# Eight Queens Question

## Installation

Recommand using python version 3.11.5 and install package with command :

```
pip install -r requirements.txt
```

## 參數說明



| 變數 | 說明 
| --------- | --------- 
| queen_num | 皇后數量
| ans_num   | 總答案數量
| division_8 | 有八種相似答案的答案個數
| division_4 | 有四種相似答案的答案個數
| division_2 | 有二種相似答案的答案個數

## 第一版 ( git commit: 0b4593b360d7f4964e76e37de5019d7dad2003a2 )
* 這版測試不跑獨立解約跑了270秒 **不夠快**

* 分析程式，如果不跑秀出特定格式答案的function大約可以省下20秒的時間，所以要優化效能還是要想辦法優化深度遞迴的演算法。

## 第二版
* 會朝去減少迴圈跌代次數的方向去優化
* 在第一版的時候其實有發現選定某一行之後的列其實每次遞迴都可以少做一列且列照順序遞減就可以了(扣掉重複)，但是卻沒有對行做優化，關於行優化的想法可以不要每次都跌代全部，上一層遞迴有選過的就不需要蝶代，所以可以有一個陣列去紀錄還剩下需要跌代的行有哪些。
* 優化後不跑秀出特定格式答案的結果約為110秒!!約是0.5倍的效率。