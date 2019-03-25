<!doctype html>
{% load static %}
<html lang="zh-cn" class="no-js">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Unfolder用户DEMO</title>
<link href='https://fonts.useso.com/css?family=Open+Sans:400,700' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
<link rel="stylesheet" href="{% static 'css/reset.css' %}">
<link rel="stylesheet" href="{% static 'css/htmleaf-demo.css' %}">
<link rel="stylesheet" href="{% static 'css/swiper.min.css' %}">
<link rel="stylesheet" href="{% static 'css/style3.css' %}">
<link rel="stylesheet" href="{% static 'css/login3.css' %}">
<link rel="stylesheet" href="{% static 'css/chinaz.css' %}">
    <style>
            #panel {
        position: fixed;
        background-color: white;
        max-height: 90%;
        overflow-y: auto;
        top: 10px;
        right: 10px;
        width: 280px;
    }
    #panel .amap-lib-driving {
	    border-radius: 4px;
        overflow: hidden;
    }
    </style>

</head>
<body>
<div class="top-bar">
	<div class="container">
		<ul class="top-contacts">
			<li class="top-unhover"><p><span class="fa fa-phone-square" aria-hidden="true"></span> +1 515 151515</p>
			</li><li class="top-hover"><p><span class="fa fa-envelope" aria-hidden="true"></span> <a href="mailto:support@company.com">support@company.com</a></p>
		</li></ul>
		<ul class="top-links">
			<li><a href="#"><i class="fa fa-facebook"></i></a></li>
			<li><a href="#"><i class="fa fa-twitter"></i></a></li>
			<li><a href="#"><i class="fa fa-linkedin"></i></a></li>
			<li><a href="#"><i class="fa fa-google-plus"></i></a></li>
		</ul>
		<div class="clearfix"></div>
	</div>
</div>
<header class="cd-main-header animate-search">
	<div class="cd-logo"><a href="/service/"><img src="{% static 'img/logo.png' %}" alt="Logo"></a></div>

	<nav class="cd-main-nav-wrapper">
		<a href="#search" class="cd-search-trigger cd-text-replace">Search</a>
		<ul class="cd-main-nav navbar-left">
			<li class="dropdown" style="left: 150px">
				<a  href="/service/{{  request.session.city }}/" id="dropdownMenu1" data-toggle="dropdown">{{  request.session.city }}
					<span class="caret"></span>
				</a>
				<div  class="dropdown-menu citylist" role="menu" aria-labelledby="dropdownMenu1">
					<div class="group">
						<h3 style="font-size: 12px;color: #999; width: 68px;overflow: hidden;padding: 10px 10px 0;position: static;">国内城市</h3>
						<div class="citya" style="padding-left: 10px;">
							<a href="/service/上海" class="cities">上海</a>
							<a href="/service/北京" class="cities">北京</a>
							<a href="/service/广州" class="cities">广州</a>
							<a href="/service/深圳" class="cities">深圳</a>
							<a href="/service/天津" class="cities">天津</a>
							<a href="/service/杭州" class="cities">杭州</a>
							<a href="/service/南京" class="cities">南京</a>
							<a href="/service/苏州" class="cities">苏州</a>
							<a href="/service/成都" class="cities">成都</a>
							<a href="/service/武汉" class="cities">武汉</a>
							<a href="/service/重庆" class="cities">重庆</a>
							<a href="/service/西安" class="cities">西安</a>
						</div>
						<h3 style="font-size: 12px;color: #999; width: 68px;overflow: hidden;padding: 10px 10px 0;position: static;margin-top: 5px">国外城市</h3>
						<div class="citya" style="padding-left: 10px;">
							<a class="cities">东京</a>
							<a class="cities">首尔</a>
							<a class="cities">曼谷</a>
							<a class="cities">巴黎</a>
						</div>
						<a style="font-size: 12px;color: #999; overflow: hidden;position: static;margin-top: 10px;float: right" href="/service/cities/">更多城市 ></a>
					</div>
				</div>
			</li>
		</ul>
		<ul class="cd-main-nav">
			<li><a href= "#">店铺</a></li>
			<li><a href="#">目的地</a></li>
			<li><a href="#">Blog</a></li>
			<li style="background-color: #5c5d6a"><a data-toggle="modal" href="#login1" data-target="#login1" style="color: white">登陆</a></li>
			<li  style="background-color: #5c5d6a"><a data-toggle="modal" href="#regist1" data-target="#regist1" style="color: white">注册</a></li>
		</ul> <!-- .cd-main-nav -->
	</nav> <!-- .cd-main-nav-wrapper -->

	<a href="#" class="cd-nav-trigger cd-text-replace">菜单<span></span></a>
</header>
<main class="cd-main-content">
</main>
<div class="container">
<div class="row">
	<div class="whitebox" style="margin-top: 20px">
        <div class="col-sm-6"> <div style="height: 300px;    box-shadow: 0px 0px 25px 1px rgba(50, 50, 50, 0.1);"><div id="allmap" style="width: 100%;height: 100%"></div></div></div>
       <div class="col-sm-6">
           <div class="weather-card london">
               <div class="weather-wrapper">
           <div class="weather-icon sun"></div>
           <h1>14º</h1>
           <p>上海</p>
           </div>
               <div class="chart inline-legend grid">
                   <div id="main1" style="height:400px;top: -130px"></div>
               </div>
           </div>
       </div>
	<div id="timeline" class="timeline" style="top:50px">
		<button id="prev" class="prev">
			<i class=""><img src="{% static 'img/icon_time_arrow_left.png' %}" alt=""></i>
		</button>
		<button id="next" class="next">
			<i class=""><img src="{% static 'img/icon_time_arrow_right.png' %}" alt=""></i>
		</button>
		<ul id="dates" class="dates"><li>
            <a href="#2012" name="2011">XX</a>
            <hr class="onepx" /></li>
            <li><a href="#2013" name="2011">XX</a>
				<hr class="onepx" />
			</li>
            <li><a href="#2014" name="2011">XX</a>
				<hr class="onepx" />
			</li>
            <li><a href="#2015" name="2011">XX</a>
				<hr class="onepx" />
			</li>
            <li><a href="#2016" name="2011">XX</a>
				<hr class="onepx" />
			</li>
            <li><a href="#2017" name="2011">XX</a>
				<hr class="onepx" />
			</li>
            <li><a href="#2018" name="2011">XX</a>
				<hr class="onepx" />
			</li>

        </ul>

		<hr class="hrLine" />
		<div class="wrap">
			<ul class="issues" id="issues">
				<li id="2011">
					<div class="left"></div>
					<div class="right">
						<h5>XX</h5>
						<hr class="yearLine" />
						<span class="textArea">地图未加载成功</span>
					</div>
				</li>
				<li id="2012">
					<div class="left">
						<h5>XXX</h5>
						<hr class="yearLine" />
						<span class="textArea">地图未加载成功</span>
					</div>
					<div class="right"></div>
				</li>
				<li id="2013">
					<div class="left"></div>
					<div class="right">
						<h5>XXX</h5>
						<hr class="yearLine" />
						<span class="textArea">这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本。</span>
					</div>
				</li>
				<li id="2014">
					<div class="left">
						<h5>XXX</h5>
						<hr class="yearLine" />
						<span class="textArea">这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本。</span>
					</div>
					<div class="right"></div>
				</li>
				<li id="2015">
					<div class="left"></div>
					<div class="right">
						<h5>2015年</h5>
						<hr class="yearLine" />
						<span class="textArea">这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这一段测试文本test文本。</span>
					</div>
				</li>
				<li id="2016">
					<div class="left">
						<h5>2016年</h5>
						<hr class="yearLine" />
						<span class="textArea">这是一段测试文本test文本;这是一段测试文本test文本。</span>
					</div>
					<div class="right"></div>
				</li>
				<li id="2017">
					<div class="left"></div>
					<div class="right">
						<h5>2017年</h5>
						<hr class="yearLine" />
						<span class="textArea">这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本。</span>
					</div>
				</li>
				<li id="2018">
					<div class="left">
						<h5>2018年</h5>
						<hr class="yearLine" />
						<span class="textArea">这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本;这是一段测试文本test文本。</span>
					</div>
					<div class="right"></div>
				</li>
			</ul>
		</div>
    </div>
</div>
</div>
</div>


<div id="page">
	<a id="left-panel-link" href="#left-panel"><img src="{% static 'img/icon/mapicon.jpg' %}"></a>
</div>
<div id="left-panel" class="panel">
</div>


<div id="searchs" class="cd-main-search">
	<form action="{% url 'search1' %}" method="POST" >
        {% csrf_token %}
		<input type="search" placeholder="搜索旅行地/酒店/景点" class="form-vertical"  name="search11" >

		<div class="cd-select">
			<span>在</span>
			<select name="select-category">
				<option value="all-categories">所有</option>
				<option value="category1">旅行地</option>
				<option value="category2">店铺</option>
				<option value="category3">景点</option>
			</select>
			<span class="selected-value">所有</span>
		</div>
         <input  class="form-vertical" style="z-index: 100000;margin-top: 500px ;display: none" type="submit" value="提交">
	</form>

	<div class="cd-search-suggestions">
		<div class="news">
			<h3>News</h3>
			<ul>
				<li>
					<a class="image-wrapper" href="#"><img src="img/placeholder.png" alt="News image"></a>
					<h4><a class="cd-nowrap" href="#">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</a></h4>
					<time datetime="2016-01-12">Feb 03, 2016</time>
				</li>

				<li>
					<a class="image-wrapper" href="#0"><img src="img/placeholder.png" alt="News image"></a>
					<h4><a class="cd-nowrap" href="#0">Incidunt voluptatem adipisci voluptates fugit beatae culpa eum, distinctio, assumenda est ad</a></h4>
					<time datetime="2016-01-12">Jan 28, 2016</time>
				</li>

				<li>
					<a class="image-wrapper" href="#0"><img src="img/placeholder.png" alt="News image"></a>
					<h4><a class="cd-nowrap" href="#0">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto, esse.</a></h4>
					<time datetime="2016-01-12">Jan 12, 2016</time>
				</li>
			</ul>
		</div> <!-- .news -->

		<div class="quick-links">
			<h3>Quick Links</h3>
			<ul>
				<li><a href="#0">Find a store</a></li>
				<li><a href="#0">Accessories</a></li>
				<li><a href="#0">Warranty info</a></li>
				<li><a href="#0">Support</a></li>
				<li><a href="#0">Contact us</a></li>
			</ul>
		</div> <!-- .quick-links -->
	</div> <!-- .cd-search-suggestions -->

	<a href="#0" class="close cd-text-replace">Close Form</a>
</div> <!-- .cd-main-search -->
<div class="cd-cover-layer"></div> <!-- cover main content when search form is open -->

<!-- 会员登录  -->
<div class="modal fade" id="login1" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" >
	<div class="modal-dialog" style="width: 400px;margin-top: 5%;">
		<div class="modal-content" style="background-color: #eeeeeead;">
			<button type="button" class="close" data-dismiss="modal" aria-hidden="true" id="close-login" style="display: none">&times;</button>
			<div class="modal-body" style="margin: 15px;">
				<div id="form_container1">
					<input type="text" class="form-control" placeholder="手机号/用户名" id="login_number" value="admin" style="margin-bottom: 30px" />
					<input type="password" class="form-control" placeholder="密码" id="login_password" />
					<div id="rememberOrfindPwd"><span><input id="remember" type="checkbox" style="margin-bottom: -1.5px;"></span><span style="color:#000000;    margin-right: 80px;">记住密码</span><span style="color:#000000">忘记密码</span></div>
					<div style="text-align: center;margin-top: 5px;margin-bottom: 28px;"><input type="button" value="登录" class="button" id="login_btn" /></div>
				</div>
				<div style="margin-top: 50px;text-align: center;"><p>还没有账号?<a id='toRegist'>立即注册</a></p></div>
				<div class="social">
					<p>用其它方式登陆</p>
					<a href=""><img src="img/icon/qq.png" alt="qq"></a>
					<a href=""><img src="img/icon/weixin.png" alt="weixin"></a>
					<a href=""><img src="img/icon/weibo.png" alt="weibo"></a>
				</div>
			</div>
		</div><!-- /.modal-content -->
	</div><!-- /.modal -->
</div>
<div class="modal fade" id="regist1" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" >
	<div class="modal-dialog" style="width: 400px;margin-top: 5%;">
		<div class="modal-content" style="background-color: #eeeeeead;">
			<button type="button" class="close" data-dismiss="modal" aria-hidden="true" id="close-reg" style="display: none">&times;</button>
			<div class="modal-body" style="margin: 15px;">
				<div id="form_container2" style="padding-top: 25px;">
					<input type="text" class="form-control" value="admin"  placeholder="用户名" id="regist_account"style="margin-bottom: 30px" />
					<input type="password" class="form-control" placeholder="密码" id="regist_password1" style="margin-bottom: 30px"  />
					<input type="password" class="form-control" placeholder="确认密码" id="regist_password2" style="margin-bottom: 30px"  />
					<input type="text" class="form-control" placeholder="手机号" id="regist_phone" style="margin-bottom: 30px"  />
					<input type="text" class="form-control" placeholder="验证码" id="regist_vcode" style="margin-bottom: 30px"  />
					<!--<button id="getVCode" type="button" class="btn btn-success" >获取验证码</button>-->
					<input id="getVCode" type="button" class="btn btn-success" value="点击发送验证码" onclick="sendCode(this)" style="margin-bottom: 30px"  />
				</div>
				<input type="button" value="注册" class="btn btn-success" id="regist_btn" style="margin-bottom: 30px"  />
				<div style="text-align: center;"><p>已有账号?<a id='toLogin'>立即登陆</a></p></div>
			</div>
		</div><!-- /.modal-content -->
	</div><!-- /.modal -->
</div>
<div id="sad" style="width: 200px;height: 200px"><h1>sadas</h1></div>
<!--<div id='Login_start' style="position: absolute;" >-->
<script src="{% static 'js/jquery-3.3.1.min.js' %}"></script>
<script src="https://webapi.amap.com/maps?v=1.4.13&key=d137b3f7a39c6a29971ee376f76a80a9&plugin=AMap.PolyEditor"></script>
<script src="https://webapi.amap.com/maps?v=1.4.13&key=d137b3f7a39c6a29971ee376f76a80a9&plugin=AMap.Walking"></script>
 <script src="{% static 'scripts/flot/echarts.min.js' %}" type="text/javascript"></script>
<script src="https://a.amap.com/jsapi_demos/static/demo-center/js/demoutils.js"></script>
<script type="text/javascript">

    var map = new AMap.Map("allmap", {
        center: [121.50651, 30.83158],
        zoom: 16
    });

    // 当前示例的目标是展示如何根据规划结果绘制路线，因此walkOption为空对象
    var walkingOption = {
        hideMarkers:true,
    }
    var maps=[];
    // 步行导航
    var walking = new AMap.Walking(walkingOption)
    var walking2 = new AMap.Walking(walkingOption)
    //根据起终点坐标规划步行路线
    walking.search([121.50651, 30.83158], [121.50491, 30.83152], function(status, result) {
        // result即是对应的步行路线数据信息，相关数据结构文档请参考  https://lbs.amap.com/api/javascript-api/reference/route-search#m_WalkingResult
        if (status === 'complete') {
            if (result.routes && result.routes.length) {
                drawRoute(result.routes[0]);
                log.success('绘制步行路线完成');
                for (var i = 0, l = result.routes[0].steps.length; i < l; i++) { maps.push(result.routes[0].steps[i]);}
            }
        } else {
            log.error('步行路线数据查询失败' + result)
        }
    });
    walking2.search([121.50491, 30.83152], [121.50121, 30.83218], function(status, result) {
        // result即是对应的步行路线数据信息，相关数据结构文档请参考  https://lbs.amap.com/api/javascript-api/reference/route-search#m_WalkingResult
        if (status === 'complete') {
            if (result.routes && result.routes.length) {
                drawRoute2(result.routes[0]);
                log.success('绘制步行路线完成');
                for (var i = 0, l = result.routes[0].steps.length; i < l; i++) { maps.push(result.routes[0].steps[i]);}
                text()
            }
        } else {
            log.error('步行路线数据查询失败' + result)
        }
    });
    function drawRoute (route) {
        var path = parseRouteToPath(route)
        var startMarker = new AMap.Marker({
            position: path[0],
            icon: 'https://webapi.amap.com/theme/v1.3/markers/n/start.png',
            map: map
        })
        var endMarker = new AMap.Marker({
            position: path[path.length - 1],
            imageSize: new AMap.Size(20, 20),
            icon: 'https://webapi.amap.com/theme/v1.3/markers/n/mark_b1.png',
            map: map
        })
        var routeLine = new AMap.Polyline({
            path: path,
            isOutline: true,
            outlineColor: '#ffeeee',
            borderWeight: 2,
            strokeWeight: 5,
            strokeColor: '#83ffc4',
            lineJoin: 'round'
        })
        routeLine.setMap(map)
        // 调整视野达到最佳显示区域
    }
    function drawRoute2 (route) {
        var path = parseRouteToPath(route)

        var endMarker = new AMap.Marker({
            position: path[path.length - 1],
            icon: 'https://webapi.amap.com/theme/v1.3/markers/n/end.png',
            map: map
        })
        var routeLine = new AMap.Polyline({
            path: path,
            isOutline: true,
            outlineColor: '#ffeeee',
            borderWeight: 2,
            strokeWeight: 5,
            strokeColor: '#83ffc4',
            lineJoin: 'round'
        })
        routeLine.setMap(map)
        // 调整视野达到最佳显示区域

    }

    // 解析WalkRoute对象，构造成AMap.Polyline的path参数需要的格式
    // WalkRoute对象的结构文档 https://lbs.amap.com/api/javascript-api/reference/route-search#m_WalkRoute
    function parseRouteToPath(route) {
        var path = []

        for (var i = 0, l = route.steps.length; i < l; i++) {
            var step = route.steps[i]

            for (var j = 0, n = step.path.length; j < n; j++) {
              path.push(step.path[j])
            }
        }
        return path}
    function text() {
        var x="<li><a href='#m0'class='selected'>起点</a><hr class=\"onepx\"/></li>";
        var y="<li id='m0'><div class=\"left\"><h5></h5><hr class=\"yearLine\"/><span class=\"textArea\">今天天气怎么样，我们替你拟合了一条XXX。</span></div><div class=\"right\"><h5> &nbsp</h5></div></li>";
        for (var c = 0; c <maps.length; c++) {
            if(maps[c].road==''){x=x+"<li><a href='#m"+(c+1)+"'>"+"小径"+"</a><hr class=\"onepx\" /></li>"}
            else {x=x+"<li><a href='#m"+(c+1)+"'>"+maps[c].road+"</a><hr class=\"onepx\" /></li>"}
        }
        for (var j = 0; j <maps.length; j++) {
            if (j%2 == 0){y=y+"<li id='m"+(j+1)+"'><div class=\"left\"></div><div class=\"right\"><h5>"+maps[j].instruction+"</h5><hr class=\"yearLine\"/><span class=\"textArea\">这是一段测试文本test文本。</span></div></li>"}
            else{y=y+"<li id='m"+(j+1)+"'><div class=\"left\"><h5>"+maps[j].instruction+"</h5><hr class=\"yearLine\"/><span class=\"textArea\">这是一段测试文本test文本。</span></div><div class=\"right\"><h5> &nbsp</h5></div></li>"}
        }
        $("#dates").html(x);
        $("#issues").html(y)
    }

</script>
<script src="{% static 'js/bootstrap.min.js' %}"></script>
<script src="{% static 'js/modernizr.js' %}"></script>
<script type="text/javascript">
    //登录到注册
    $("#toRegist").on('click',function(){
        $("#close-login").trigger("click");
        $('#regist1').modal();
    });

    //注册到登录
    $("#toLogin").on('click',function(){
        $("#close-reg").trigger('click');
        $('#login1').modal();
    });
    var clock = '';
    var nums = 30;
    var btn;
    function sendCode(thisBtn) {
        btn = thisBtn;
        btn.disabled = true; //将按钮置为不可点击
        btn.value = '重新获取（'+nums+'）';
        clock = setInterval(doLoop, 1000); //一秒执行一次
    }

    function doLoop() {
        nums--;
        if (nums > 0) {
            btn.value = '重新获取（'+nums+'）';
        } else {
            clearInterval(clock); //清除js定时器
            btn.disabled = false;
            btn.value = '点击发送验证码';
            nums = 10; //重置时间
        }
    }

    $(document).ready(function(){
        $("#login_QQ").click(function(){
            alert("暂停使用！");
        });
        $("#login_WB").click(function(){
            alert("暂停使用！");
        });
        var myChart = echarts.init(document.getElementById('main1'));
        var option = {
            tooltip: {
                trigger: 'axis'
            },
            radar: [
                {
                    indicator: [
                        {text: '精力', max: 100,color:"#333"},
                        {text: '娱乐', max: 100,color:"#333"},
                        {text: '饥饿', max: 100,color:"#333"},
                        {text: '社交', max: 100,color:"#333"},
                        {text: '明确', max: 100,color:"#333"}
                    ],
                    radius: 80,
                    center: ['50%','60%'],
                }
            ],
            series: [
                {
                    type: 'radar',
                    data: [
                        {
                            value: [85, 90, 90, 95, 95],
                            name: '人物状态'
                        }
                    ],
                    itemStyle:{

                     normal:{

                        color:'#5CACEE'

                    }}
                }
            ]
        };
         myChart.setOption(option);

window.onresize = function() {

    myChart.resize();

}
    });
</script>
<script src="{% static 'js/main3.js' %}"></script> <!-- Resource jQuery -->
<script src="{% static 'js/jquery.panelslider.js' %}" type="text/javascript"></script>
<script>
    $('#left-panel-link').panelslider();
</script>
<script src="{% static 'js/swiper.min.js' %}" type="text/javascript"></script>
<script src="{% static 'js/jquery.mousewheel.js' %}" type="text/javascript"></script>
<script src="{% static 'js/jquery.timelinr-2.0.0.js' %}" type="text/javascript"></script>
<script type="text/javascript">
    $(function() {
        $().timelinr({
            autoPlay: false,
            autoPlayDirection: "forward",
            startAt: 1,
            mousewheel:  'false'
        });


        // 指定图表的配置项和数据
    });
</script>
<script type="text/javascript">

        </script>
</body>

</html>
