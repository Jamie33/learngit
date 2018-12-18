<?php

$_LANG['flow_salve_error'] = "海量用户正在同一时刻下单，请返回重新下单";
$_LANG['back_cart'] = "返回购物车";

$_LANG['flow_login_register']['username_not_null'] = '请您输入用户名。';
$_LANG['flow_login_register']['username_invalid'] = '您输入了一个无效的用户名。';
$_LANG['flow_login_register']['password_not_null'] = '请您输入密码。';
$_LANG['flow_login_register']['email_not_null'] = '请您输入电子邮件。';
$_LANG['flow_login_register']['email_invalid'] = '您输入的电子邮件不正确。';
$_LANG['flow_login_register']['password_not_same'] = '您输入的密码和确认密码不一致。';
$_LANG['flow_login_register']['password_lt_six'] = '密码不能小于6个字符。';

$_LANG['regist_success'] = "恭喜您，%s 账号注册成功!";
$_LANG['login_success'] = '恭喜！您已经成功登录本站！';

/* 购物车 */
$_LANG['update_cart'] = '更新购物车';
$_LANG['back_to_cart'] = '返回购物车';
$_LANG['update_cart_notice'] = '购物车更新成功，请您重新选择您需要的赠品。';
$_LANG['direct_shopping'] = '不打算登录，直接购买';
$_LANG['goods_not_exists'] = '对不起，指定的商品不存在';
$_LANG['drop_goods_confirm'] = '您确实要把该商品移出购物车吗？';
$_LANG['goods_number_not_int'] = '请您输入正确的商品数量。';
$_LANG['stock_insufficiency'] = '非常抱歉，您选择的商品 %s 的库存数量只有 %d，您最多只能购买 %d 件。';
$_LANG['package_stock_insufficiency'] = '非常抱歉，您选择的超值礼包数量已经超出库存。请您减少购买量或联系商家。';
$_LANG['group_stock_insufficiency'] = "非常抱歉，您选择的商品 %s 的套餐数量只有 %d 件，您最多只能购买 %d 件。";
$_LANG['shopping_flow'] = '购物流程';
$_LANG['username_exists'] = '您输入的用户名已存在，请换一个试试。';
$_LANG['email_exists'] = '您输入的电子邮件已存在，请换一个试试。';
$_LANG['surplus_not_enough'] = '您使用的余额不能超过您现有的余额。';
$_LANG['integral_not_enough'] = '您使用的积分不能超过您现有的积分。';
$_LANG['integral_too_much'] = "您使用的积分不能超过%d";
$_LANG['invalid_bonus'] = "您选择的红包并不存在。";
$_LANG['no_goods_in_cart'] = '您的购物车中没有商品！';
$_LANG['not_submit_order'] = '您参与本次团购商品的订单已提交，请勿重复操作！';
$_LANG['pay_success'] = '本次支付已经成功，我们将尽快为您发货。';
$_LANG['pay_fail'] = '本次支付失败，请及时和我们取得联系。';
$_LANG['pay_disabled'] = '您选用的支付方式已经被停用。';
$_LANG['pay_invalid'] = '您选用了一个无效的支付方式。该支付方式不存在或者已经被停用。请您立即和我们取得联系。';
$_LANG['flow_no_shipping'] = '您必须选定一个配送方式。';
$_LANG['flow_no_payment'] = '您必须选定一个支付方式。';
$_LANG['pay_not_exist'] = '选用的支付方式不存在。';
$_LANG['storage_short'] = '库存不足';
$_LANG['subtotal'] = '小计';
$_LANG['accessories'] = '配件';
$_LANG['no_accessories'] = '没有相关配件';
$_LANG['largess'] = '赠品';
$_LANG['shopping_money'] = '购物金额小计 %s';
$_LANG['than_market_price'] = '比市场价 %s 节省了 %s (%s)';
$_LANG['your_discount'] = '根据优惠活动<a href="activity.php"><font color=red>%s</font></a>，您可以享受折扣 %s';
$_LANG['no'] = '无';
$_LANG['not_support_virtual_goods'] = '购物车中存在非实体商品,不支持匿名购买,请登录后在购买';
$_LANG['not_support_insure'] = '不支持保价';
$_LANG['clear_cart'] = '清空购物车';
$_LANG['drop_to_collect'] = '放入收藏夹';
$_LANG['password_js']['show_div_text'] = '请点击更新购物车按钮';
$_LANG['password_js']['show_div_exit'] = '关闭';
$_LANG['goods_fittings'] = '商品相关配件';
$_LANG['parent_name'] = '相关商品：';
$_LANG['remark_package'] = '礼包';
$_LANG['flow_no_shipping_prompt'] = '对不起，以下商品暂时无法进行配送';

/* 优惠活动 */
$_LANG['favourable_name'] = '活动名称：';
$_LANG['favourable_period'] = '优惠期限：';
$_LANG['favourable_range'] = '优惠范围：';
$_LANG['far_ext'][FAR_ALL] = '全部商品';
$_LANG['far_ext'][FAR_BRAND] = '以下品牌';
$_LANG['far_ext'][FAR_CATEGORY] = '以下分类';
$_LANG['far_ext'][FAR_GOODS] = '以下商品';
$_LANG['favourable_amount'] = '金额区间：';
$_LANG['favourable_type'] = '优惠方式：';
$_LANG['fat_ext'][FAT_DISCOUNT] = '享受 %d%% 的折扣';
$_LANG['fat_ext'][FAT_GOODS] = '从下面的赠品（特惠品）中选择 %d 个（0表示不限制数量）';
$_LANG['fat_ext'][FAT_PRICE] = '直接减少现金 %d';

$_LANG['favourable_not_exist'] = '您要加入购物车的优惠活动不存在';
$_LANG['favourable_not_available'] = '您不能享受该优惠';
$_LANG['favourable_used'] = '该优惠活动已加入购物车了';
$_LANG['pls_select_gift'] = '请选择赠品（特惠品）';
$_LANG['gift_count_exceed'] = '您选择的赠品（特惠品）数量超过上限了';
$_LANG['gift_in_cart'] = '您选择的赠品（特惠品）已经在购物车中了：%s';
$_LANG['label_favourable'] = '优惠活动';
$_LANG['label_collection'] = '我的收藏';
$_LANG['collect_to_flow'] = '立即购买';

/* 登录注册 */
$_LANG['forthwith_login'] = '登录';
$_LANG['forthwith_register'] = '注册新用户';
$_LANG['signin_failed'] = '对不起，登录失败，请检查您的用户名和密码是否正确';
$_LANG['gift_remainder'] = '说明：在您登录或注册后，请到购物车页面重新选择赠品。';

/* 收货人信息 */
$_LANG['flow_js']['consignee_not_null'] = '收货人姓名不能为空！';
$_LANG['flow_js']['country_not_null'] = '请您选择收货人所在国家！';
$_LANG['flow_js']['province_not_null'] = '请您选择收货人所在省份！';
$_LANG['flow_js']['city_not_null'] = '请您选择收货人所在城市！';
$_LANG['flow_js']['district_not_null'] = '请您选择收货人所在区域！';
$_LANG['flow_js']['invalid_email'] = '您输入的邮件地址不是一个合法的邮件地址。';
$_LANG['flow_js']['address_not_null'] = '收货人的详细地址不能为空！';
$_LANG['flow_js']['tele_not_null'] = '电话不能为空！';
$_LANG['flow_js']['shipping_not_null'] = '请您选择配送方式！';
$_LANG['flow_js']['payment_not_null'] = '请您选择支付方式！';
$_LANG['flow_js']['goodsattr_style'] = 1;
$_LANG['flow_js']['tele_invaild'] = '电话号码不有效的号码';
$_LANG['flow_js']['zip_not_num'] = '邮政编码只能填写数字';
$_LANG['flow_js']['mobile_invaild'] = '手机号码不是合法号码';

$_LANG['new_consignee_address'] = '新收货地址';
$_LANG['consignee_address'] = '收货地址';
$_LANG['consignee_name'] = '收货人姓名';
$_LANG['country_province'] = '配送区域';
$_LANG['please_select'] = '请选择';
$_LANG['city_district'] = '城市/地区';
$_LANG['email_address'] = '电子邮件地址';
$_LANG['detailed_address'] = '详细地址';
$_LANG['postalcode'] = '邮政编码';
$_LANG['phone'] = '电话';
$_LANG['mobile'] = '手机';
$_LANG['backup_phone'] = '手机';
$_LANG['sign_building'] = '标志建筑';
$_LANG['deliver_goods_time'] = '最佳送货时间';
$_LANG['default'] = '默认';
$_LANG['default_address'] = '默认地址';
$_LANG['confirm_submit'] = '确认提交';
$_LANG['confirm_edit'] = '确认修改';
$_LANG['country'] = '国家';
$_LANG['province'] = '省份';
$_LANG['city'] = '城市';
$_LANG['area'] = '所在区域';
$_LANG['consignee_add'] = '添加新收货地址';
$_LANG['shipping_address'] = '配送至这个地址';
$_LANG['address_amount'] = '您的收货地址最多只能是三个';
$_LANG['not_fount_consignee'] = '对不起，您选定的收货地址不存在。';

/*------------------------------------------------------ */
//-- 订单提交
/*------------------------------------------------------ */

$_LANG['goods_amount_not_enough'] = '您购买的商品没有达到本店的最低限购金额 %s ，不能提交订单。';
$_LANG['balance_not_enough'] = '您的余额不足以支付整个订单，请选择其他支付方式';
$_LANG['select_shipping'] = '您选定的配送方式为';
$_LANG['select_payment'] = '您选定的支付方式为';
$_LANG['order_amount'] = '您的应付款金额为';
$_LANG['remember_order_number'] = '感谢您在本店购物！您的订单已提交成功，请记住您的订单号';
$_LANG['back_home'] = '返回首页';
$_LANG['goto_user_center'] = '用户中心';
$_LANG['order_submit_back'] = '您可以 %s 或去 %s';

$_LANG['order_placed_sms'] = '您有新订单，收货人：%s 电话：%s'; //互亿短信
$_LANG['ali_order_placed_sms'] = '您有新订单，收货人：%s 收货地址：%s 电话：%s'; //阿里大鱼短信

$_LANG['sms_paid'] = '已付款';

$_LANG['notice_gb_order_amount'] = '（备注：团购如果有保证金，第一次只需支付保证金和相应的支付费用）';

$_LANG['pay_order'] = '支付订单 %s';
$_LANG['validate_bonus'] = '验证红包';
$_LANG['input_bonus_no'] = '或者输入红包序列号';
$_LANG['select_bonus'] = '选择已有红包';
$_LANG['bonus_sn_error'] = '该红包序列号不正确';
$_LANG['bonus_min_amount_error'] = '订单商品金额没有达到使用该红包的最低金额 %s';
$_LANG['bonus_is_ok'] = '该红包序列号可以使用，可以抵扣 %s';

$_LANG['msg_unfilled_or_receive'] = '还未发货或者已收货';

$_LANG['shopping_myship'] = '我的配送';
$_LANG['shopping_activity'] = '活动列表';
$_LANG['shopping_package'] = '超值礼包列表';

$_LANG['order_success'] = '下单成功';
$_LANG['receiving_address'] = '收货地址';
$_LANG['msg_receiving_notnull'] = '收货人不能为空';
$_LANG['msg_contact_way_notnull'] = '收货联系方式不能为空';
$_LANG['msg_mobile_format_error'] = '手机号码格式不正确';
$_LANG['msg_area_notnull'] = '所在地区不能为空';
$_LANG['msg_address_notnull'] = '详细地址不能为空';
$_LANG['msg_save_address'] = '最多只能保存 %s 个收货地址';
$_LANG['add_address'] = '新增收货地址';
$_LANG['not_exist_address'] = '您没有此收货地址';
$_LANG['edit_address'] = '修改收货地址';
$_LANG['success_address'] = '添加收货地址成功';
$_LANG['error_address'] = '添加收货地址失败';
$_LANG['no_address']= '没有此收货地址';
$_LANG['stock_store_shortage'] = "非常抱歉，您选择的商品 %s 的门店库存数量只有 %d，您最多只能购买 %d 件。";

// 购物车优惠活动显示
$_LANG['with_a_gift'] = "满赠";
$_LANG['full_reduction'] = "满减";
$_LANG['discount'] = "折扣";
$_LANG['activity_notes_one'] = "已购满";
$_LANG['activity_notes_three'] = "购满";
$_LANG['yuan'] = "元";
$_LANG['jian'] = "件";
$_LANG['already_receive'] = "已领取";
$_LANG['receive_gifts'] = "可领取赠品";
$_LANG['receive_gifts_again'] = "还可领取赠品";
$_LANG['receive_gift'] = "领取赠品";
$_LANG['see_gift'] = "查看赠品";
$_LANG['gather_together'] = "去凑单";
$_LANG['look_around'] = "再逛逛";
$_LANG['been_reduced'] = "已减";
$_LANG['activity_notes_two'] = "元， 即可享受满减";
$_LANG['reduce'] = "减";
$_LANG['already_enjoy'] = "已享受";
$_LANG['percent_off_discount'] = "折优惠";
$_LANG['percent_off'] = "折";
$_LANG['by_stages'] = "分期";
$_LANG['seller_store'] = "门店取货";
$_LANG['have_goods'] = "有货";
$_LANG['no_goods'] = "无货";
$_LANG['move_my_collection'] = "移到我的收藏";
$_LANG['remove_checked_goods'] = "删除选中的商品";
$_LANG['go_pay'] = "去结算";
$_LANG['title_count'] = '总价(不含运费)';
$_LANG['already_save'] = "已节省";
$_LANG['choose'] = "已选择";
$_LANG['cart_null_goods'] = "购物车内暂时没有商品，登录后将显示您之前加入的商品";
$_LANG['go_shoping'] = "去购物";
$_LANG['recommendation'] = "为你推荐";
$_LANG['history'] = "最近浏览";

$_LANG['can_receive_gifts'] = "元，即可领取赠品";
$_LANG['can_also_receive'] = "还可领取";
$_LANG['zhekouxianzhi'] = "元， 即可享受折扣";
$_LANG['can_receive_up_to'] = "可领取最多";
$_LANG['checked_in'] = "已选";


// 凑单语言包
$_LANG['coudan_title'] = "购物凑单";
$_LANG['activity_error'] = "优惠活动不存在";

// 余额支付备注
$_LANG['flow_surplus_pay'] = "使用余额支付订单";


return $_LANG;