<header class="bg-black header header-md navbar navbar-fixed-top-xs">
    @if(Auth::check())
        <div class="navbar-right ">
            <ul class="nav navbar-nav m-n hidden-xs nav-user user">
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle bg clear" data-toggle="dropdown">
              <span class="thumb-sm avatar pull-right m-t-n-sm m-b-n-sm m-l-sm">
               <img src="images/m21.jpg" class="img-circle">
              </span>
                        张三 <b class="caret"></b>
                    </a>
                    <ul class="bg-black dropdown-menu animated fadeInRight">
                        <li>
                            <span class="arrow top"></span>
                            <span class="bg clear"><a href="{{ url('personal') }}" class="btn btn-s-md btn-black">个人主页</a></span>
                        </li>
                        <li class="divider"></li>
                        {{--   <li>
                               <span class="bg clear"><a href="{{ url('personal') }}" class="btn btn-s-md btn-black">我的账户</a></span>

                           </li>--}}
                        {{--     <li class="divider"></li>
                             <li>
                                 <span class="bg clear"><a href="#" class="btn btn-s-md btn-black">VIP</a></span>

                             </li>
                             <li class="divider"></li>
                             <li>
                                 <span class="bg clear"><a href="#" class="btn btn-s-md btn-black">设置</a></span>

                             </li>
                             <li class="divider"></li>--}}

                        <li>
                            <span class="bg clear"><a href="auth/logout" class="btn btn-s-md btn-black">退出登录</a></span>
                        </li>
                    </ul>
                </li>
            </ul>

        </div>
    @else
        <div class="navbar-right ">
            <ul class="nav navbar-nav m-n hidden-xs nav-user user">
                <div class="navbar-right ">
                    <ul class="nav navbar-nav m-n hidden-xs nav-user user">

                        <li class="dropdown">
                            <a href="{{ url('auth/register') }}">
              <span class="icon-pencil icon text-info-dker">

              </span>注册
                            </a>

                        </li>
                        <li class="dropdown">
                            <a href="{{ url('auth/login') }}">
              <span class="icon-bulb icon text-info-dker">

              </span>登录</a>

                        </li></ul>

                </div>

            </ul>
        </div>
    @endif
</header>