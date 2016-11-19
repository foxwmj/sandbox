(function(){
    var TIMEOUT = 10*1000;

    var mj_log = function(str) {
        // FIXME
        //console.log(str);
    }

    // return if need this 
    var titleChecker = function(value) {
        //mj_log(value.text());
        var res =value.text().indexOf("工程师") > -1;
        var dev = value.text().indexOf("开发") > -1;
        //mj_log(res);
        return res || dev;
    };

    var jobChecker = function(value) {
        var resSZ = value.text().indexOf("深圳") > -1;
        var resGZ = value.text().indexOf("广州") > -1;
        return resSZ || resGZ;
    }

    var jobBlackList = function(value) {
        var b1 = value.text().indexOf("策划") > -1;
        var b2 = value.text().indexOf("产品经理") > -1;
        return b1 || b2;
    }

    String.prototype.hashCode = function() {
      var hash = 0, i, chr, len;
      if (this.length == 0) return hash;
      for (i = 0, len = this.length; i < len; i++) {
        chr   = this.charCodeAt(i);
        hash  = ((hash << 5) - hash) + chr;
        hash |= 0; // Convert to 32bit integer
      }
      return hash;
    };

    var infoGetter = function(jqValue) {
        var res = new Array(7);
        var valid = true;
        jqValue.find("td").each(
            function(index, value){ 
                if (index == 0 ) { //name
                    mj_log($(value).text());
                    var link = $(value).find("a").prop("href");
                    if (link) {
                        link = link.replace(/&keywords=.*/, "");
                        res.push(link);
                    } else {
                        res.push("");
                    }
                    
                } else if (index == 1) { //job desc
                    mj_log($(value).text());
                    if (! titleChecker($(value))) {
                        valid = false;
                    }
                    if (! jobChecker($(value))) {
                        valid = false;
                    }
                    if (jobBlackList($(value))) {
                        valid = false;
                    }
                } else if (index == 2) { //school
                    mj_log($(value).text());
                } else if (index == 3) { //last job
                    mj_log($(value).text());
                } else if (index == 4) { //work years
                    mj_log($(value).text());
                } else if (index == 5) { //location
                    mj_log($(value).text());
                } else if (index == 6) { //time
                    mj_log($(value).text());
                }
                res.push($(value).text().replace(/\xA0/g, " "));
            }
        );
        return valid ? res : null;
    }
    
    /*
    var infoGetter = function(jqValue) {
        var res = new Array(7);
        var valid = true;
        jqValue.find("td").each(
            function(index, value){ 
                if (index == 0 ) { //name
                    mj_log($(value).text());
                    var link = $(value).find("a").prop("href");
                    if (link) 
                        res.push(link);
                    else
                        res.push("");
                    
                } else if (index == 1) { //job desc
                    mj_log($(value).text());
                    if (! titleChecker($(value))) {
                        valid = false;
                    }
                } else if (index == 2) { //school
                    mj_log($(value).text());
                } else if (index == 3) { //last job
                    mj_log($(value).text());
                } else if (index == 4) { //work years
                    mj_log($(value).text());
                } else if (index == 5) { //location
                    mj_log($(value).text());
                } else if (index == 6) { //time
                    mj_log($(value).text());
                }
                res.push($(value).text().replace(/\xA0/g, " "));
            }
        );
        return valid ? res : null;
    }
    */

    var startDayString = function() {
        var today = new Date();
        today.setDate(today.getDate() - 1); // FIXME
        var dd = today.getDate();
        var mm = today.getMonth()+1; //January is 0!

        var yyyy = today.getFullYear();
        if(dd<10){
            dd='0'+dd
        } 
        if(mm<10){
            mm='0'+mm
        } 

        return yyyy+'-'+mm+'-'+dd;
    };



    var dayString = function() {
        var today = new Date();
        //today.setDate(today.getDate() - 4); // FIXME
        var dd = today.getDate();
        var mm = today.getMonth()+1; //January is 0!

        var yyyy = today.getFullYear();
        if(dd<10){
            dd='0'+dd
        } 
        if(mm<10){
            mm='0'+mm
        } 

        return yyyy+'-'+mm+'-'+dd;
    };


    var runOncePage = function(keyword, isNextPage) {
        $("iframe#myIframe").one("load", {key: keyword, next: isNextPage}, iframeOnLoad);

        var iframeContents = $("iframe#myIframe").contents();
        // keyword
        iframeContents.find("#ctl00_ContentPlaceHolder1_QueryBar1_txtAll").val(keyword);
        // day
        var startStr = startDayString();
        var dayStr = dayString();
        iframeContents.find("#ctl00_ContentPlaceHolder1_QueryBar1_LastUpdateTime_tbDateBegin").val(startStr);
        iframeContents.find("#ctl00_ContentPlaceHolder1_QueryBar1_LastUpdateTime_tbDateEnd").val(dayStr);

        // page num
        // FIXME
        iframeContents.find("#ctl00_ContentPlaceHolder1_ddlPerPageNum").val(50);
        
        // click
        if (isNextPage) {
            iframeContents.find("#ctl00_ContentPlaceHolder1_lbLastPage")[0].click();
        } else {
            iframeContents.find("#ctl00_ContentPlaceHolder1_QueryBar1_btnSearch")[0].click();
        }
    };

/*

    var runOncePage = function(keyword, isNextPage) {
        $("iframe#docs-List").one("load", {key: keyword, next: isNextPage}, iframeOnLoad);

        var iframeContents = $("iframe#docs-List").contents();
        // keyword
        iframeContents.find("#ctl00_ContentPlaceHolder1_QueryBar1_txtAll").val(keyword);
        // day
        iframeContents.find("#ctl00_ContentPlaceHolder1_QueryBar1_LastUpdateTime").val(1); // FIXME

        // page num
        iframeContents.find("#ctl00_ContentPlaceHolder1_ddlPerPageNum").val(50);
        
        // click
        if (isNextPage) {
            iframeContents.find("#ctl00_ContentPlaceHolder1_lbLastPage")[0].click();
        } else {
            iframeContents.find("#ctl00_ContentPlaceHolder1_QueryBar1_btnSearch")[0].click();
        }
    };
*/

    var nextPage = function(keyword) {
        var iframeContents = $("iframe#myIframe").contents();
        var hasNext = (iframeContents.find("#ctl00_ContentPlaceHolder1_lbLastPage").prop('href') != "");

        if (hasNext) {
            runOncePage(keyword, true);
            return true;
        } else {
            return false;
        }
    }

    var collectResult = function() {
        var Save = new Array();
        var infoArray = null;
        var infoHash = null;
        var resume = null;
        var resumeHash = null;
        var hasError = false;
        $("iframe#myIframe").contents().find("#ctl00_ContentPlaceHolder1_PithinessList1_table").find("tr[rowindex]").each(
                function(index, element){
                    if (index % 2 === 0 ) {
                        // info
                        hasError = false;

                        infoArray = infoGetter($(element));
                        if (infoArray == null) {
                            hasError = true;
                        } else {
                            var hash = new String(infoArray.join()).hashCode();
                            infoHash = hash;
                            mj_log(hash);
                        }
                        return;
                    }
                    if (index % 2 === 1 ) {
                        //resume = $(element).text().replace(/\xA0/g, " ");
                        resume = $(element).find(".keyNote").text().replace(/\xA0/g, " ");

                        var hash = new String(resume).hashCode();
                        resumeHash = hash;
                        mj_log(hash);
                        // resume
                        if (! hasError) {
                            //Save.push([infoHash, resumeHash, infoArray, resume]);
                            Save.push([infoHash, resumeHash, infoArray, resume]);
                        }
                    }
        });

        return Save;
    };

/*
    var collectResult = function() {
        var Save = new Array();
        var infoArray = null;
        var infoHash = null;
        var resume = null;
        var resumeHash = null;
        var hasError = false;
        //$("tbody","#ctl00_ContentPlaceHolder1_PithinessList1_table").find("tr").each(
        $("iframe#docs-List").contents().find("#ctl00_ContentPlaceHolder1_PithinessList1_table").find("tr").each(
                function(index, element){
                    if (index === 0 ) {
                        mj_log("head");
                        return; // header
                    }
                    if (index % 3 === 1 ) {
                        // info
                        hasError = false;

                        infoArray = infoGetter($(element));
                        if (infoArray == null) {
                            hasError = true;
                        } else {
                            var hash = new String(infoArray.join()).hashCode();
                            infoHash = hash;
                            mj_log(hash);
                        }
                        return;
                    }
                    if (index % 3 === 2 ) {
                        resume = $(element).text().replace(/\xA0/g, " ");
                        var hash = new String(resume).hashCode();
                        resumeHash = hash;
                        mj_log(hash);
                        // resume
                    }
                    if (index % 3 === 0) {
                        // finish
                        if (! hasError) {
                            //Save.push([infoHash, resumeHash, infoArray, resume]);
                            Save.push([infoHash, resumeHash, infoArray, resume]);
                        }
                    }
        });

        return Save;
    };
    */

    var iframeOnLoad = function(event) {
        //alert(event.data.key + " " + event.data.next);

        var res = collectResult();
        //console.log(res);
        //console.log($.toJSON(res));

        $.ajax({
          type: "POST",
          contentType: "application/json; charset=gb2312",
          url: 'http://127.0.0.1:5000/post',
          data: $.toJSON(res),
          dataType: "json"
        });
        


        if (! nextPage(event.data.key)) {
            setTimeout(runOnceOption, TIMEOUT);
            console.log("Run next Option");
        }
    }

    var runOnceOption = function() {
        if (timeValid()) {
            var len = Option.length;
            //if (currentOptionIndex >= len) return;
            
            if (currentOptionIndex >= len) {
                currentOptionIndex = 0;
                setTimeout(runOnceOption, BIG_INTERVAL);
                console.log("wait next");
                return;
            }

            if (currentOptionIndex == 0) {
                console.log("===================== Run Once ===============");
            }
            runOncePage(Option[currentOptionIndex], false)
            currentOptionIndex += 1;

        } else {
            setTimeout(runOnceOption, BIG_INTERVAL);
            console.log("free time");
        }
    }

    var timeValid = function() {
        // FIXME
        /**/
        var now = new Date();
        var begin = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 9, 0, 0, 0);
        var end = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 22, 0, 0, 0);
        return begin < now && now < end;
        /**
        return true;
        /**/
    }

    var BIG_INTERVAL = 30 * 60 * 1000;

    var currentOptionIndex = 0;
    //var Option = ["acm", "优秀"];
    //var Option = ["android","安卓","acm", "数学建模", "算法", "优秀", "奖", "top"];
    //var Option = ["iOS","acm", "数学建模", "算法", "优秀", "奖", "top","github","微软","百度","阿里","迅雷","谷歌","google"];
    var Option = ["icpc","数学建模","算法","优秀", "奖","普联技术","阿里","迅雷","谷歌","清华大学","华中科技大学","浙江大学","电子科技大学","北京航空航天大学","武汉大学","西安电子科技大学","北京邮电大学","东北大学","上海交通大学","同济大学","南京大学","哈尔滨工业大学","北京交通大学","北京大学","中南大学","重庆大学","吉林大学","东南大学","中山大学","华南理工大学","华南农业大学"];
    //var Option = ["普联技术","阿里","迅雷","谷歌","清华大学","华中科技大学","浙江大学","电子科技大学","北京航空航天大学","武汉大学","西安电子科技大学","北京邮电大学","东北大学","上海交通大学","同济大学","南京大学","哈尔滨工业大学","北京交通大学","北京大学","中南大学","重庆大学","吉林大学","东南大学","中山大学","华南理工大学","华南农业大学"];
    

    //runOncePage("acm", false);
    runOnceOption();
})();

