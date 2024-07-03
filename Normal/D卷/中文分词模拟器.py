import re


def get_result(sentences, words):
    # word_map 记录词库词汇
    word_map = {word: i for i, word in enumerate(words)}

    # ans 记录最终分词结果
    ans = []

    while sentences:
        sentence = sentences.pop(0)

        r = len(sentence)
        for r in range(len(sentence), 0, -1):
            # 截取句子 [0, r) 范围子串词汇，实现优先最长匹配
            fragment = sentence[:r]

            # 若词库中是否存在该子串词汇
            if fragment in word_map:
                # 则将对应子串词汇纳入结果
                ans.append(fragment)
                del word_map[fragment]  # 词库中每个词汇只能使用一次，因此移除

                # 若子串词汇只是句子部分，则句子剩余部分还要继续去词库中查找
                if r < len(sentence):
                    sentences.insert(0, sentence[r:])

                break

        # 没有在词库中找到对应子串词汇，则输出单个字母
        if r == 0:
            # 只放一个字母到结果中，句子剩余部分继续去词库中查找
            ans.append(sentence[0])

            if len(sentence) > 1:
                sentences.insert(0, sentence[1:])

    return ",".join(ans)


if __name__ == "__main__":
    sentences = re.split(r"[;,]", input().strip())
    words = re.split(r"[;,]", input().strip())

    result = get_result(sentences, words)
    print(result)
