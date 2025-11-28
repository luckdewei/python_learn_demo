# 安装依赖：uv add openpyxl
import openpyxl


# 定义函数：从Excel文件中提取所有单元格内容为文本
def extract_text_from_excel(file_path):
    """
    从Excel文件中提取所有单元格内容为文本，并以字符串返回。
    :param file_path: Excel文件路径
    :return: 文本内容字符串
    """
    # 加载Excel工作簿
    wb = openpyxl.load_workbook(file_path)
    # 获取活动工作表
    ws = wb.active
    # 初始化用于存储每一行文本的列表
    rows = []
    # 遍历工作表中的每一行，values_only=True表示只获取单元格的值
    for row in ws.iter_rows(values_only=True):
        # 将每一行的所有单元格内容转换为字符串，并用制表符分隔，空单元格用空字符串代替
        rows.append("\t".join([str(cell) if cell is not None else "" for cell in row]))
    # 将所有行用换行符拼接为一个大字符串
    all_text = "\n".join(rows)
    # 返回拼接后的文本
    return all_text


# 主程序入口，进行测试调用
if __name__ == "__main__":
    # 指定要读取的Excel文件名
    file_path = "example.xlsx"
    # 调用函数提取Excel文本
    result = extract_text_from_excel(file_path)
    # 打印提取到的文本内容
    print(result)
