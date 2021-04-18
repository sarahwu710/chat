def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    sarah_word_count = 0
    sarah_sticker_count = 0
    sarah_image_count = 0
    yellow_word_count = 0
    yellow_sticker_count = 0
    yellow_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == '莎拉':
            if s[2] == '貼圖':
                sarah_sticker_count += 1
            elif s[2] == '圖片':
                sarah_image_count += 1
            else:
                for msg in s[2:]:
                    sarah_word_count += len(msg)
        elif name == 'Yellow游妍柔Cassandra專案':
            if s[2] == '貼圖':
                yellow_sticker_count += 1
            elif s[2] == '圖片':
                yellow_image_count += 1
            else:
                for msg in s[2:]:
                    yellow_word_count += len(msg)
    print('Sarah說了', sarah_word_count, '個字')
    print('Sarah傳了', sarah_sticker_count, '個貼圖')
    print('Sarah傳了', sarah_image_count, '張圖片')
    print('Yellow說了', yellow_word_count, '個字')
    print('Yellow傳了', yellow_sticker_count, '個貼圖')
    print('Yellow傳了', yellow_image_count, '張圖片')
    
    
  
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('[LINE]Yellow.txt')
    lines = convert(lines)
    #write_file('output_line_chat.txt', lines)


main()

