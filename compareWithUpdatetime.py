from tkinter import simpledialog,messagebox
import datetime
import os

def main():
    target_excel_file_path = simpledialog.askstring("Input Box", "対象ファイルを指定して",)
    sliced_target_excel_file_path = sliceStartAndEndCharacter(target_excel_file_path)
    comparing_excel_file_path = simpledialog.askstring("Input Box", "比較するファイルを指定して",)
    sliced_comparing_excel_file_path = sliceStartAndEndCharacter(comparing_excel_file_path)

    target_unix_timestamp = os.path.getmtime(sliced_target_excel_file_path)
    comparing_unix_timestamp = os.path.getmtime(sliced_comparing_excel_file_path)
    convert_target_time = datetime.datetime.fromtimestamp(target_unix_timestamp)
    convert_comparing_time = datetime.datetime.fromtimestamp(comparing_unix_timestamp)

    if convert_target_time == convert_comparing_time:
        messagebox.showinfo('確認', '同じだから大丈夫')
    else:
        messagebox.showerror('エラー', 'シートが違うから確認して')

def sliceStartAndEndCharacter(targetString):
    slicedStartCharacterString = targetString[1:]
    slicedEndCharacterString = slicedStartCharacterString[:-1]
    return slicedEndCharacterString

# メイン処理
if __name__ == "__main__":
    main()


