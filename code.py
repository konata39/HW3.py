#encoding=utf-8
# 這邊宣告
import sys
import re
reload(sys)
sys.setdefaultencoding('utf8')

#這邊切command line字串
#先看是不是3個argv 不是就fail
if len(sys.argv) != 3:
    print "Invaild argument"
    sys.exit()

#把十個pair用逗號切出來
spilt_pair = sys.argv[1].split(",")

#印出來看有沒有錯
print "\n".join(spilt_pair)

#用#分隔馬英九#蔡因文
pair_1 = spilt_pair[1].split("#")

#讀黨
file = open(sys.argv[2], 'r')

#把內容拿出來
content = file.read()

#用換行字源切割
content_str = str(content).split("\n")

#檢查符不符合regular exprewwion
m = re.search(pair_1[0],content_str[417])
#m =  re_words.search(content_str,0)

#印出有馬英九跟蔡英文對的該筆資料
print content_str[417]

#看有沒有對到
print m

file.close()

