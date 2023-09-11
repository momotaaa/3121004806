# Detect_similarity_article

# Abstract:
This project is implemented in Python with the aim of detecting the similarity between various articles or research papers, providing precise floating-point results up to the hundredth percentile. The program effectively serves as a deterrent against unethical academic plagiarism, thus ensuring the preservation of the diligent efforts made by researchers day after day.

github链接 ：https://github.com/momotaaa/Detect_similarity_article

题目：论文查重

描述如下：

设计一个论文查重算法，给出一个原文文件和一个在这份原文上经过了增删改的抄袭版论文的文件，在答案文件中输出其重复率。

原文示例：今天是星期天，天气晴，今天晚上我要去看电影。
抄袭版示例：今天是周天，天气晴朗，我晚上要去看电影。
要求输入输出采用文件输入输出，规范如下：

从命令行参数给出：论文原文的文件的绝对路径。
从命令行参数给出：抄袭版论文的文件的绝对路径。
从命令行参数给出：输出的答案文件的绝对路径。
我们提供一份样例，课堂上下发，上传到班级群，使用方法是：orig.txt是原文，其他orig_add.txt等均为抄袭版论文。

注意：答案文件中输出的答案为浮点型，精确到小数点后两位
PSP表格记录
PSP	Personal Software Process Stages	预估耗时（分钟）	实际耗时（分钟）
Planning	计划	140	60
· Estimate	· 估计这个任务需要多少时间	120	120
Development	开发	240	300
· Analysis	· 需求分析 (包括学习新技术)	160	100
· Design Spec	· 生成设计文档	30	10
· Design Review	· 设计复审	15	10
· Coding Standard	· 代码规范 (为目前的开发制定合适的规范)	20	5
· Design	· 具体设计	10	5
· Coding	· 具体编码	180	140
· Code Review	· 代码复审	20	5
· Test	· 测试（自我测试，修改代码，提交修改）	30	20
Reporting	报告	30	20
· Test Repor	· 测试报告	40	10
· Size Measurement	· 计算工作量	5	5
· Postmortem & Process Improvement Plan	· 事后总结, 并提出过程改进计划	5	5
Total	总计	975	815
代码实现
jieba分词
　　通过jieba库来对文本进行分词

words1 = list(jieba.cut(content1))
words2 = list(jieba.cut(content2))
文件读取
def read_file(file_path):
    # Check file path
    if not os.path.exists(file_path):
        print("File path does not exist. Please check!")
        return None

    # Read file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def write_to_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)
difflib.SequenceMatcher计算相似度
similarity_ratio = difflib.SequenceMatcher(None, words1, words2).ratio()
余弦值计算相似度
for tup1, tup2 in zip(words1, words2):
    inner_product += tup1[1]*tup2[1]
    square_length_vec1 += tup1[1]**2
    square_length_vec2 += tup2[1]**2
return (inner_product/sqrt(square_length_vec1*square_length_vec2))
命令行参数
parser = argparse.ArgumentParser(description='Compute similarity between two files.')
parser.add_argument('file1', default='orig.txt', help='path to the original file')
parser.add_argument('file2', default='modify_orig.txt', help='path to the modified file', )
parser.add_argument('output_file', default='res.txt', help='path to the output file', )
args = parser.parse_args()
上述提供了两种方法计算文本相似度，一种是基于文本匹配，另外一种是通过计算余弦相似度

运行结果
在终端输入命令行参数

python .\main.py .\orig.txt .\modify_orig.txt .\res.txt
Namespace(file1='.\\orig.txt', file2='.\\modify_orig.txt', output_file='.\\res.txt')
Building prefix dict from the default dictionary ...                  
Loading model from cache C:\Users\26685\AppData\Local\Temp\jieba.cache
Loading model cost 0.418 seconds.
Prefix dict has been built successfully.
0.76
结果显示程序运行0.418秒，重复率为76%，性能比较优秀。

 分词部分结果：

['活着', '前言', '\n', '\n', ' ', ' ', ' ', ' ', '一位', '真正', '的', '作家', '永远', '只', '为', '内心', '写作', '，', '只有', '内心', '才', '会', '真实', '地', '告诉', '他', '，', '他', '的', '自私', '、', '他', '的', '高尚', '是', '多么', '突出', '。', '内心', '
让', '他', '真实', '地', '了解', '自己', '，', '一旦', '了解', '了', '自己', '也', '就', '了解', '了', '世界', '。', '很多年', '前', '我', '就', '明白', '了', '这个', '原则', '，', '可是', '要', '捍卫', '这个', '原则', '必须', '付出', '艰辛', '的', '劳动', '和', '长
', '时期', '的', '痛苦', '，', '因为', '内心', '并非', '时时刻刻', '都', '是', '敞开', '的', '，', '它', '更', '多', '的', '时候', '倒', '是', '封闭', '起来', '，', '于是', '只有', '写作', '，', '不停', '地', '写作', '才能', '使', '内心', '敞开', '，', '才能', '使',
 '自己', '置身于', '发现', '之中', '，', '就', '像', '日出', '的', '光芒', '照亮', '了', '黑暗', '，', '灵感', '这时候', '才', '会', '突然', '来到', '。', '\n', '\n', ' ', ' ', ' ', ' ', '长期以来', '，', '我', '的', '作品', '都', '是', '源', '出于', '和', '现实', '
的', '那', '一层', '紧张', '关系', '。', '我', '沉湎', '于', '想象', '之中', '，', '又', '被', '现实', '紧紧', '控制', '，', '我', '明确', '感受', '着', '自我', '的', '分裂', '，', '我', '无法', '使', '自己', '变得', '纯粹', '，', '我', '曾经', '希望', '自己', '成为
', '一位', '童话', '作家', '，', '要', '不', '就是', '一位', '实实在在', '作品', '的', '拥有者', '，', '如果', '我', '能够', '成为', '这', '两者', '中', '的', '任何', '一个', '，', '我', '想', '我', '内心', '的', '痛苦', '将会', '轻微', '得', '多', '，', '可是', '与
此同时', '我', '的', '力量', '也', '会', '削弱', '很多', '。', '\n', '\n', ' ', ' ', ' ', ' ', '事实上', '我', '只能', '成为', '现在', '这样', '的', '作家', '，', '我', '始终', '为', '内心', '的', '需要', '而', '写作', '，', '理智',
