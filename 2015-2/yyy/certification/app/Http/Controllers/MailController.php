<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use Mail;
use Crypt;
use Illuminate\Contracts\Encryption\DecryptException;
class MailController extends Controller
{
    public function send( )
    {

        $rand = uniqid(rand());
        $token = Crypt::encrypt($rand);
        $size = 200;
        $text = $token;
        if(!$size || !$text) return '';
        $qrCode = new QrCode();
        $qrCode->setText($text);
        $qrCode->setSize($size);
        $qrCode->setPadding(10);
        $response = Response::make($qrCode->get(), 200);
        $response->header('content-type', 'image/png');
        return $response;
       /* echo $rand;
        echo '/';
        echo $token . '/';
        try {
            $decrypted = Crypt::decrypt($token);
        } catch (DecryptException $e) {
            //
        }
        echo $decrypted;*/

      /*  $flag = Mail::raw($token, function ($message) {
            $to = '545374042@qq.com';
            $message ->to($to)->subject('ʅ（‾◡◝）ʃ哒铛～');
        });
        if($flag){
            echo '发送邮件成功，请查收！';
        }else{
            echo '发送邮件失败，请重试！';
        }*/
    }
}
