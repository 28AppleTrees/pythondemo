import os
import pdf2image  # 更正导入方式
from docx import Document
# import pytesseract # 不再需要 pytesseract
from paddleocr import PaddleOCR  # 导入 PaddleOCR

# --- 初始化 PaddleOCR ---
# 第一次运行时会自动下载模型，可能需要一些时间
# use_angle_cls=True 会启用方向分类器
# lang='ch' 设置为中文识别（支持中英文）
# show_log=False 可以减少控制台输出
# use_gpu=False 明确指定使用CPU，如果你有GPU并配置好了，可以设为True
ocr_engine = PaddleOCR(use_angle_cls=True, lang='ch')


def ocr_pdf_to_word_paddle(pdf_path, word_path=None, poppler_path=None):  # 移除了 tesseract 相关参数
    """ 使用 PaddleOCR 将PDF转换为Word """
    if not os.path.exists(pdf_path):
        print(f"文件 {pdf_path} 不存在。")
        return False

    if not word_path:
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        word_path = f"{base_name}_paddle_ocr.docx"

    try:
        # Step 1: 将PDF转换为图片列表 (需要Poppler)
        # 注意：poppler_path 仍然是需要的
        pages = pdf2image.convert_from_path(pdf_path, dpi=200, poppler_path=poppler_path)

        # Step 2: 创建Word文档
        doc = Document()

        # Step 3: 遍历图片，执行 PaddleOCR，并将结果写入Word
        for i, page_image in enumerate(pages):
            print(f"正在对第 {i + 1} 页进行 PaddleOCR 识别...")

            # 使用 PaddleOCR 进行OCR识别
            # result 是一个列表，包含检测到的文本框信息 [[[[x1,y1],[x2,y2],[x3,y3],[x4,y4]], score, text], ...]
            result = ocr_engine.ocr(page_image, cls=True)

            page_text_content = ""
            if result and result[0]:  # 检查结果是否为空列表或包含空元素
                # 遍历识别结果，拼接文本
                # result[0] 是第一页的结果
                for line_info in result[0]:
                    # line_info[1][0] 是识别出的文本
                    detected_text = line_info[1][0]
                    page_text_content += detected_text + "\n"  # 用换行符连接每一行

            if page_text_content.strip():
                doc.add_paragraph(page_text_content)
            else:
                doc.add_paragraph("(PaddleOCR 未能识别此页内容或此页无文本)")

        # Step 4: 保存Word文档
        doc.save(word_path)
        print(f"PaddleOCR 转换完成，文档已保存至: {word_path}")
        return True

    except Exception as e:
        print(f"PaddleOCR 转换过程中出错: {e}")
        import traceback
        traceback.print_exc()  # 打印详细错误堆栈
        return False


# --- 使用 PaddleOCR 工具类 ---
if __name__ == "__main__":
    # 确保 Poppler 的 bin 路径仍然正确
    POPPLER_BIN_PATH = r"D:\tools\poppler-23.07.0\Library\bin"  # 根据你的实际路径修改
    # 使用原始字符串避免转义警告
    input_scanned_pdf = r"D:\Google\Chrome\download\仪表设计信息模块优化需求.pdf"  # 根据你的实际路径修改

    # 调用新的函数
    ocr_pdf_to_word_paddle(input_scanned_pdf, poppler_path=POPPLER_BIN_PATH) 