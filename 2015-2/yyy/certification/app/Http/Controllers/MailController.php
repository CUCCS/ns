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
        $token = uniqid(rand());
       /* $token = Crypt::encrypt($rand);
        try {
            $decrypted = Crypt::decrypt($token);
        } catch (DecryptException $e) {
            //
        }*/
        $flag = Mail::send('email',['token'=>$token],function($message){
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
