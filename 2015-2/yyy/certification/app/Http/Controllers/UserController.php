<?php
namespace App\Http\Controllers;
header("Access-Control-Allow-Origin: *");
use Illuminate\Http\Request;
use Mail,QrCode,Crypt,Response, Log,Redirect, Input, Config, Hash, Validator, Redis,Session;
use App\Http\Requests;
use App\Http\Controllers\Controller;
use Illuminate\Foundation\Auth\ThrottlesLogins;
use Illuminate\Foundation\Auth\AuthenticatesAndRegistersUsers;
use Auth;
use Lang;
use App\User;
class UserController extends Controller
{




    /*
    |--------------------------------------------------------------------------
    | Registration & Login Controller
    |--------------------------------------------------------------------------
    |
    | This controller handles the registration of new users, as well as the
    | authentication of existing users. By default, this controller uses
    | a simple trait to add these behaviors. Why don't you explore it?
    |
    */

    use AuthenticatesAndRegistersUsers, ThrottlesLogins;

    /**
     * Create a new authentication controller instance.
     *
     * @return void
     */

    public function __construct( )
    {
        $this->middleware('guest', ['except' => 'getLogout']);

    }

    public function getLogout()
    {
        if(Auth::guest()) {
            return redirect("/");
        }

        Auth::logout();
        return redirect(property_exists($this, 'redirectAfterLogout') ? $this->redirectAfterLogout : '/auth/login');

    }

    /**
     * Get a validator for an incoming registration request.
     *
     * @param  array  $data
     * @return \Illuminate\Contracts\Validation\Validator
     */
    protected function validator(array $data)
    {
        return Validator::make($data, [
            'email' => 'required|email|max:255',
            'password' => 'required|min:6',
            'key' => 'required'
        ]);
    }

    /**
     * Create a new user instance after a valid registration.
     *
     * @param  array  $data
     * @return User
     */
    protected function create(array $data)
    {
        return User::create([
            'nick_name' => $data['name'],
            'email' => $data['email'],
            'pwd' => Hash::make($data['password']),
        ]);
    }

    public function authenticat(Request $request)
    {
        $redis = Redis::connection();
//        $token = Session::get('uid');
        $token = $redis->get('uid');
        Log::debug("trying to authenticate,token is:" . $token);
        $email = Input::get("email");
        $password = Input::get("password");
        $ukey = Input::get("key");
        $validator = $this->validator(Input::all());

        if($validator->fails()) {
            return Redirect::to('/auth/login')
                ->withErrors($validator) // send back all errors to the login form
                ->withInput(Input::except('password')); // send back the input (not the password) so that we can repopulate the form
        }


        if (Auth::attempt(['email' => $email, 'password' => $password], $request->has("remember"), true)) {
            // 进一步检查用户token是否正确
            Log::debug("login passed");
            $user = Auth::user();
            if($ukey != $token) {

                Auth::logout();
                return Redirect::to("/auth/login")
                    ->withInput(Input::except("password"))
                    ->withErrors(["login.failed" => Lang::has("auth.unauthorzied") ? Lang::get("auth.unauthorzied") : "验证码不正确"]);
            }

            // Authentication passed...
           return Redirect::to('/home');
        } else {
            Log::debug("login failed");

            return Redirect::to("/auth/login")
                ->withInput(Input::except("password"))
                ->withErrors(["login.failed" => Lang::has("auth.failed") ? Lang::get("auth.failed") : "用户名和密码不匹配，登录失败"]);
        }
    }


    public function getLogin( )
    {
        return view("auth.login");
    }

    public function postLogin(Request $request)
    {
        Log::debug("trying to postLogin");
        Log::debug(Input::all());
        return $this->authenticat($request);
    }



    public function send(Request $request)
    {
        $redis = Redis::connection();
        if(count(User::where('email', '=', $request->get('email')))){

            $user = User::where('email', '=', $request->get('email'))->get();
            Log::debug($user);
            $token = md5(microtime(true));
            Session::put('uid', $token);
            $redis->set('uid', $token);
            Log::debug('sending email.token is:' . $token);
            $flag = Mail::send('email',['token'=>$token],function($message) use ($user) {

                $message->to($user[0]->email)->subject('ʅ（‾◡◝）ʃ哒铛～');
            });

            if($flag){
                return "发送邮件成功，请查收！";
            }else{
                return "发送邮件失败，请重试！";
            }

        }else{
            return "ʅ（‾◡◝）ʃ你要不要先注册呀";
        }


    }


}
