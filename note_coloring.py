def ColorNote(path : str, tps : list, save_as : str):
    '''
    tps : 3 element tuple
    (x,y,color)
    '''
    content = ''
    with open(path,'rt',encoding='utf-8') as f:
        content = f.read()

    tps.sort(key = lambda tp : tp[0])
    now_line = -1
    now_line_position = 0

    for tp in tps:
        if tp[0] != now_line:
            now_line = tp[0]
            now_line_position = content.find("var notes{}".format(now_line))
            if now_line_position == -1:
                raise IndexError("Index {} out of range".format(now_line))
            now_line_position = content.find('];',now_line_position)
            now_line_position += 2
        if now_line < 0 :
            raise IndexError("Index less than zero")
        
        coloring = "\n notes{}[{}].setStyle({{ fillStyle: '{}', strokeStyle: '{}' }});".format(tp[0],tp[1],tp[2],tp[2])
        content = content[0:now_line_position] + coloring + content[now_line_position : ]
    
    with open(save_as,'wt',encoding='utf-8') as f:
        content = f.write(content)

if __name__ == '__main__':
    ColorNote('./data/trans_1.txt.html',[(0,0,'#66ccff'),(1,0,'#66ccff')],'./data/trans_1.txt_color.html')
        