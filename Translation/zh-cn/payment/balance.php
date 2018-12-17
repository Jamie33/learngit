<?php

/**
 * 余额支付插件类
 */
class balance implements PaymentInterface
{

    /**
     * 提交函数
     */
    function get_code()
    {
        return '';
    }

    /**
     * 处理函数
     */
    function response()
    {
        return;
    }
}

?>