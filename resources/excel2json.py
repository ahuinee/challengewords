
import xlrd
import json
excel_path = "../单词.xlsx"

def excel2json():

    data = achieve_data(excel_path)

    if data is not None:
        sheets_names = data.sheet_names()

        wordsList = list()
        wordsDic = {"gradeName":"", "volumes":[]}

        for sheetName in sheets_names:
            dicKeyName = sheetName[0:3]
            
            subDicKeyName = sheetName[3:5]   # "上册"
            
            # 获取 单个 sheet 底下 数据   上册："数据"
            table = data.sheet_by_name(sheetName)
            subDict = dict()
            subDict = {"volumeName": subDicKeyName, "units": decodeTableSheet(table)}
            

            # 设置 三年级 key名称, 如果没有 三年级 类别数据，则先添加 三年级 类别数据
            if (wordsDic["gradeName"].find(dicKeyName)):  # "三年级"
                wordsDic["gradeName"] = dicKeyName
                wordsDic["volumes"] = [subDict]
            else:
                wordsDic["volumes"].append(subDict)
                wordsList.append(wordsDic.copy())

        print("test")
        with open("words.json", 'w', encoding='utf-8') as result:
            # ensure_ascii=False 显示中文
            # indent=4 json格式换行
            json.dump(wordsList, result, ensure_ascii=False, indent=4)
            print("test")

def decodeTableSheet(table):
    try:
        unitDic = dict()
        unitArray = list()
        
        wordsArray = list()
        chineseIndex = 0

        # 循环 列 数据
        for i in range(0, table.ncols):
            col = table.col_values(i)
            
            # 循环 列 组中数据
            for indexj, column in enumerate(col):
                
                if (indexj == 0): # 添加 单元 名
                    if (len(column)>0):
                        wordsArray.clear()
                        unitDic["unitName"] = column
                        chineseIndex = i
                else:
                    if (i==(chineseIndex+1) and len(column)>0): # 添加 英语 列
                        tempEnDic = wordsArray[indexj-1]
                        tempEnDic["english"] = column
                        wordsArray[indexj-1] = tempEnDic
                    else: # 添加 中文 列
                        if (len(column)>0):
                            tempChDic = {"chinese": column}
                            wordsArray.append(tempChDic)
                
                    
            unitDic["words"] = wordsArray.copy()
            if (i == (chineseIndex + 1)):
                unitArray.append(unitDic.copy())
                unitDic = dict()
        
        return unitArray

    except Exception as e:
        print(e)
        return None

def achieve_data(file_path):
    try:
        data = xlrd.open_workbook(file_path)
        return data
    except Exception as e:
        print("excel表格读取失败：%s" % file_path)
        print(e)
        return None

if __name__ == '__main__':
    excel2json()
