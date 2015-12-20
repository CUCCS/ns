@extends('auth.auth')
@section('content')
    @if (count($errors) > 0)
        <div class="alert alert-danger">
            <strong>天啦噜！</strong> 出错了囧：<br><br>
            <ul>
                @foreach ($errors->all() as $error)
                    <li>{{ $error }}</li>
                @endforeach
            </ul>
        </div>
    @endif
    <body >
    <section id="content" class="m-t-lg wrapper-md animated fadeInDown">
        <div class="container aside-xl">
            <a class="navbar-brand block" href="index.html"><span class="h1 font-bold">Two-factor</span></a>
            <section class="m-b-lg">
                <header class="wrapper text-center">
                    <strong>注册</strong>
                </header>
                <form action="{{ url('auth/register') }}" method="post">
                    {!! csrf_field() !!}
                    <div class="form-group">
                        <input name="name" type="text" value="{{ old('name') }}" placeholder="用户名" class="form-control rounded input-lg text-center no-border">
                    </div>
                    <div class="form-group">
                        <input name="email" type="email" value="{{ old('email') }}" placeholder="邮箱"
                               class="form-control rounded input-lg text-center no-border">
                    </div>
                    <div class="form-group">
                        <input name="password" type="Password" placeholder="密码" class="form-control rounded input-lg text-center no-border">
                    </div>
                    <div class="form-group">
                        <input  name="password_confirmation" type="Password" placeholder="确认密码" class="form-control rounded input-lg text-center no-border">
                    </div>
                    <button type="submit" class="btn btn-lg btn-info btn-block btn-rounded">注册</button>

                    <div class="line line-dashed"></div>
                    <p class="text-muted text-center">
                        <small>已经有了账户？</small>
                    </p>
                    <a href="{{ url('auth/login') }}" class="btn btn-lg btn-info btn-block btn-rounded">登录</a>
                </form>
            </section>
        </div>
    </section>
    </body>

@endsection
