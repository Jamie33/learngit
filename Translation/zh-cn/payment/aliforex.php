<?php

class aliforex
{
    /**
     * 生成支付代码
     * @param   array $order 订单信息
     * @param   array $payment 支付方式信息
     */
    public function get_code($order, $payment)
    {
        if (! defined('CHARSET')) {
            $charset = 'utf-8';
        } else {
            $charset = CHARSET;
        }
        
        $gateway = 'https://mapi.alipay.com/gateway.do?';
        $parameter = array(
            "service" => "create_forex_trade_wap",
            "partner" => $payment['alipay_partner'], // 合作者身份ID
            "return_url"	=> return_url(basename(__FILE__, '.php'), array('type'=>0)),
            "notify_url"	=> base_url().'/resources/notify/alipay.php',
            "subject"	=> $order['order_sn'],
            "body"	=> $order['order_sn'],
            "out_trade_no"	=> $order['order_sn'] . 'O' . $order['log_id'],
            "currency"	=> 'dollar',
            "total_fee"	=> $order['order_amount'],
            "_input_charset"	=> $charset
        );
        
        ksort($parameter);
        reset($parameter);
        $param = '';
        $sign = '';
        
        foreach ($parameter as $key => $val) {
            $param .= "$key=" . urlencode($val) . "&";
            $sign .= "$key=$val&";
        }
        
        $param = substr($param, 0, - 1);
        $sign = substr($sign, 0, - 1) . $payment['alipay_key'];

        // 请求授权接口
        $result = Http::doPost($gateway, $param . '&sign=' . md5($sign));
        $result = urldecode($result); // URL转码
        $result_array = explode('&', $result); // 根据 & 符号拆分

        // 重构数组
        $new_result_array = $temp_item = array();
        if (is_array($result_array)) {
            foreach ($result_array as $vo) {
                $temp_item = explode('=', $vo, 2); // 根据 & 符号拆分
                $new_result_array[$temp_item[0]] = $temp_item[1];
            }
        }
        $xml = simplexml_load_string($new_result_array['res_data']);
        $request_token = (array) $xml->request_token;

        // 请求交易接口
        $parameter = array(
            'service' => 'alipay.wap.auth.authAndExecute', // 接口名称
            'format' => 'xml', // 请求参数格式
            'v' => $new_result_array['v'], // 接口版本号
            'partner' => $new_result_array['partner'], // 合作者身份ID
            'sec_id' => $new_result_array['sec_id'],
            'req_data' => '<auth_and_execute_req><request_token>' . $request_token[0] . '</request_token></auth_and_execute_req>',
            'request_token' => $request_token[0],
            '_input_charset' => $charset
        );
        
        ksort($parameter);
        reset($parameter);
        $param = '';
        $sign = '';
        
        foreach ($parameter as $key => $val) {
            $param .= "$key=" . urlencode($val) . "&";
            $sign .= "$key=$val&";
        }

        $param = substr($param, 0, - 1);
        $sign = substr($sign, 0, - 1) . $payment['alipay_key'];
        
        /* 生成支付按钮 */
        $button = '<script type="text/javascript" src="'.base_url('public').'/js/ap.js"></script><div><button type="button" class="btn btn-default" onclick="javascript:_AP.pay(\'' . $gateway . $param . '&sign=' . md5($sign) . '\')"  >' . L('pay_button') . '</button></div>';
        return $button;
    }

    /**
     * 同步通知
     * @param $data
     * @return mixed
     */
    public function callback($data)
    {
        if (! empty($_GET)) {
            $out_trade_no = explode('O', $_GET['out_trade_no']);
            $log_id = $out_trade_no[1];
            $payment = get_payment($data['code']);

            /* 检查数字签名是否正确 */
            ksort($_GET);
            reset($_GET);
            
            $sign = '';
            foreach ($_GET as $key => $val) {
              if ($key != 'sign' && $key != 'sign_type' && $key != 'code') {
                $sign .= "$key=$val&";
              }
            }
            $sign = substr($sign, 0, - 1) . $payment['alipay_key'];
            if (md5($sign) != $_GET['sign']) {
              return false;
            }
            
            if ($_GET['result'] == 'success') {
              /* 改变订单状态 */
              order_paid($log_id, 2);
              return true;
            } else {
              return false;
            }
        }else{
            return false;
        }
    }

    /**
     * 异步通知
     * @param $data
     * @return mixed
     */
    public function notify($data)
    {
        if (! empty($_POST)) {
            $payment = get_payment($data['code']);
            // 支付宝系统通知待签名数据构造规则比较特殊，为固定顺序。
            $parameter['service'] = $_POST['service'];
            $parameter['v'] = $_POST['v'];
            $parameter['sec_id'] = $_POST['sec_id'];
            $parameter['notify_data'] = $_POST['notify_data'];
            // 生成签名字符串
            $sign = '';
            foreach ($parameter as $key => $val) {
                $sign .= "$key=$val&";
            }
            $sign = substr($sign, 0, - 1) . $payment['alipay_key'];
            // 验证签名
            if (md5($sign) != $_POST['sign']) {
                exit("fail");
            }
            // 解析notify_data
            $data = (array) simplexml_load_string($parameter['notify_data']);
            // 交易状态
            $trade_status = $data['trade_status'];
            // 获取支付订单号log_id
            $out_trade_no = explode('O', $data['out_trade_no']);
            $log_id = $out_trade_no[1]; // 订单号log_id
            if ($trade_status == 'TRADE_FINISHED' || $trade_status == 'TRADE_SUCCESS') {
                /* 改变订单状态 */
                order_paid($log_id, 2);
                if(method_exists('WechatController', 'do_oauth')){
                    /* 如果需要，微信通知 */
                    $order_id = model('Base')->model->table('order_info')->field('order_id')->where('order_sn = "'.$out_trade_no[0].'"')->getOne();
                    $order_url = __HOST__ . url('user/order_detail', array('order_id'=>$order_id));
                    $order_url = urlencode(base64_encode($order_url));
                    send_wechat_message('pay_remind', '', $out_trade_no[0].' 订单已支付', $order_url, $out_trade_no[0]);
                }
                exit("success");
            } else {
                exit("fail");
            }
        } else {
            exit("fail");
        }
    }

    /**
     * 订单查询
     * @return mixed
     */
    public function query($order, $payment)
    {

    }


}