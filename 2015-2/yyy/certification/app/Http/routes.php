<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the controller to call when that URI is requested.
|
*/

Route::get('/', function () {
    return view('welcome');
});
Route::get('home', "HomeController@index");

// 认证路由...
Route::get('auth/login', 'Auth\AuthController@getLogin');
Route::post('auth/login', 'Auth\AuthController@postLogin');
Route::get('auth/logout', 'Auth\AuthController@getLogout');
// 注册路由...
Route::get('auth/register', 'Auth\AuthController@getRegister');
Route::post('auth/register', 'Auth\AuthController@postRegister');
// 发送邮件
Route::get('mail/send','MailController@send');



Route::get('qrcode', function(){
    $size = 200;
    $text = 'ʅ（‾◡◝）ʃ';
    if(!$size || !$text) return '';
    $qrCode = new QrCode();
    $qrCode->setText($text);
    $qrCode->setSize($size);
    $qrCode->setPadding(10);
    $response = Response::make($qrCode->get(), 200);
    $response->header('content-type', 'image/png');
    return $response;
});




