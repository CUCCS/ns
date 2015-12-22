<!doctype html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
</head>
<body>
请扫码获取二维码哟嚯嚯嚯
<br>
<img src="{!!$message->embedData(QrCode::format('png')->size(399)->generate($token), 'QrCode.png', 'image/png')!!}">
</body>
</html>