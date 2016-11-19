(function(){
    var run = function() {
        //var Option = ["iOS","acm", "数学建模", "算法", "优秀", "奖", "top","github","微软","百度","阿里","迅雷","谷歌","google"];
        //var Option = ["iOS","acm", "数学建模", "算法", "优秀", "奖", "top","github","阿里","迅雷","谷歌","清华大学","华中科技大学","浙江大学","电子科技大学","北京航空航天大学","武汉大学","西安电子科技大学","北京邮电大学","东北大学","上海交通大学","同济大学","南京大学","哈尔滨工业大学","北京交通大学","北京大学","中南大学","重庆大学","吉林大学","东南大学","中山大学","华南理工大学","华南农业大学"];
        var Option = ["雅虎","中兴","京东","百度","华为","Google","支付宝","网易","搜狐","iOS","android","安卓","icpc","数学建模","算法","优秀", "奖","普联","阿里","迅雷","谷歌","清华大学","华中科技大学","浙江大学","电子科技大学","北京航空航天大学","武汉大学","西安电子科技大学","北京邮电大学","东北大学","上海交通大学","同济大学","南京大学","哈尔滨工业大学","北京交通大学","北京大学","中南大学","重庆大学","吉林大学","东南大学","中山大学","华南理工大学","华南农业大学"]; 
        //var Option = ["工程师"];

        var res = document.body.innerHTML;
        for (var x in Option){
            //console.log(x);
            var regex = new RegExp(Option[x]+"(?!.%3f)", 'gi');
            res = res.replace(regex, "</span><span style='color:red; font-weight:bold;'>"+Option[x]+"</span><span>");

            //res = res.replace(Option[x],"<span style='color:red'>"+Option[x]+"</span>","gi");
        }


        var year = [ "一年以上", "三年以上", "二年以上"];

        for (var x in year){
            var regex = new RegExp(">"+year[x]+"<", 'gi');
            res = res.replace(regex, " style='color:red; font-weight:bold;'> "+year[x]+" <");
        }





            document.body.innerHTML = res;
    }

    run();
})();


