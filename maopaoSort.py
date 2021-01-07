'''
冒泡排序
'''
# def bubbo_sort(arr):
#     length = len(arr)
#     for i in range(length):
#         for j in range(length-i-1):
#             if arr[j] > arr[j+1]:
#                 # tmp = arr[j]
#                 # arr[j]=arr[j+1]
#                 # arr[j+1]=tmp
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
# arr=[1,3,4,5,6,8,2,7]
# bubbo_sort(arr)
# print(arr)


'''
俩数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
'''

# arr=[1,3,6,15]
# target=9
# '''
# 一遍哈希表
# '''
# def two_sum_with_dict2(nums, target):
#     _dict = {}
#     for i, e in enumerate(nums):
#         if _dict.get(target - e) is not None:
#             return (_dict.get(target - e), i)
#         _dict[e] = i
#
# res=two_sum_with_dict2(arr,target)
# print(res)
'''
暴力循环
'''

# def twoSum(nums,target):
#     for i, m in enumerate(nums):
#         j=i+1
#         while j<len(nums):
#             if target == m+nums[j]:
#                 return [i,j]
#             else:
#                 j+=1
#
# res = twoSum(arr,target)
# print(res)


'''
反转字符串
'''
# eStr=["h","e","l","l","o"]
# outputStr=["o","l","l","e","h"]
#
# eStr.reverse()
#
# 双向指针
# i, j = 0, len(eStr)-1
# while i<j:
#     eStr[i], eStr[j]=eStr[j],eStr[i]
#     i+=1
#     j-=1

'''
反转字符串里的单词
'''
# rStr = "the sky is blue"
# 方法一
# newrStr = rStr.split()
# i, j = 0, len(newrStr)-1
# while i < j:
#     newrStr[i], newrStr[j] = newrStr[j], newrStr[i]
#     i+=1
#     j-=1
# print(' '.join(newrStr))
# # 方法二
# print(' '.join(rStr.split()[::-1]))
#

'''
回文数
'''

# def isPalindrome(x):
#     if x < 0:#当数字是负数的时候必然不是回文数
#         return False
#     result = 0
#     temp = x
#     while temp != 0:
#         result = result * 10 + temp % 10
#         temp = temp // 10
#         print(result, temp)
#     return x == result
#
# res = isPalindrome(121)
# print(res)

#
# 将字符串转化为数字,实现int()方法
s = '298476'
n = 298476
s = s[::-1]
number = 0
for i, e in enumerate(s):
    print(i, e)
    for j in range(0, 10):
        if e == str(j):
            number += j*(10**i)

print(number, type(number))

# for i, e in enumerate(s):
#     if e == s[i]:
#         num = num + int(e)*(10**i)
#
# num = 0
# for i, v in enumerate(s):
#     num += (ord(v)-ord('0'))*(10**i)
#
# print(num)



# import json
#
# dic = {'certType':'IC', 'city':'', 'bankName':'', 'orderAmount':'2000', 'province':'', 'bankNo':'123456', 'digest':'NKBWCFihpcBIffjYMq6vHS3cpDEkRifZ+0KshduC8kNGJYhpNJZprziJCSq05mP+mt0Gr2+xEXnSAZZodhSi2qKAnrG3B7qFP43od4FOlXA9DPClM78cTXjViVeXE1gGLzP4GBk0NCDaDkFIbg7/oYQU8CeVA/p/vdl7MImm963xYGOdeWg9zw3o3l/tG9GpU8zyYrMU+i7JUsqM1JCj8MP0pGz4QjkdcaqXwQnh/BaWBSAewGzlBwVwbuYHPkFsFWwi1JPYgCe6/Z8pyHU+WTK0GQ2STzVhPUpsIZjHzCRvfIrXkYOscgCsCfb7pSjULIjIS/35JAC3CwRuzGAFdw==', 'signType':'RSA2', 'expireDate':'', 'attr':'1', 'ext1':'自定义', 'cvv':'', 'orderNo':'201909251429223352', 'productId':'D01', 'accNo':'6217003320034459100', 'accName':'测试', 'cardType':'01', 'mobile':'13500000000', 'branchName':'', 'version':'V1.0', 'certNo':'320582198707061118', 'notifyUrl':'http://localhost:8080/notify', 'orderDate':'20190925', 'merchantNo':'666100000000888', 'branchNo':''}
# js = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ':'))
# print(js)

import time
from datetime import datetime

# print(time.ctime(),type(time.ctime()))
# print(time.gmtime(),type(time.gmtime()))
# print(datetime.datetime.now(),type(datetime.datetime.now()))
# print(datetime.datetime(2019,9,19)+datetime.timedelta(1))
# print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))
# print(time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime()))
# dt = datetime.timestamp(datetime.now())
# print(dt, type(dt))
# df = datetime.fromtimestamp(dt)
# print(df, type(df))

# print(datetime.weekday(datetime.today()))
# print(datetime.utcnow())
# ds = datetime.strptime('2019-09-26 18:17:36', '%Y-%m-%d %H:%M:%S')
# print(ds, type(ds))
# dtf=datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
# print(dtf,type(dtf))


def get_other_time(day,format='%Y%m%d%H%M%S'):
    #这个函数是用来获取N天前的时间，或者N天后的时间
    #day如果传入负数，那么就是几天前的。传入正数，就是几天后的
    import datetime
    res = datetime.datetime.now()+datetime.timedelta(day)#取几天后的
    res_time = res.strftime(format)#格式化时间
    return res_time


#1、写一个程序，输入qq群号码，把每个群成员的头像下载下来，保存到本地，图片名字取群昵称，如果没有群昵称，取qq名字


#2、登录接口 login
    #username password
    #登陆成功，产生 seesionid,  1102a245b59af9c783bb8c18948ef96d# username+当前时间戳+salt
    #seesionid 存到redis里面，user_seesions: {
#               1102a245b59af9c783bb8c18948ef96d:{"user_name":"wyj","userid":1}
#               1102a245b59af9c783bb8c18948ef16d:{"user_name":"wqz","userid":1}
#               }，key的失效时间



#2、支付接口，支付需要登录
    #post请求，参数：seesionId，money
    #表字段
    #user  id username password balance
    #1、session不正确，提示请登录
    #2、校验money的类型
    #3、balance必须大于等于money才可以支付


