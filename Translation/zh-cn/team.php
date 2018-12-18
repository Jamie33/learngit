<?php

/**
 * ECTouch Open Source Project
 * ============================================================================
 * Copyright (c) 2015-2016 http://ectouch.cn All rights reserved.
 * ----------------------------------------------------------------------------
 * 文件名称：team.php
 * ----------------------------------------------------------------------------
 * 功能描述：拼团语言
 * ----------------------------------------------------------------------------
 * Licensed ( http://www.ectouch.cn/docs/license.txt )
 * ----------------------------------------------------------------------------
 */

$_LANG['ranking_list'] = '排行';
$_LANG['team_user_list'] = '拼团成员';
$_LANG['waiting_team'] = '等待成团';
$_LANG['team_succes'] = '拼团成功';
$_LANG['team_failure'] = '拼团失败';
$_LANG['team_goods_info'] = '商品详情';
$_LANG['team_goods_comment'] = '商品评论';
$_LANG['my_team_order'] = '拼团订单';
$_LANG['team_keywords_result'] = '搜索结果';
$_LANG['invalid_number'] = '对不起，您输入非法商品数值';

/* 订单状态 */
$_LANG['os'][OS_UNCONFIRMED] = '未确认';
$_LANG['os'][OS_UNCONFIRMED] = 'UNCONFIRMED';
$_LANG['os'][OS_CONFIRMED] = '已确认';
$_LANG['os'][OS_CONFIRMED] = 'CONFIRMED';
$_LANG['os'][OS_SPLITED] = '已确认';
$_LANG['os'][OS_SPLITED] = 'SPLITED';
$_LANG['os'][OS_SPLITING_PART] = '已确认';
$_LANG['os'][OS_SPLITING_PART] = 'SPLITING_PART';
$_LANG['os'][OS_CANCELED] = '已取消';
$_LANG['os'][OS_CANCELED] = 'CANCELED';
$_LANG['os'][OS_INVALID] = '无效';
$_LANG['os'][OS_INVALID] = 'INVALID';
$_LANG['os'][OS_RETURNED] = '退货';
$_LANG['os'][OS_RETURNED] = 'RETURNED';

$_LANG['ss'][SS_UNSHIPPED] = '未发货';
$_LANG['ss'][SS_UNSHIPPED] = 'UNSHIPPED';
$_LANG['ss'][SS_PREPARING] = '配货中';
$_LANG['ss'][SS_PREPARING] = 'PREPARING';
$_LANG['ss'][SS_SHIPPED] = '已发货';
$_LANG['ss'][SS_SHIPPED] = 'SHIPPED';
$_LANG['ss'][SS_RECEIVED] = '收货确认';
$_LANG['ss'][SS_RECEIVED] = 'RECEIVED';
$_LANG['ss'][SS_SHIPPED_PART] = '已发货(部分商品)';
$_LANG['ss'][SS_SHIPPED_PART] = 'SHIPPED_PART';
$_LANG['ss'][SS_SHIPPED_ING] = '配货中'; // 已分单
$_LANG['ss'][SS_SHIPPED_ING] = 'SHIPPED_ING'; // 已分单

$_LANG['ps'][PS_UNPAYED] = '未付款';
$_LANG['ps'][PS_UNPAYED] = 'COD';   //货到付款
$_LANG['ps'][PS_PAYING] = '付款中';
$_LANG['ps'][PS_PAYING] = 'PAYING';
$_LANG['ps'][PS_PAYED] = '已付款';
$_LANG['ps'][PS_PAYED] = 'PAYED';
$_LANG['ps'][PS_PAYED_PART] = '部分付款(定金)';
$_LANG['ps'][PS_PAYED_PART] = 'PAYED_PART';

return $_LANG;