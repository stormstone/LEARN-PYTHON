# -*- coding: utf-8 -*- 
#lempel-ziv压缩与解压缩文件
#code:myhaspl@myhaspl.com
#4-2.py
import struct
import sys
txtfilename=sys.argv[1]
compressfn=sys.argv[2]
mystr=""
print "\n读取源文件".decode("utf8")
mytextfile= open(txtfilename,'r')
try:
     mystr=mytextfile.read( )
finally:
     mytextfile.close()
my_str=mystr
#码表
codeword_dictionary={}
#待压缩文本长度
str_len=len(my_str)
#码字最大长度
dict_maxlen=1
#将解析文本段的位置（下一次解析文本的起点）
now_index=0
#码表的最大索引
max_index=0

#压缩后数据
print "\n生成压缩数据中".decode("utf8") 
compresseddata=[]
while (now_index<str_len):    
    #向后移动步长
    mystep=0
    #当前匹配长度
    now_len=dict_maxlen
    if now_len>str_len-now_index:
        now_len=str_len-now_index
    #查找到的码表索引，0表示没有找到
    cw_addr=0   
    while (now_len>0):
        cw_index=codeword_dictionary.get(my_str[now_index:now_index+now_len])
        if cw_index!=None:
    		#找到码字
            cw_addr=cw_index
            mystep=now_len  
            break
        now_len-=1    
    if cw_addr==0:
        #没有找到码字,增加新的码字
        max_index+=1
        mystep=1
        codeword_dictionary[my_str[now_index:now_index+mystep]]=max_index
        print "don't find the Code word,add Code word:%s index:%d"%(my_str[now_index:now_index+mystep],max_index)
    else:
        #找到码字,增加新的码字
        if now_index+mystep+1<str_len:
            #如果文件尾部正好是字典中的码字，后面再无内容时，这部分将不会执行
            max_index+=1    
            codeword_dictionary[my_str[now_index:now_index+mystep+1]]=max_index
            if mystep+1>dict_maxlen:
                dict_maxlen=mystep+1      
            print "find the Code word:%s  add Code word:%s index:%d"%(my_str[now_index:now_index+now_len],my_str[now_index:now_index+mystep+1],max_index)  
    #压缩后结果
    cwdindex=cw_addr
    if cwdindex==0:
        cwlater=my_str[now_index:now_index+1] 
        now_index+=1
    else:
        now_index+=mystep     
        if now_index>=str_len:
        #文件已经读取完毕，后面无内容
           cwlater=""          
        else:
           cwlater=my_str[now_index:now_index+1] 
        now_index+=1        
    cw=(cwdindex,cwlater)
    compresseddata.append(cw)
print "\n生成压缩数据头部".decode("utf8")  
#生成数据压缩大小格式,65535为H能容纳的最大数据
if len(codeword_dictionary)<=65535:
    FLAG_FMT='H'
    FLAG_LEN='2'
else:
    FLAG_FMT='I'
    FLAG_LEN='4'    
 
  
#压缩数据写入文件
print "\n将压缩数据写入压缩文件中".decode("utf8"),   
lzv_file = open(compressfn,'wb')
try:
    #写入压缩数据头部信息
    #压缩数据长度
    lzv_len=len(compresseddata)
    lzv_file.write(struct.pack('I',lzv_len))
    #数据解码大小格式：
    lzv_file.write(struct.pack('1s1s',FLAG_FMT,FLAG_LEN))
    #写入压缩数据
    for temp_data in compresseddata:
        temp_key,temp_later=temp_data
        temp_wdata=struct.pack(FLAG_FMT+'1s',temp_key,temp_later)
        lzv_file.write(temp_wdata) 
        print ".",        
finally:
    lzv_file.close()

#解压缩数据
print "\n读入压缩数据中".decode("utf8"),
my_compresseddata=[]
my_codeword_dictionary={}
lzv_file = open(compressfn,'rb')
try:
    #读入压缩数据的长度
    lzv_len,=struct.unpack("I",lzv_file.read(4))
    #读入数据解码大小格式
    MY_FLAG_FMT,MY_FLAG_LEN=struct.unpack('1s1s',lzv_file.read(2))
    #读入压缩数据
    tmp_count=1
    while tmp_count<=lzv_len:
        #读入压缩数据
        temp_data =lzv_file.read(int(MY_FLAG_LEN)+1)
        temp_key,temp_later=struct.unpack(MY_FLAG_FMT+'1s',temp_data)
        my_compresseddata.append((temp_key,temp_later))        
        tmp_count+=1
        print ".",
    print "\n读入压缩数据成功".decode("utf8")
finally:
     lzv_file.close( )
print "\n解压中".decode("utf8"),
#解压缩
uncompress_str=''
#解码后数据
uncompressdata=[]
my_maxindex=0
#解码，同时重构码表
for (cwkey,cwlaster) in my_compresseddata:    
    if cwkey==0:
        my_maxindex+=1
        my_codeword_dictionary[my_maxindex]=cwlaster        
        uncompressdata.append(cwlaster)
    else:
        my_maxindex+=1
        my_codeword_dictionary[my_maxindex]=my_codeword_dictionary[cwkey]+cwlaster
        uncompressdata.append(my_codeword_dictionary[cwkey])
	if cwlaster!='\0':
           uncompressdata.append(cwlaster)     
    print ".",
uncompress_str=uncompress_str.join(uncompressdata)
uncompressstr=uncompress_str
print "\n将解压结果写入文件中..\n".decode("utf8")
uncompress_file= open('uncompress.txt','w')
try:
    uncompress_file.write(uncompressstr)
    print "\n解压成功，已解压到uncompress.txt！\n".decode("utf8")
finally:
    uncompress_file.close()




    
    




	


