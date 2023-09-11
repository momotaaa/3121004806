import difflib
import argparse
from math import sqrt
import jieba
import os


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


def compute_similarity(file1, file2):
    # Read file content
    content1 = read_file(file1)
    content2 = read_file(file2)

    if content1 is None or content2 is None:
        return None

    # Tokenize file content using jieba
    words1 = list(jieba.cut(content1))
    words2 = list(jieba.cut(content2))

    # Create a SequenceMatcher instance for comparison
    similarity_ratio = difflib.SequenceMatcher(None, words1, words2).ratio()

    # Return similarity rounded to two decimal places
    return round(similarity_ratio, 2)


def similarity_with_2_sents(file1, file2):
    inner_product = 0
    square_length_vec1 = 0
    square_length_vec2 = 0

    content1 = read_file(file1)
    content2 = read_file(file2)
    if content1 is None or content2 is None:
        return None

    # Tokenize file content using jieba
    words1 = list(jieba.cut(content1))
    words2 = list(jieba.cut(content2))

    for tup1, tup2 in zip(words1, words2):
        inner_product += tup1[1]*tup2[1]
        square_length_vec1 += tup1[1]**2
        square_length_vec2 += tup2[1]**2

    return (inner_product/sqrt(square_length_vec1*square_length_vec2))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Compute similarity between two files.')
    parser.add_argument('file1', default='orig.txt', help='path to the original file')
    parser.add_argument('file2', default='modify_orig.txt', help='path to the modified file', )
    parser.add_argument('output_file', default='res.txt', help='path to the output file', )
    args = parser.parse_args()
    print(args)

    file1 = args.file1
    file2 = args.file2
    output_file = args.output_file

    similarity = compute_similarity(file1, file2)
    print(similarity)

    if similarity is not None:
        write_to_file(output_file, str(similarity))