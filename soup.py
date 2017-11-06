#coding:utf-8

from var_dump import *
from bs4 import BeautifulSoup

html_doc = """

<!DOCTYPE html>
<html lang="zh-cmn-Hans" class="ua-windows ua-webkit book-new-nav">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>豆瓣图书 Top 250</title>
  
<script>!function(e){var o=function(o,n,t){var c,i,r=new Date;n=n||30,t=t||"/",r.setTime(r.getTime()+24*n*60*60*1e3),c="; expires="+r.toGMTString();for(i in o)e.cookie=i+"="+o[i]+c+"; path="+t},n=function(o){var n,t,c,i=o+"=",r=e.cookie.split(";");for(t=0,c=r.length;t<c;t++)if(n=r[t].replace(/^\s+|\s+$/g,""),0==n.indexOf(i))return n.substring(i.length,n.length).replace(/\"/g,"");return null},t=e.write,c={"douban.com":1,"douban.fm":1,"google.com":1,"google.cn":1,"googleapis.com":1,"gmaptiles.co.kr":1,"gstatic.com":1,"gstatic.cn":1,"google-analytics.com":1,"googleadservices.com":1},i=function(e,o){var n=new Image;n.onload=function(){},n.src="https://www.douban.com/j/except_report?kind=ra022&reason="+encodeURIComponent(e)+"&environment="+encodeURIComponent(o)},r=function(o){try{t.call(e,o)}catch(e){t(o)}},a=/<script.*?src\=["']?([^"'\s>]+)/gi,g=/http:\/\/(.+?)\.([^\/]+).+/i;e.writeln=e.write=function(e){var t,l=a.exec(e);return l&&(t=g.exec(l[1]))?c[t[2]]?void r(e):void("tqs"!==n("hj")&&(i(l[1],location.href),o({hj:"tqs"},1),setTimeout(function(){location.replace(location.href)},50))):void r(e)}}(document);
</script>

  
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
  
  <script>var _head_start = new Date();</script>
  
  <link href="https://img3.doubanio.com/f/book/508ab0203af261c837f3001238b66d1fc339c8f9/css/book/master.css" rel="stylesheet" type="text/css">

  <link href="https://img3.doubanio.com/f/book/8a9d097c416aabac4f7e45f5d2ce9c6834b3fc7a/css/book/base/init.css" rel="stylesheet">
  <style type="text/css"></style>
  <script src="https://img3.doubanio.com/f/book/0495cb173e298c28593766009c7b0a953246c5b5/js/book/lib/jquery/jquery.js"></script>
  <script src="https://img3.doubanio.com/f/book/0f1957d4c436280f238b0295e4d0ba6855510555/js/book/master.js"></script>
  

  
  <script>  </script>
  <!-- COLLECTED CSS -->

  <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
</head>
<body>
  
    <script>var _body_start = new Date();</script>
    
   
    <link href="//img3.doubanio.com/dae/accounts/resources/321e246/shire/bundle.css" rel="stylesheet" type="text/css"> 
<div id="db-global-nav" class="global-nav">
  <div class="bd">
    
<div class="top-nav-info">
  <a href="https://www.douban.com/accounts/login?source=book" class="nav-login" rel="nofollow">登录</a>
  <a href="https://www.douban.com/accounts/register?source=book" class="nav-register" rel="nofollow">注册</a>
</div>     
<div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="slogan">我们的精神角落</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
    <div id="doubanapp-tip">
      <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 5.0 全新发布</a>
      <a href="javascript: void 0;" class="tip-close">×</a>
    </div>
  </div>
</div>

     <div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
    </li>
    <li class="on">
      <a href="https://book.douban.com"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
    </li>
    <li class="">
      <a href="https://movie.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/time&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://dongxi.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-commodity&quot;,&quot;uid&quot;:&quot;0&quot;}">东西</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">市集</a>
    </li>
    <li>
      <a href="#more" class="bn-more"><span>更多</span></a>
      <div class="more-items">
        <table cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td>
                <a href="https://ypy.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-ypy&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣摄影</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script> 
    <script src="//img3.doubanio.com/dae/accounts/resources/321e246/shire/bundle.js" defer="defer"></script> 

   
    <link href="//img3.doubanio.com/dae/accounts/resources/321e246/book/bundle.css" rel="stylesheet" type="text/css"> 

<div id="db-nav-book" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https:&#47;&#47;book.douban.com">豆瓣读书</a>
    </div>
    <div class="nav-search">
      <form action="https:&#47;&#47;book.douban.com/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="书名、作者、ISBN" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1001" />
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">
    

<div class="nav-items">
  <ul>
    <li    ><a href="https://book.douban.com/cart/"
     >购书单</a>
    </li>
    <li    ><a href="https://read.douban.com/ebooks/?dcs=book-nav&dcm=douban"
            target="_blank"
     >电子图书</a>
    </li>
    <li    ><a href="https://market.douban.com/book?utm_campaign=book_nav_freyr&utm_source=douban&utm_medium=pc_web"
     >豆瓣书店</a>
    </li>
    <li    ><a href="https://book.douban.com/annual2016/?source=navigation"
            target="_blank"
     >2016年度榜单</a>
    </li>
    <li    ><a href="https://book.douban.com/standbyme/2016?source=navigation"
            target="_blank"
     >2016读书报告</a>
    </li>
    <li          class=" book-cart"
    ><a href="https://market.douban.com/cart/?utm_campaign=book_nav_cart&utm_source=douban&utm_medium=pc_web"
            target="_blank"
     >购物车</a>
    </li>
  </ul>
</div>

  </div>
</div>

<script id="suggResult" type="text/x-jquery-tmpl">
  <li data-link="{{= url}}">
            <a href="{{= url}}" onclick="moreurl(this, {from:'book_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
            <img src="{{= pic}}" width="40" />
            <div>
                <em>{{= title}}</em>
                {{if year}}
                    <span>{{= year}}</span>
                {{/if}}
                <p>
                {{if type == "b"}}
                    {{= author_name}}
                {{else type == "a" }}
                    {{if en_name}}
                        {{= en_name}}
                    {{/if}}
                {{/if}}
                 </p>
            </div>
        </a>
        </li>
  </script> 

    <script src="//img3.doubanio.com/dae/accounts/resources/321e246/book/bundle.js" defer="defer"></script>      <div id="wrapper">
        
        
  <div id="content">
    
    <h1>豆瓣图书 Top 250</h1>

    <div class="grid-16-8 clearfix">
      
      <div class="article">
  <div class="indent">
    
  

        <p class="ulfirst"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/1770782/"
              onclick="moreurl(this,{i:'0'})"

              >
              <img src="https://img3.doubanio.com/mpic/s1727290.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/1770782/" onclick=&#34;moreurl(this,{i:&#39;0&#39;})&#34; title="追风筝的人"
                
              >
                追风筝的人

                
              </a> 
                &nbsp; <img src="https://img3.doubanio.com/pics/read.gif" alt="可试读" title="可试读"/>

              
                <br/>
                <span style="font-size:12px;">The Kite Runner</span>
            </div>

              <p class="pl">[美] 卡勒德·胡赛尼 / 李继宏 / 上海人民出版社 / 2006-5 / 29.00元</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">8.9</span>

                <span class="pl">(
                    288937人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">为你，千千万万遍</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/1084336/"
              onclick="moreurl(this,{i:'1'})"

              >
              <img src="https://img1.doubanio.com/mpic/s1237549.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/1084336/" onclick=&#34;moreurl(this,{i:&#39;1&#39;})&#34; title="小王子"
                
              >
                小王子

                
              </a> 

              
                <br/>
                <span style="font-size:12px;">Le Petit Prince</span>
            </div>

              <p class="pl">[法] 圣埃克苏佩里 / 马振聘 / 人民文学出版社 / 2003-8 / 22.00元</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">9.0</span>

                <span class="pl">(
                    228220人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">献给长成了大人的孩子们</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/1008145/"
              onclick="moreurl(this,{i:'2'})"

              >
              <img src="https://img3.doubanio.com/mpic/s1070222.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/1008145/" onclick=&#34;moreurl(this,{i:&#39;2&#39;})&#34; title="围城"
                
              >
                围城

                
              </a> 

              
            </div>

              <p class="pl">钱锺书 / 人民文学出版社 / 1991-2 / 19.00</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">8.9</span>

                <span class="pl">(
                    190707人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">对于“人艰不拆”四个字最彻底的违抗</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/25862578/"
              onclick="moreurl(this,{i:'3'})"

              >
              <img src="https://img3.doubanio.com/mpic/s27264181.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/25862578/" onclick=&#34;moreurl(this,{i:&#39;3&#39;})&#34; title="解忧杂货店"
                
              >
                解忧杂货店

                
              </a> 

              
                <br/>
                <span style="font-size:12px;">ナミヤ雑貨店の奇蹟</span>
            </div>

              <p class="pl">[日] 东野圭吾 / 李盈春 / 南海出版公司 / 2014-5 / 39.50元</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">8.6</span>

                <span class="pl">(
                    242870人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">一碗精心熬制的东野牌鸡汤，拒绝很难</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/1082154/"
              onclick="moreurl(this,{i:'4'})"

              >
              <img src="https://img3.doubanio.com/mpic/s23836852.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/1082154/" onclick=&#34;moreurl(this,{i:&#39;4&#39;})&#34; title="活着"
                
              >
                活着

                
              </a> 

              
            </div>

              <p class="pl">余华 / 南海出版公司 / 1998-5 / 12.00元</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">9.1</span>

                <span class="pl">(
                    134775人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">活着本身就是人生最大的意义</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/3259440/"
              onclick="moreurl(this,{i:'5'})"

              >
              <img src="https://img3.doubanio.com/mpic/s4610502.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/3259440/" onclick=&#34;moreurl(this,{i:&#39;5&#39;})&#34; title="白夜行"
                
              >
                白夜行

                
              </a> 
                &nbsp; <img src="https://img3.doubanio.com/pics/read.gif" alt="可试读" title="可试读"/>

              
                <br/>
                <span style="font-size:12px;">白夜行</span>
            </div>

              <p class="pl">[日] 东野圭吾 / 刘姿君 / 南海出版公司 / 2008-9 / 29.80元</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">9.1</span>

                <span class="pl">(
                    195473人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">暗夜独行的残破灵魂，爱与恶本就难分难舍</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/1046265/"
              onclick="moreurl(this,{i:'6'})"

              >
              <img src="https://img3.doubanio.com/mpic/s1228930.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/1046265/" onclick=&#34;moreurl(this,{i:&#39;6&#39;})&#34; title="挪威的森林"
                
              >
                挪威的森林

                
              </a> 

              
                <br/>
                <span style="font-size:12px;">ノルウェイの森</span>
            </div>

              <p class="pl">[日] 村上春树 / 林少华 / 上海译文出版社 / 2001-2 / 18.80元</p>
               <div class="star clearfix">
                  <span class="allstar40"></span>
                  <span class="rating_nums">8.0</span>

                <span class="pl">(
                    187555人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">村上之发轫，多少人的青春启蒙</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/3211779/"
              onclick="moreurl(this,{i:'7'})"

              >
              <img src="https://img3.doubanio.com/mpic/s3254244.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/3211779/" onclick=&#34;moreurl(this,{i:&#39;7&#39;})&#34; title="嫌疑人X的献身"
                
              >
                嫌疑人X的献身

                
              </a> 

              
                <br/>
                <span style="font-size:12px;">容疑者Xの献身</span>
            </div>

              <p class="pl">[日] 东野圭吾 / 刘子倩 / 南海出版公司 / 2008-9 / 28.00</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">8.9</span>

                <span class="pl">(
                    148879人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">数学好是一种极致的浪漫</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/2567698/"
              onclick="moreurl(this,{i:'8'})"

              >
              <img src="https://img1.doubanio.com/mpic/s2768378.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/2567698/" onclick=&#34;moreurl(this,{i:&#39;8&#39;})&#34; title="三体"
                
              >
                三体

                
                  <span style="font-size:12px;"> : “地球往事”三部曲之一 </span>
              </a> 

              
            </div>

              <p class="pl">刘慈欣 / 重庆出版社 / 2008-1 / 23.00</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">8.8</span>

                <span class="pl">(
                    148911人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">你我不过都是虫子</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/1017143/"
              onclick="moreurl(this,{i:'9'})"

              >
              <img src="https://img1.doubanio.com/mpic/s1091698.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/1017143/" onclick=&#34;moreurl(this,{i:&#39;9&#39;})&#34; title="不能承受的生命之轻"
                
              >
                不能承受的生命之轻

                
              </a> 
                &nbsp; <img src="https://img3.doubanio.com/pics/read.gif" alt="可试读" title="可试读"/>

              
                <br/>
                <span style="font-size:12px;">Nesnesitelná lehkost bytí</span>
            </div>

              <p class="pl">[捷克] 米兰·昆德拉 / 许钧 / 上海译文出版社 / 2003-7 / 23.00元</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">8.5</span>

                <span class="pl">(
                    135698人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">朝向媚俗的一次伟大的进军</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/1007305/"
              onclick="moreurl(this,{i:'10'})"

              >
              <img src="https://img1.doubanio.com/mpic/s1070959.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/1007305/" onclick=&#34;moreurl(this,{i:&#39;10&#39;})&#34; title="红楼梦"
                
              >
                红楼梦

                
              </a> 

              
            </div>

              <p class="pl">[清] 曹雪芹 著 / 人民文学出版社 / 1996-12 / 59.70元</p>
               <div class="star clearfix">
                  <span class="allstar50"></span>
                  <span class="rating_nums">9.6</span>

                <span class="pl">(
                    122986人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">谁解其中味？</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/1016300/"
              onclick="moreurl(this,{i:'11'})"

              >
              <img src="https://img1.doubanio.com/mpic/s1513378.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/1016300/" onclick=&#34;moreurl(this,{i:&#39;11&#39;})&#34; title="梦里花落知多少"
                
              >
                梦里花落知多少

                
              </a> 

              
            </div>

              <p class="pl">郭敬明 / 春风文艺出版社 / 2003-11 / 20.00元</p>
               <div class="star clearfix">
                  <span class="allstar35"></span>
                  <span class="rating_nums">7.1</span>

                <span class="pl">(
                    146834人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">只是青春留下的余烬</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/1040771/"
              onclick="moreurl(this,{i:'12'})"

              >
              <img src="https://img3.doubanio.com/mpic/s1513425.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/1040771/" onclick=&#34;moreurl(this,{i:&#39;12&#39;})&#34; title="达·芬奇密码"
                
              >
                达·芬奇密码

                
              </a> 

              
                <br/>
                <span style="font-size:12px;">The Da Vinci Code</span>
            </div>

              <p class="pl">[美] 丹·布朗 / 朱振武 / 上海人民出版社 / 2004-2 / 28.00元</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">8.2</span>

                <span class="pl">(
                    127993人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">一切畅销的因素都有了</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/20427187/"
              onclick="moreurl(this,{i:'13'})"

              >
              <img src="https://img3.doubanio.com/mpic/s24468373.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/20427187/" onclick=&#34;moreurl(this,{i:&#39;13&#39;})&#34; title="看见"
                
              >
                看见

                
              </a> 

              
            </div>

              <p class="pl">柴静 / 广西师范大学出版社 / 2013-1-1 / 39.80元</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">8.8</span>

                <span class="pl">(
                    121277人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">在这里看见中国</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/6082808/"
              onclick="moreurl(this,{i:'14'})"

              >
              <img src="https://img3.doubanio.com/mpic/s6384944.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/6082808/" onclick=&#34;moreurl(this,{i:&#39;14&#39;})&#34; title="百年孤独"
                
              >
                百年孤独

                
              </a> 

              
                <br/>
                <span style="font-size:12px;">Cien años de soledad</span>
            </div>

              <p class="pl">[哥伦比亚] 加西亚·马尔克斯 / 范晔 / 南海出版公司 / 2011-6 / 39.50元</p>
               <div class="star clearfix">
                  <span class="allstar50"></span>
                  <span class="rating_nums">9.2</span>

                <span class="pl">(
                    118145人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">尼采所谓的永劫复归，一场无始无终的梦魇</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/5275059/"
              onclick="moreurl(this,{i:'15'})"

              >
              <img src="https://img3.doubanio.com/mpic/s4477716.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/5275059/" onclick=&#34;moreurl(this,{i:&#39;15&#39;})&#34; title="1988：我想和这个世界谈谈"
                
              >
                1988：我想和这个世界谈谈

                
              </a> 

              
            </div>

              <p class="pl">韩寒 / 国际文化出版公司 / 2010-9 / 25.00元</p>
               <div class="star clearfix">
                  <span class="allstar40"></span>
                  <span class="rating_nums">7.9</span>

                <span class="pl">(
                    121052人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">车手韩寒的公路小说</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/1461903/"
              onclick="moreurl(this,{i:'16'})"

              >
              <img src="https://img3.doubanio.com/mpic/s2529195.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/1461903/" onclick=&#34;moreurl(this,{i:&#39;16&#39;})&#34; title="何以笙箫默"
                
              >
                何以笙箫默

                
              </a> 

              
            </div>

              <p class="pl">顾漫 / 朝华出版社 / 2007-4 / 15.00元</p>
               <div class="star clearfix">
                  <span class="allstar40"></span>
                  <span class="rating_nums">7.8</span>

                <span class="pl">(
                    118916人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">倒追有风险，入行需谨慎</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/1200840/"
              onclick="moreurl(this,{i:'17'})"

              >
              <img src="https://img3.doubanio.com/mpic/s2335693.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/1200840/" onclick=&#34;moreurl(this,{i:&#39;17&#39;})&#34; title="平凡的世界（全三部）"
                
              >
                平凡的世界（全三部）

                
              </a> 

              
            </div>

              <p class="pl">路遥 / 人民文学出版社 / 2005-1 / 64.00元</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">9.0</span>

                <span class="pl">(
                    101339人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">中国当代城乡生活全景</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/1141406/"
              onclick="moreurl(this,{i:'18'})"

              >
              <img src="https://img3.doubanio.com/mpic/s5924326.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/1141406/" onclick=&#34;moreurl(this,{i:&#39;18&#39;})&#34; title="简爱"
                
              >
                简爱

                
              </a> 

              
                <br/>
                <span style="font-size:12px;">Jane Eyre</span>
            </div>

              <p class="pl">[英] 夏洛蒂·勃朗特 / 世界图书出版公司 / 2003-11 / 18.00元</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">8.5</span>

                <span class="pl">(
                    107791人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">灰姑娘在十九世纪</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/1041007/"
              onclick="moreurl(this,{i:'19'})"

              >
              <img src="https://img3.doubanio.com/mpic/s1990480.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/1041007/" onclick=&#34;moreurl(this,{i:&#39;19&#39;})&#34; title="哈利·波特与魔法石"
                
              >
                哈利·波特与魔法石

                
              </a> 
                &nbsp; <img src="https://img3.doubanio.com/pics/read.gif" alt="可试读" title="可试读"/>

              
                <br/>
                <span style="font-size:12px;">Harry Potter and the Philosopher&#39;s Stone</span>
            </div>

              <p class="pl">[英] J. K. 罗琳 / 苏农 / 人民文学出版社 / 2000-9 / 19.50元</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">9.0</span>

                <span class="pl">(
                    87314人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">羽加迪姆勒维奥萨！</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/10554308/"
              onclick="moreurl(this,{i:'20'})"

              >
              <img src="https://img1.doubanio.com/mpic/s29384019.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/10554308/" onclick=&#34;moreurl(this,{i:&#39;20&#39;})&#34; title="白夜行"
                
              >
                白夜行

                
              </a>
              
            </div>

              <p class="pl">东野圭吾 / 刘姿君 / 南海出版公司 / 2013-1-1 / CNY 39.50</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">9.2</span>

                <span class="pl">(
                    99176人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">封面剧透</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/3066477/"
              onclick="moreurl(this,{i:'21'})"

              >
              <img src="https://img3.doubanio.com/mpic/s3078482.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/3066477/" onclick=&#34;moreurl(this,{i:&#39;21&#39;})&#34; title="三体Ⅱ"
                
              >
                三体Ⅱ

                
                  <span style="font-size:12px;"> : 黑暗森林 </span>
              </a>
            </div>

              <p class="pl">刘慈欣 / 重庆出版社 / 2008-5 / 32.00</p>
              <div class="star clearfix">
                  <span class="allstar50"></span>
                  <span class="rating_nums">9.3</span>

                <span class="pl">(
                    88192人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">无边的黑暗森林，比第一部更为恢弘壮丽</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/1068920/"
              onclick="moreurl(this,{i:'22'})"

              >
              <img src="https://img1.doubanio.com/mpic/s1078958.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/1068920/" onclick=&#34;moreurl(this,{i:&#39;22&#39;})&#34; title="飘">
                飘
              </a>

                <br/>
                <span style="font-size:12px;">Gone with the Wind</span>
            </div>

              <p class="pl">[美国] 玛格丽特·米切尔 / 李美华 / 译林出版社 / 2000-9 / 40.00元</p>
               <div class="star clearfix">
                  <span class="allstar50"></span>
                  <span class="rating_nums">9.3</span>

                <span class="pl">(
                    78652人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">革命时期的爱情，随风而逝</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>

      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/4238362/"
              onclick="moreurl(this,{i:'23'})"

              >
              <img src="https://img1.doubanio.com/mpic/s4243447.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/4238362/" onclick=&#34;moreurl(this,{i:&#39;23&#39;})&#34; title="送你一颗子弹"
                
              >
                送你一颗子弹
              </a>

            </div>

              <p class="pl">刘瑜 / 上海三联书店 / 2010-1 / 25.00元</p>
               <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">8.6</span>

                <span class="pl">(
                    88930人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">犀利又温柔，穿过胸口隐隐作痛</span>
              </p>           </td>
        </tr>
      </table>
        <p class="ul"></p>
 
      <table width="100%">
        <tr class="item">
          <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/5363767/"
              onclick="moreurl(this,{i:'24'})"

              >
              <img src="https://img3.doubanio.com/mpic/s26012674.jpg" width="90" />
            </a>
          </td>
          <td valign="top">
            
            <div class="pl2">               <a href="https://book.douban.com/subject/5363767/" onclick=&#34;moreurl(this,{i:&#39;24&#39;})&#34; title="三体Ⅲ">
                三体Ⅲ

                  <span style="font-size:12px;"> : 死神永生 </span>
              </a>

            </div>

              <p class="pl">刘慈欣 / 重庆出版社 / 2010-11 / 38.00元</p>

              <div class="star clearfix">
                  <span class="allstar50"></span>
                  <span class="rating_nums">9.2</span>

                <span class="pl">(
                    86668人评价
                )</span>
              </div>

            
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">终章，何去何从</span>
              </p>           </td>
        </tr>
      </table>
        <div class="paginator">
        <span class="prev">
            &lt;前页
        </span>
        
        

                <span class="thispage">1</span>
                
            <a href="https://book.douban.com/top250?start=25" >2</a>
        
                
            <a href="https://book.douban.com/top250?start=50" >3</a>
        
                
            <a href="https://book.douban.com/top250?start=75" >4</a>
        
                
            <a href="https://book.douban.com/top250?start=100" >5</a>
        
                
            <a href="https://book.douban.com/top250?start=125" >6</a>
        
                
            <a href="https://book.douban.com/top250?start=150" >7</a>
        
                
            <a href="https://book.douban.com/top250?start=175" >8</a>
        
                
            <a href="https://book.douban.com/top250?start=200" >9</a>
        
                
            <a href="https://book.douban.com/top250?start=225" >10</a>
        
        <span class="next">
            <link rel="next" href="https://book.douban.com/top250?start=25"/>
            <a href="https://book.douban.com/top250?start=25" >后页&gt;</a>
        </span>

        </div>   </div>
</div>
      <div class="aside">
        
  <span class="indent pl">
    豆瓣用户每天都在对“读过”的书进行“很差”到“力荐”的评价，豆瓣根据每本书读过的人数以及该书所得的评价等综合数据，通过算法分析产生了豆瓣图书 Top 250。
  </span>

      </div>
      <div class="extra">
        
      </div>
    </div>
  </div>

        
  <div id="footer">
    
<span id="icp" class="fleft gray-link">
    &copy; 2005－2017 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about?policy=disclaimer">免责声明</a>
    
    · <a href="https://help.douban.com/?app=book" target="_blank">帮助中心</a>
    · <a href="https://book.douban.com/library_invitation">图书馆合作</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

  </div>

    </div>
    <!-- COLLECTED JS -->
    <!-- mako -->
    
    
  

<script type="text/javascript">
  var _paq = _paq || [];
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0]; 
    g.type='text/javascript';
    g.defer=true; 
    g.async=true; 
    g.src=p+'://s.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
  })();
</script>

<script type="text/javascript">
var setMethodWithNs = function(namespace) {
  var ns = namespace ? namespace + '.' : ''
    , fn = function(string) {
        if(!ns) {return string}
        return ns + string
      }
  return fn
}

var gaWithNamespace = function(fn, namespace) {
  var method = setMethodWithNs(namespace)
  fn.call(this, method)
}

var _gaq = _gaq || []
  , accounts = [
      { id: 'UA-7019765-1', namespace: 'douban' }
    , { id: 'UA-7019765-16', namespace: '' }
    ]
  , gaInit = function(account) {
      gaWithNamespace(function(method) {
        gaInitFn.call(this, method, account)
      }, account.namespace)
    }
  , gaInitFn = function(method, account) {
      _gaq.push([method('_setAccount'), account.id])

      
  _gaq.push([method('_addOrganic'), 'google', 'q'])
  _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
  _gaq.push([method('_addOrganic'), 'soso', 'w'])
  _gaq.push([method('_addOrganic'), 'youdao', 'q'])
  _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
  _gaq.push([method('_addOrganic'), 'sogou', 'query'])
  if (account.namespace) {
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
    _gaq.push([method('_addIgnoredOrganic'), 'douban'])
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
    _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
  }

      if (account.namespace === 'douban') {
        _gaq.push([method('_setDomainName'), '.douban.com'])
      }

        _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])

        _gaq.push([method('_setCustomVar'), 2, 'login_status', '0', 2]);

      _gaq.push([method('_trackPageview')])
    }

for(var i = 0, l = accounts.length; i < l; i++) {
  var account = accounts[i]
  gaInit(account)
} ;(function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
})()
</script>

    <!-- sindar14d-docker-->

</body>
</html>

"""
soup = BeautifulSoup(html_doc, 'html.parser')

# print soup.prettify()

# print soup.title
# print soup.title.name
# print soup.title.string
# print soup.title.parent
# print soup.title.parent.name

print soup.a.get('href')
all_a = soup.find_all('a')
for a in all_a:
