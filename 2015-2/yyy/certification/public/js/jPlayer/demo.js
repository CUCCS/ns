var myPlaylist;
$(document).ready(function(){

  myPlaylist = new jPlayerPlaylist({
    jPlayer: "#jplayer_N",
    cssSelectorAncestor: "#jp_container_N"
  }, [
    {
      title:"如果没有你",
      artist:"莫文蔚",
      mp3:"testMusic/ruguomeiyouni.mp3",
      poster: "https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=3215547217,2712053834&fm=58"
    },
    {
      title:"说谎",
      artist:"林宥嘉",
      mp3:"testMusic/shuohuang.mp3",
      poster: "https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=2931206592,2565102266&fm=58"
    }
  ], {
    playlistOptions: {
      enableRemoveControls: true,
      autoPlay: false
    },
    swfPath: "js/jPlayer",
    supplied: "webmv, ogv, m4v, oga, mp3",
    smoothPlayBar: true,
    keyEnabled: true,
    audioFullScreen: false
  });
  
  $(document).on($.jPlayer.event.pause, myPlaylist.cssSelector.jPlayer,  function(){
    $('.musicbar').removeClass('animate');
    $('.jp-play-me').removeClass('active');
    $('.jp-play-me').parent('li').removeClass('active');
  });

  $(document).on($.jPlayer.event.play, myPlaylist.cssSelector.jPlayer,  function(){
    $('.musicbar').addClass('animate');
  });

  $(document).on('click', '.jp-play-me', function(e){
    e && e.preventDefault();
    var $this = $(e.target);
    if (!$this.is('a')) $this = $this.closest('a');

    $('.jp-play-me').not($this).removeClass('active');
    $('.jp-play-me').parent('li').not($this.parent('li')).removeClass('active');

    $this.toggleClass('active');
    $this.parent('li').toggleClass('active');
    if( !$this.hasClass('active') ){
      myPlaylist.pause();
    }else{
      var i = Math.floor(Math.random() * (1 + 7 - 1));
      myPlaylist.play(i);
    }
    
  });


  // video

  $("#jplayer_1").jPlayer({
    ready: function () {
      $(this).jPlayer("setMedia", {
        title: "Big Buck Bunny",
        m4v: "http://flatfull.com/themes/assets/video/big_buck_bunny_trailer.m4v",
        ogv: "http://flatfull.com/themes/assets/video/big_buck_bunny_trailer.ogv",
        webmv: "http://flatfull.com/themes/assets/video/big_buck_bunny_trailer.webm",
        poster: "images/m41.jpg"
      });
    },
    swfPath: "js",
    supplied: "webmv, ogv, m4v",
    size: {
      width: "100%",
      height: "auto",
      cssClass: "jp-video-360p"
    },
    globalVolume: true,
    smoothPlayBar: true,
    keyEnabled: true
  });

});


function add_to_list(obj, name,immediately_play)
{
    var p = obj.parentElement.parentElement.parentElement;

    p.className = "item-overlay opacity r r-2x bg-black active";

	var data = '{"libai":{"title":"李白","artist":"李荣浩","mp3":"testMusic/libai.mp3"},"banchengyansha":{"title":"半城烟沙","artist":"许嵩","mp3":"testMusic/banchengyansha.mp3"},"fangsheng":{"title":"放生","artist":"关心妍","mp3":"testMusic/fangsheng.mp3"},"naxienian":{"title":"那些年","artist":"胡夏","mp3":"testMusic/naxienian.mp3"},"xihuanni":{"title":"喜欢你","artist":"邓紫棋","mp3":"testMusic/xihuanni.mp3"},"bunengshuodemimi":{"title":"不能说的秘密","artist":"周杰伦","mp3":"testMusic/bunengshuodemimi.mp3"},"firework":{"title":"Firework","artist":"Katy Perry","mp3":"testMusic/FireWork.mp3"},"ybwm":{"title":"You Belong With Me","artist":"Taylor swift","mp3":"testMusic/You Belong With Me.mp3"},"ls":{"title":"Love Story","artist":"Taylor swift","mp3":"testMusic/Love Story.mp3"},"r":{"title":"red","artist":"Taylor swift","mp3":"testMusic/Red.mp3"},"f":{"title":"Fifteen","artist":"Taylor swift","mp3":"testMusic/Fifteen.mp3"},"tdomg":{"title":"Tear drops On My Guitar","artist":"Taylor swift","mp3":"testMusic/Tear drops On My Guitar.mp3"}}';
	var songs_json = jQuery.parseJSON(data);
  	myPlaylist.add({
		title:songs_json[name]["title"],
		artist:songs_json[name]["artist"],
		mp3:songs_json[name]["mp3"],
		poster: "http://www.jplayer.org/audio/poster/Miaow_640x360.png"
	});
	if(immediately_play){
		myPlaylist.play(-1); //播放播放列表的倒数第一首
	}

}
