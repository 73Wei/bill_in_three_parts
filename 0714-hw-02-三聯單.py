"""
# 73 WEI
2.三聯單

Entry 數量            Entry 單價

Button 計算
Label  金額
Label  銷售合計金額
Label  營業稅
Label   總計 
Label   總計的中文

"""
print("=====第二題：三聯單=====")

import tkinter as tk                           # 在Python 3.x 匯入該tkinter 函式庫
from PIL import ImageTk, Image
win = tk.Tk()                                   # 步驟2：建立GUI 應用程式的主視窗

win.resizable(width=False, height=False)        # 是否可以調整 (最大和最小設定一樣)
win.minsize(width=928, height=528)              # 最小的視窗
win.maxsize(width=928, height=528)              # 最大的視窗
win.wm_title("0714-HW02-三聯單")                 # 設定主視窗標題


x=Image.open("三聯單-01.jpg")                    # 讀取圖片
img = ImageTk.PhotoImage(x)                     # 轉換成PhotoImage
label1 =tk.Label(win, image = img)              # 建立Label物件 顯示圖片
label1.pack()

# 建立文字
label1 =tk.Label(win,text="XX管理顧問社",font=("微軟正黑體",16))
label1.place(x=150, y=40)
label2 =tk.Label(win,text="42364761",font=("微軟正黑體",16),width=17)
label2.place(x=150, y=80)
label3 =tk.Label(win,text="中華民國  07 月 16 日",font=("微軟正黑體",20))
label3.place(x=600, y=80)
label4 =tk.Label(win,text="顧問服務費",font=("微軟正黑體",10))
label4.place(x=120, y=160)


# 1.2新增輸入框Entry

entryQuantity = tk.StringVar()
entry1=tk.Entry(win,textvariable = entryQuantity,bg="#DCDCDC",width=8)
entry1.place(x=300, y=162)

entryPrice = tk.StringVar()
entry2=tk.Entry(win,textvariable = entryPrice,bg="#DCDCDC",width=8)
entry2.place(x=380, y=162)


# 3.label 金額
labelAmount = tk.StringVar()
labelA =tk.Label(win,text="用戶輸入的資料", textvariable=labelAmount,font=("微軟正黑體",10))
labelAmount.set("金額")
labelA.place(x=500, y=160)

# 4.label 銷售額合計
labeltotal = tk.StringVar()
labelT =tk.Label(win,text="用戶輸入的資料", textvariable=labeltotal,font=("微軟正黑體",10))
labeltotal.set("合計")
labelT.place(x=500, y=292)

#5.營業稅
labelTax = tk.StringVar()
labelTx =tk.Label(win,text="用戶輸入的資料", textvariable=labelTax,font=("微軟正黑體",10))
labelTax.set("稅額")
labelTx.place(x=500, y=340)

# 6.label 總計
labeltotal2 = tk.StringVar()
labelT2 =tk.Label(win,text="用戶輸入的資料", textvariable=labeltotal2,font=("微軟正黑體",10))
labeltotal2.set("總計")
labelT2.place(x=500, y=370)

def tripleSheet():
    global entryQuantity                                 # 1.新增輸入框Entry
    global entryPrice                                    # 2.新增輸入框Entry
    global labelAmount                                   # 3.金額
    global labeltotal                                    # 4.銷售額合計
    global labelTax                                      # 5.營業稅
    global labeltotal2                                   # 6.總計
    global labelChinese                                  # 8.總計新臺幣

    getQuantity = entryQuantity.get()                    # 1.取得entryQuantity上的文字
    getPrice = entryPrice.get()                          # 2.取得entryPrice上的文字

    x = int(getQuantity)                                 # 字串轉為數值
    y = int(getPrice)
                                                         # 因為只有一樣 可以這樣寫 如果有很多樣可以用 list 和 for in 的方式寫

    labelAmount.set(str(x * y))                          # 3.設定 labelAmount    的文字
    labeltotal.set(str(x * y))                           # 4.設定 labeltotal     的文字

    labelTax.set(str(round((x * y * 5) / 100)))          # 5.設定 labelTax       的文字  round 表示四捨五入
    z = (int(round((x * y * 5) / 100)))
    labeltotal2.set(str(x * y + z))                      # 6.設定 labeltotal2    的文字
    num1=int(str(x * y + z))
    labelChinese.set(numberToChinese(num1))


# 數字- 0-99999999 轉 國字

def numberToChinese(n):
    list1 = ["元 ", "拾", "佰", "仟", "萬", "拾", "佰", "仟", "億"]
    list2 = ["零", "壹", "貳", "參", "肆", "伍", "陸", "柒", "捌", "玖"]

    n = int((labeltotal2.get()))  # 6-1帶入 labeltotal2    的文字

    str1 = ""
    digit = 0
    while n > 0:
        n1 = n % 10  # 把取完整數的數字 取除以10的餘數(低位數)---- 從低位數開始處理
        n = n // 10  # 把數字n 拿去除以10 取整數 (高位數)
        # 處理位數
        str1 = list1[digit] + str1  # 因為是從低位數開始處理 會一直把算出來的數字往右推 所以加一個空白字串在右邊
        # 處理數字
        if n1 >= 0 and n1 <= 9:  # 如果是數字 1-9
            str1 = list2[n1] + str1  # 就幫我在表單2中找到對應的數字 並加一個空白字串給他(往右推顯示)
        digit = digit + 1  # 要把位數 加 1

    return str1

# 7.按鈕
btn1=tk.Button(win,text="點我\n計算",width=10,height=5,bg="#D0D0D0",command=tripleSheet)
btn1.place(x=350,y=190)

# 8.label 總計新臺幣 轉大寫
labelChinese = tk.StringVar()
labelC =tk.Label(win,text="用戶輸入的資料", textvariable=labelChinese,font=("微軟正黑體",16))
labelChinese.set("新臺幣")
labelC.place(x=250, y=420)


win.mainloop()                     # 最後步驟：程式做無限循環(關掉視窗才能執行這一行)

