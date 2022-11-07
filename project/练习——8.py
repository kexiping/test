'''
阿里巴巴商家节，用户名消费总金额 账户金额 优惠券
输入购买总购买金额
如果金额0-500则是LV1级别
如果500-2000元则是LV2，2000以上则是LV3
Lv1：随机赠送3张1-10元的优惠券
LV2：赠送2张50元的优惠券，如果充值则送充值金额的10%
LV3：赠送2张100优惠券，如果充值则赠送15%的金额

'''
import random
username = '石龙'
total = '1500'#消费总金额
money = 0 #账户金额
coupon = 0 #优惠券 总金额

#根据总金额判断级别
if 0 < total < 500: # LV1
    #随机赠送3张1-10元的优惠券
    quan1 = random.randint(1, 10)
    quan2 = random.randint(1, 10)
    quan3 = random.randint(1, 10)
    #将金额数加到coupon
    coupon = quan1 + quan1 + quan3
elif 500<=total<2000:
    #赠送2张50元的优惠券，如果充值则送充值金额的10%
    coupon += 2*50
    #嵌套if
    recharge = input('%s，是否要充值(送充值金额的10%)？（y/n）')
    if recharge == 'y':
        money += 1.1*int(input('输入充值金额：'))

elif total >=2000:
    #赠送2张100优惠券，如果充值则赠送15%的金额
    pass


