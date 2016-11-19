(function(){
    var ms = {
        "31" : "上海",
        "53" : "云南",
        "51" : "四川",
        "64" : "宁夏",
        "34" : "安徽",
        "37" : "山东",
        "44" : "广东",
        "45" : "广西",
        "65" : "新疆",
        "66" : "新疆兵团",
        "32" : "江苏",
        "36" : "江西",
        "41" : "河南",
        "33" : "浙江",
        "46" : "海南",
        "42" : "湖北",
        "43" : "湖南",
        "91" : "澳门",
        "62" : "甘肃",
        "35" : "福建",
        "54" : "西藏",
        "52" : "贵州",
        "50" : "重庆",
        "61" : "陕西",
        "63" : "青海",
        "81" : "香港",
        "15" : "内蒙",
        "11" : "北京",
        "71" : "台湾",
        "22" : "吉林",
        "12" : "天津",
        "14" : "山西",
        "13" : "河北",
        "21" : "辽宁",
        "23" : "黑龙江"
    };


    var imp = {
        "44" : "广东",
        "45" : "广西",
        "36" : "江西",
        "46" : "海南",
        "42" : "湖北",
        "43" : "湖南",
        "91" : "澳门",
        "35" : "福建",
        "81" : "香港",
        "71" : "台湾",
        "22" : "吉林",
        "21" : "辽宁",
        "23" : "黑龙江"
    };
    

    var checkID = function(value) {
        var len = value.length;
        var ok = true;
        for (var i = 0; i < value.length; ++i) { 
            var c = value.charAt(i) ;
            if (! ('0' <= c && c <= '9' || c == 'x' || c == 'X')) ok = false;
        }

        return len == 18 && ok;
    };

    var checkID_2 = function(value) {
        var len = value.length;
        var ok = true;
        for (var i = 0; i < value.length; ++i) { 
            var c = value.charAt(i) ;
            if (! ('0' <= c && c <= '9')) ok = false;
        }

        return (len == 6 || len == 5) && ok;
    };


    var runOnceOption = function() {
        $("span.value").each(
                function(index, value) {
                    var t = $(value).text();

                    if (checkID(t)) {
                        var s2 =  t.substr(0, 2);
                        var val_province = ms[s2];

                        if (s2 in imp) {
                            $(value).after(" <span style='color:red; font-weight:bold;'>"+val_province+"</span> ");
                        } else if (s2 in ms) {
                            $(value).after(" "+val_province+" ");
                        }
                    }
                }
        );

        $("span.value").each(
                function(index, value) {
                    var t = $(value).text();

                    if (checkID_2(t)) {
                        $(value).after(" <a href='https://hrc.tencent.com/preview.php?id="+ t +"'>link</a>");
                    }
                }
        );
        



    }
    

    runOnceOption();
})();


