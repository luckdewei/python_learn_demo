# 安装依赖：uv add PyMuPDF
import fitz  # PyMuPDF


# 定义一个函数用于提取PDF文件中的所有文本内容
def extract_pdf_text(pdf_path):
    """
    提取PDF文件中的所有文本内容

    参数:
        pdf_path (str): PDF文件路径

    返回:
        str: 合并后的所有页文本
    """
    # 打开PDF文件
    pdf = fitz.open(pdf_path)
    # 创建一个空列表用于存放每一页的文本内容
    text_list = []
    # 遍历PDF中的每一页
    for page in pdf:
        # 提取当前页的文本内容，并添加到列表中
        text_list.append(page.get_text("text"))  # type: ignore
    # 将所有页的文本内容合并为一个字符串
    all_text = "\n".join(text_list)
    # 返回合并后的文本
    return all_text


# 主程序入口，进行测试调用
if __name__ == "__main__":
    # 指定要读取的PDF文件名
    pdf_file = "example.pdf"
    # 调用函数提取PDF文本
    result_text = extract_pdf_text(pdf_file)
    # 打印提取到的文本内容
    print(result_text)
