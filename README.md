Ancient-Chinese-Pinyin-transform-Tool
=====================================

根据许占宇(@hynuza)提供的古代字音表，将现代文转换为古汉语拼音.

###match.py

####combine()函数
用于创建字音文件，文件内容格式为:  
例：爲為潙䧦鄬𩻟\*ye  (目标汉字与拼音用*相隔 )  
保存目标文件为dicFile  


####match()函数
传入三个参数， dicFile, sourceFile, saveFile  
dicFile为利用combine函数所生成的字典文件  
sourceFile内容为要转换为古汉语拼音的文字  
saveFile用于保存结果

###示例

例如：  

> 臣植言：臣聞士之生世，入則事父，出則事君。事父尚於榮親，事君貴於興國。故慈父不能愛無益之子，仁君不能畜無用之臣。夫論德而授官者，成功之君也；量能而受爵者，畢命之臣也。故君無虛授，臣無虛受；虛授謂之謬舉，虛受謂之尸祿。詩之素餐，所由作也。昔二虢不辭兩國之任，其德厚也；旦奭不讓燕魯之封，其功大也。

将被转换为： 

> zjin zjik ngian ：zjin myonh zrix cji srvngh sjed ，njip cok zrih byox ，chjyt cok zrih kyon 。zrih byox zjangh qo yeng chinh ，zrih kyon kyoih qo hingh kuok 。koh zi byox NULL naih qaih myo qjek cji cix ，njin kyon NULL naih thriuk myo jyungh cji zjin 。pyo luonh tok nji zjuh kuan cjax ，zjeng kung cji kyon jax ；liangh naih nji zjux ciak cjax ，pjit miengh cji zjin jax 。koh kyon myo hio zjuh ，zjin myo hio zjux ；hio zjuh yoih cji myh kiox ，hio zjux yoih cji sjii luk 。sji cji soh chan ，sriox ju cak jax 。siek njiih kruak NULL zsi liangh kuok cji njimh ，ki tok ghuh jax ；tanh sjek NULL njangh qenh lox cji pyungh ，ki kung dah jax 。