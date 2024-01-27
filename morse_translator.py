def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    # 将输入文本转换为小写
    text = text.upper()

    # 初始化一个空列表来存储翻译的莫尔斯电码
    translated_text = []

    # 遍历输入文本中的每个字符
    for char in text:
        # 检查字符是否为字母
        if char.isalpha():
            # 检查字母在字典中是否有对应的莫尔斯电码
            if char in morse_code_dict:
                # 将莫尔斯电码添加到翻译文本列表中
                translated_text.append(morse_code_dict[char])
        # 检查字符是否为空格或斜杠
        elif char in [' ', '/']:
            # 将字符添加到翻译文本列表中
            translated_text.append(char)

    # 将翻译文本列表中的元素连接成一个字符串，并用空格分隔字母，用斜杠分隔单词
    translated_text = ' '.join(translated_text)

    return translated_text





print(morse_translator("NISHIBUSHIDABENDAN?"))