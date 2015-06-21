 // Using localSttorage for the list of visited pages
if (localStorage.getItem("journey") === null) {
  localStorage.setItem('journey', "");
}
$(function() {
  // URL parameters
  function getParameterByName(name) {
    return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null;
  }
  
  // Submenu
  $('.collapse').on('shown.bs.collapse', function(e) {
      $('.collapse').not(this).removeClass('in');
  });

  $('[data-toggle=collapse]').click(function(e) {
      $('[data-toggle=collapse]').parent('li').removeClass('active');
      $(this).parent('li').toggleClass('active');
  });
  // Parameters:
  //option 1: show first topic if score(t1) > 20%. Otherwise no-topic (white)
  var thershold = getParameterByName("th");
  if (thershold == "" || thershold == undefined) { thershold = 0.20;}
  //var thershold = 0.20;  
  // option 2:  
          
  var c = 0;
  $.each(topicMatrix, function(i, row) {
    myi = i + 1; 
    var myAuthor = DATA[i]["author"];
    myAuthorLabel = "<span class=\"author\">"+myAuthor+"</span>";;
    if (Number(i)>0) {
      if (DATA[i-1]["author"] == myAuthor) { myAuthorLabel = "";}
    }
    $("#grid").append("<div id='" + i + "' class='row'>"+myAuthorLabel+"<div></div></div>");
    $.each(row, function(j, column) {
      if (parseFloat(column[0].split("-")[2]) < thershold)  {
        topic = 0; subTopic = 0;
      } else {
        topic = column[0].split("-")[0];
        subTopic = column[0].split("-")[1];
      }
      topicSubtopic = topic + "-" + subTopic;
      myj = j + 1
      $("#" + i + ">div").append("<div id='" + i + "x" + Number(myj) + "' class='c c" + topic + "' t='" + topicSubtopic + "'></div>");
      c += 1;
    })
  })
  // Detail popup
  $(".row div div")
    .mouseover(function( event ) {
      var pos = $(this).position();
      var offs = $(this).offset();
      if ($(this).attr("class") != "c c0")  {
  var classBgcolor = $(this).attr("class");
  } else  {
  var classBgcolor = "c cC";  
  }
      var topic = $(this).attr("t");
      var myid = $(this).attr('id').split("x");
 /////////////////////// FIXME
 console.log(pos.left);
      if (pos.left > 0) {
        correctionLeft = 10;
      } else {
        correctionLeft = 10;
      }
      $("#detail").css("display", "block").addClass(classBgcolor).css("top", event.pageY + "px").css("left", event.pageX + correctionLeft + "px");
      $(this).css("border", "3px solid #424242");
      $("#detail").html(view_detail(myid[0], myid[1], topic));
      $("#detail").css("background-image", "");
    })
  .mouseout(function() {
    $("#detail").css("display", "none").attr('class', '');
    $(this).css("border", "1px solid #fff");
  })
  .click(function() {
      //if ($(this).css('background-image') == "none")  {
      main(this.id);
      //}
  });

  // Reader close
  $("#reader-close img, #reader-overlay").click(function() {
    $("#reader").css("display", "none");
    $("#reader-overlay").css("display", "none");
    $("#reader").css("display", "none").attr('class', '');
  });
  $(document).on('keydown', function(e) {
    if (e.keyCode === 27) { // key ESC
        $("#reader").css("display", "none");
        $("#reader-overlay").css("display", "none");
        $("#reader").css("display", "none").attr('class', '');
    }
  });

  // buttons: show/hide topics
  $("#showAllTopics").click(function() {
      topicsView("show");
  });
  $("#hideAllTopics").click(function() {
      topicsView("hide");
  });
  $("#topicsView li a").click(function() {
      $("#reader").css("display", "none");
      $("#reader-overlay").css("display", "none");
      $("#reader").css("display", "none").attr('class', '');
      var myid = $(this).attr('id');
      topicsView("hide");
      topicsView(myid);
  });
  $("#showJourney").click(function() {
      var myid = $(this).attr('id');
      topicsView("journey");
  });
  $("nav ul li a").click(function() {
      var mysubtopic = $(this).attr('id');
      topicsView("hide");
      topicsView("subtopic", mysubtopic);
  });

  // non-anonymous functions:

  function main(myid) {
    var myids = myid.split("x");
    var myid = "#" + myid;
    // Reader popup      
    // Check pages back & forward:
    var go = "no";
    if (Number(myids[1]) >= 1 && Number(myids[1]) <= DATA[myids[0]]["page_no"]) {
      go = "yes";
    } else {
      go = "no";
    }
    if (go == "yes") {
      $("#reader").css("display", "none").attr('class', '');
      var classBgcolor = $(myid).attr("class");
      var code = $(myid).attr("t");
      $("#reader").css("display", "block");
      if (classBgcolor == "") {
          classBgcolor = myid[2];
      }
      if (classBgcolor == "c c0") {
          classBgcolor = "c cC";
      }
      $("#reader").addClass(classBgcolor);
      $("#reader-overlay").css("display", "block");
      $(".browser").addClass(classBgcolor);
      $("#detail").css("display", "none").attr('class', '');
      // Store visited page in localstore:
      var journey = localStorage.getItem('journey') + ">" + myid;
      localStorage.setItem('journey', journey);
      myJourney(myid, "add");

      var buttons = "<p id_track=\"" + myids[0] + "x" + myids[1] + "x" + classBgcolor + "\"><a class=\"nav_diary\" id=\"back\">BACK</a> -";
      buttons += "<a class=\"nav_diary\" id=\"forward\">FORWARD</a> - ";
      buttons += "[<a id=\"add_to_journey\" onClick=\"myJourney(" + myid + ", \"remove\");\">remove from visited</a>]";
      buttons += " ( <a href=\"data/diariesPages/" + DATA[myids[0]]["diary_id"] + "/" + pages[myids[0]][Number(myids[1])-1] + ".txt\"";
      buttons += " target=\"_page\">" + DATA[myids[0]]["diary_id"] + "/" + pages[myids[0]][Number(myids[1])-1] + "</a>) ";
      buttons += " (<a href=\"http://transcripts.sl.nsw.gov.au/api/node/" + pages[myids[0]][myids[1]] + "\" target=\"_api\">API</a>) (<a href=\"http://transcripts.sl.nsw.gov.au/node/" + DATA[myids[0]]["diary_id"] + "\" target=\"_diary\">Diary</a> ";
      buttons += ")</p><p class=\"topic\">" + get_topic_name(code, TOPICS) + "</p>";
      $("#reader-buttons").html(buttons);
      view_reader_text(myids[0], myids[1] - 1);
      $("#meta").html(view_reader_meta(myids[0], myids[1]));
      enlarge();
      //do_buttons();
      $(".nav_diary").click(function() {
        do_buttons(classBgcolor, this.id, topic)
      });
    }
  }

  function myJourney(myid, action) {
    var x = action; // Other options to define: remove, get["all", "last", "first"], 
    //return;
  }

  function do_buttons(classBgcolor, direction, topic) {
    var myid = $(".nav_diary").parent().attr("id_track").split("x");
    // Buttons
    if (Number(myid[1]) >= 1 && Number(myid[1]) < DATA[myid[0]]["page_no"]) {
      go = "yes";
    } else {
      go = "no";
    }
    if (Number(myid[1] - 1) == 0 && direction == "back") {
      go = "no";
    }
    if (Number(myid[1]) == DATA[myid[0]]["page_no"] && direction == "back") {
      go = "yes";
    }
    if (go == "yes") {
      if (direction == "back") {
          val = Number(myid[1]) - 1
      } else {
          val = Number(myid[1]) + 1;
      }
      view_reader_text(myid[0], val, DATA);
      $("#meta").html(view_reader_meta(myid[0], val, DATA));
      main(myid[0] + "x" + val);
    }
  }

  function get_topic_name(code, TOPICS) {
    if (code != "0-0") {
        topic = "#showTopics" + code.split("-")[0];
        var out = $(topic).html();
        $.each(TOPICS, function(i, val) {
            if (val["code"] == code) {
                out += " > " + val["topic"];
            }
        });
    } else {
        out = "no relevant topic"
    }
    return out;
  }

  function enlarge() {
    // FIXME Too simple images enlarger
    $("img.enlarge")
      .mouseover(function() {
         $(this).addClass("enlarged");
     })
       .click(function() {
         $(this).removeClass("enlarged");
     })
  }

  function view_detail(row, column, topic) {
    var g = DATA[row];
    var mypageFile = page_img_file_name(g["don"], Number(column), g["cover"]);
    var page_image = '';
    var topicsStats = '<p class="detail-p"></p>';
    if (topic != "0-0")  {
      myScoreValue = Math.round(Number(topicMatrix[row][column-1][0].split("-")[2])*100)
      myScoreHtml = "<h4>Topic score:<br />%s%</h4>"
    }  else {
       myScoreValue = '';
       myScoreHtml = "";  
    }

    if (column == 1) {
        page_image = "";
    }
    return sprintf('<p>[id=%s] %s <br />by %s<br /><i>%s</i></p>\
    <p>%s</p>\
    ', g["id"], g["title"], g["author"], g["kind"], topicsChart(topicMatrix[row][column-1]));
  }

  function view_reader_meta(row, column) {
    var g = DATA[row];
    var mypageFile = page_img_file_name(g["don"], Number(column), g["cover"]);
    var page_image = '<p class="reader-p"><i>this page</i><br /><img class="enlarge" src="%s" width="70px"/></p>';
    if (column == 1) {
        page_image = "";
    }
    return sprintf('<small><i>no. %s</i></small><h1>%s <br />by %s <small><a href="http://www.acmssearch.sl.nsw.gov.au/s/search.html?collection=slnsw&form=simple&query=%s&type=1&meta_G_sand=&sort=&submit-search=Search" target="_slnsw">[more]</a></small>\
    <h1><span class="topicsDia">Topics distribution:'+topicsChart(topicMatrix[row][column-1])+'</span></h1>\
    <p>Kind: %s. <i>This is page %s from %s</i></p>\
    <p class="reader-p">Cover<br /><img class="enlarge" src="data/diariesCovers/%s" width="70px"/></p>' + page_image, g["id"], g["title"], g["author"], g["author"].replace(" ", "+"), g["kind"], column, g["page_no"], g["cover"], mypageFile);
  }
  function type(val){
    return Object.prototype.toString.call(val).replace(/^\[object (.+)\]$/,"$1").toLowerCase();
  }

  function topicsChart(pageInfo) {
    var table = "<table><tr>"; var tablec = "</tr></table>";
    var td = "<td>"; var tdc = "</td>"; var tc = "<tc  title=\""; var tc1 = "\" class=\"c"; var tcc="\"></tc>";
    var myTopic = ""; var mySubTopic = ""; var myScore = "";
    var chart0 = "";var chart1 = "";var chart2 = "";var chart3 = "";var chart4 = "";var chart5 = "";
    // group elements by score percentage
    $.each(pageInfo, function(i, val) {
      myScore = parseFloat(val.split("-")[2]);
      mySubTopic = val.split("-")[1];
      myTopic = val.split("-")[0];
      code = val.split("-")[0]+"-"+val.split("-")[1]
      if (myScore >= 0.80)  {
        chart0 += tc+get_topic_name(code, TOPICS)+tc1+myTopic+tcc; 
      } else if (myScore < 0.80 && myScore >= 0.60)  {
        chart1 += tc+get_topic_name(code, TOPICS)+tc1+myTopic+"("+myScore+")"+tcc;
      } else if (myScore < 0.60 && myScore >= 0.40)  {
        chart2 += tc+get_topic_name(code, TOPICS)+tc1+myTopic+" ("+myScore+")"+tcc;
      } else if (myScore < 0.40 && myScore >= 0.20)  {
        chart3 += tc+get_topic_name(code, TOPICS)+tc1+myTopic+" ("+myScore+")"+tcc;
      } else if (myScore < 0.20 && myScore > 9.99)  {
        chart4 += tc+get_topic_name(code, TOPICS)+tc1+myTopic+" ("+myScore+")"+tcc;
      } else {
        chart5 += tc+get_topic_name(code, TOPICS)+tc1+myTopic+" ("+myScore+")"+tcc;
      }
    })
    return table+"<td>100-80%</td>"+td+chart0+tdc+"</tr><tr><td>80-60%</td>"+td+chart1+tdc+"</tr><tr><td>60-40%</td>"+td+chart2+tdc+"</tr><tr><td>40-20%</td>"+td+chart3+tdc+"</tr><tr><td>20-10%</td>"+td+chart4+tdc+tablec;
  }

  function view_reader_text(row, column) {
    var g = DATA[row];
    var path = "data/diariesPages/" + g["diary_id"] + "/" + pages[row][column] + ".txt";
    $("#reader-text pre").load(path);
    return;
  }

  function page_img_file_name(pre, suf, cover) {
    var pre = 'http://transcripts.sl.nsw.gov.au/sites/all/files/' + pre;
    var mysuf = '';
    var s = suf.toString();
    switch (s.length) {
      case 1:
        mysuf = "00" + s;
        break;
      case 2:
        mysuf = "0" + s;
        break;
      case 3:
        mysuf = s;
        break;
      default:
        return 'data/diariesCovers/' + cover
        break;
    }
      return pre + mysuf + "h.jpg";
  }

  function topicsView(topic, mysubtopic) { // Show/hide pages according to topics, visited,...
    $("#journey").css('display', 'none');
    switch (topic) {
      case 'show':
        $(".c").css("background-image", "");
        $("#topicsView li").attr('class', '');
        break;
      case 'hide':
        $(".c").css("background-image", "url('img/7x7grey.png')");
        $("#topicsView li").attr('class', '');
          break;
      case 'showTopics1':
        $("ul.navbar-nav li").removeClass("bggrey");
        $(".c1").css('background-image', '');
        break;
      case 'showTopics2':
        $("ul.navbar-nav li").removeClass("bggrey");
        $(".c2").css('background-image', '');
        break;
      case 'showTopics3':
        $("ul.navbar-nav li").removeClass("bggrey");
        $(".c3").css('background-image', '');
        break;
      case 'showTopics4':
        $("ul.navbar-nav li").removeClass("bggrey");
        $(".c4").css('background-image', '');
        break;
      case 'showTopics5':
        $("ul.navbar-nav li").removeClass("bggrey");
        $(".c5").css('background-image', '');
        break;
      case "subtopic":
        $(".c").css("background-image", "url('img/7x7grey.png')");
        $("[t='" + mysubtopic + "']").css('background-image', '');
        $("#" + mysubtopic).parent().siblings().addClass("bggrey");
        $("#" + mysubtopic).parent().removeClass("bggrey");
        break;
      case 'journey':
        // Get visited pages from and transform to string for $ selection
        var myjourney = localStorage.getItem("journey").split(">").splice(1).join();
        // Hide all pages
        $(".c").css("background-image", "url('img/7x7grey.png')");
        // show visited & put them class journey -> z-index:5;
        $(myjourney).css('background-image', '');
        /////////////////////////////////////////////////////////////////////
        // Draw arrows --> Check d3js options for this (??)
        //check http://www.w3.org/TR/SVG/paths.html#PathData 
        //and raphaeljs: http://raphaeljs.com/reference.html#Paper.path 

        //$("#journey").css('display','block');
        break;
      default:
        var a = 1;
    }
  }


  function sprintf() {
    // from http://stackoverflow.com/questions/610406/javascript-equivalent-to-printf-string-format 
    // by Luke Madhanga
    var args = arguments,
      string = args[0],
      i = 1;
    return string.replace(/%((%)|s|d)/g, function(m) {
      // m is the matched format, e.g. %s, %d
      var val = null;
      if (m[2]) {
        val = m[2];
      } else {
        val = args[i];
        // A switch statement so that the formatter can be extended. Default is %s
        switch (m) {
          case '%d':
            val = parseFloat(val);
            if (isNaN(val)) {
              val = 0;
            }
            break;
        }
        i++;
      }
      return val;
    });
  }
})
