// Generated by CoffeeScript 1.6.1
(function(){$(document).ready(function(){$.tablesorter.addParser({id:"skillz",is:function(e){return!1},format:function(e){return e.toLowerCase().replace(/high/,2).replace(/medium/,1).replace(/low/,0)},type:"numeric"});$("#skills-table").tablesorter({sortList:[[1,1],[2,1]],headers:{1:{sorter:"skillz"},2:{sorter:"skillz"}}});$("#gist-hover").click(function(e){return $(".gist").toggle()});$(".foursquare").click(function(e){var t,n;n=350;if($(this).hasClass("big")){$(".foursquare").show().animate({width:window.startingWidth,height:window.startingWidth},n);$(this).removeClass("big")}else{window.startingWidth=$(this).width();t=$(this).width()*2+2*parseInt($(this).css("margin-top"));$(this).siblings().animate({width:"0px"},n);$(this).parent().siblings().find("div").each(function(e){return $(this).animate({height:"0px"},n)});$(this).animate({width:t,height:t},n,function(e){$(".foursquare").not($(this)).hide();$(this).addClass("big")})}});$("#show-table").click(function(e){$("#skills-row").toggle()});$(".tile img, .tile .blk-label, .tile .blk-label label").click(function(e){var t,n;$(".modal-body").html($(this).siblings(".desc").html());t=$(e.target).prop("tagName");n="";t==="LABEL"?n=$(this).html():t==="DIV"?n=$(this).find("label").html():n=$(this).siblings(".blk-label").find("label").html();$("#modalLabel").html(n);$("#portfolioModal").modal("show");_gaq.push(["_trackEvent","Portfolio",n])});$("#freeOfficeButton").click(function(e){_gaq.push(["_trackEvent","Buttons","Office Hours"])})})}).call(this);