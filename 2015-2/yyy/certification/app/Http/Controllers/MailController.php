<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Mail,QrCode,Crypt,Response, Log;
use Illuminate\Contracts\Encryption\DecryptException;
class MailController extends Controller
{
    public function send( )
    {
        $rand = uniqid(rand());
        $token = Crypt::encrypt($rand);
        QrCode::size(100);
        try {
            $decrypted = Crypt::decrypt($token);
        } catch (DecryptException $e) {
            //
        }
        $name = '嘤嘤嘤';
        $flag = Mail::send('email',['name'=>$name,'token'=>$token],function($message){
            $to = '545374042@qq.com';
            $message->to($to)->subject('ʅ（‾◡◝）ʃ哒铛～');
        });
        if($flag){
            echo '发送邮件成功，请查收！';
        }else{
            echo '发送邮件失败，请重试！';
        }
    }
}
