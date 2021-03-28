# genshin_piano_simulator

this simulator based on mido (https://github.com/mido/mido) to parse midi files and convert it to keymap.
so easyly play songs in game Genshin Impact if you can find .midi files 

usage : 
play canon
  install python and pip install packages from requirements.txt
  open Genshin(Windowed) and take of  your harp(not sure) ready to play 
  run main.py with administrator rights and keep your cursor focused on Genshin window.
  listen
  
other songs:
  because of the limit in Genshin , we may need to edit main.py to adjust the key of differernt midi files
  maybe you need to checkout DEFAULT_OFFSET and DEFAULT_TEMPO.
 
现在我奶奶都能在原神弹canon辣! 这是一个模拟按键实现.midi文件到原神乐谱按键映射的项目，可以支持音域在原神这个风琴
内的.midi文件，具体的操作大家看看代码吧，有疑问的地方也可以git提问(虽然我也是懵逼状态)
 
使用方法：
  安装python 再使用pip安装相关依赖
  窗口化原神，拿出活动送的琴，进入弹琴界面
  管理员直接运行main.py 鼠标光标扔在游戏窗口内 然后等加载完就会弹了.
  
要自定义其他midi 请在main.py里修改路径，然后因为原神只有3个key的24个白键 编辑一下DEFAULT_OFFSET的升降调以及DEFAULT_TEMPO节拍时值
