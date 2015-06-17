   // Using localSttorage for the list of visited pages
  if (localStorage.getItem("journey") === null) {
      localStorage.setItem('journey', "");
  }
  $(function() {
          // URL parameters
          function getParameterByName(name) {
            return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null;
          }
          var myParm = getParameterByName("topics");
          if (myParm == "" || myParm == undefined) { myParm = "default";}
  
          // Submenu
          $('.collapse').on('shown.bs.collapse', function(e) {
              $('.collapse').not(this).removeClass('in');
          });

          $('[data-toggle=collapse]').click(function(e) {
              $('[data-toggle=collapse]').parent('li').removeClass('active');
              $(this).parent('li').toggleClass('active');
          });
          // Add authors static html
          $("#left").html(AUTHORS);
          // Grid builder
          
          // Parameters:
          //option 1: show first topic if score(t1) > 20%. Otherwise no-topic (white)
          
          // option 2:  
          
          
          
          var c = 0;
          $.each(topicMatrix, function(i, row) {
              myi = i + 1;
              $("#grid").append("<div id='" + i + "' class='row'></div>");
              $.each(row, function(j, column) {
                  topic = column[0].split("-")[0]
                  topicSubtopic = topic + "-" + column[0].split("-")[1];
                  myj = j + 1
                  var coord = getCoordinates(i, j);
                  $("#" + i).append("<div id='" + i + "x" + Number(myj) + "' class='c c" + topic + "' t='" + topicSubtopic + "' style=\"left:" + coord[1] + "px;top:" + coord[0] + "px;\"></div>");
                  c += 1;
              })
          })
          //console.log("TOTAL PAGES= "+c);
          //$("#left").html("<p>"+c+" pages</p>");

          // Detail popup
          $(".row div")
              .mouseover(function() {
                  var pos = $(this).position();
                  var offs = $(this).offset();
                  if ($(this).attr("class") != "c c0")  {
					var classBgcolor = $(this).attr("class");
				  } else  {
					var classBgcolor = "c cC";  
				  }
                  var topic = $(this).attr("t");
                  var myid = $(this).attr('id').split("x");
                  if (myid[1] < 100) {
                      myposleft = pos.left + 107;
                  } else {
                      myposleft = pos.left - 60;
                  }
                  $("#detail").css("display", "block").addClass(classBgcolor).css("top", pos.top - 5 + "px").css("left", myposleft + "px");
                  $(this).css("border", "3px solid #424242");
                  $("#detail").html(view_detail(myid[0], myid[1], topic));
                  $("#detail").css("background-image", "");
              })
              .mouseout(function() {
                  $("#detail").css("display", "none").attr('class', '');
                  $(this).css("border", "0");
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
                      /////////////////////// RECHECK THIS left right keys
                      /*
						$(document).on( 'keydown', function ( e ) {
						  if ( e.keyCode === 37 ) { // key Left
							do_buttons(classBgcolor, "back")
						  }
						  if ( e.keyCode === 39 ) { // key Right
							do_buttons(classBgcolor, "forward")
						  }
						});
					  */
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
                      out = "topic  not specificied"
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
                  var page_image = '';//'''<p class="detail-p"><i>page %s of %s</i><br /><img " \
        //style=\'background-image: url("img/Throbber_allbackgrounds_monochrome.gif");background-repeat: no-repeat;background-position: \
        //center bottom;\' src="%s" /></p>';
                  //////////////////////////////////////////////////
                  //////////////////////////////////////////////////
                  var topicsStats = '<p class="detail-p"></p>';
                  if (topic != "0-0")  {
					myScoreValue = Math.round(Number(topicMatrix[row][column-1].split("-")[2])*100)
					myScoreHtml = "<h4>Topic score:<br />%s%</h4>"
				  }  else {
					 myScoreValue = '';
					 myScoreHtml = "";  
				  }
				  
                  if (column == 1) {
                      page_image = "";
                  }
                  return sprintf('<p>[id=%s] <b>[%s]</b> %s <br />by %s<br /><i>%s</i></p>\
        <p class="detail-p">Cover<br /><img src="data/diariesCovers/%s" /></p>\
        ' +myScoreHtml+ page_image, g["id"], topic, g["title"], g["author"], g["kind"], g["cover"], myScoreValue);
        //' + page_image, g["id"], topic, g["title"], g["author"], g["kind"], g["cover"], column, g["page_no"], mypageFile, g["page_no"]);              }
			  }
			  
              function view_reader_meta(row, column) {
                  var g = DATA[row];
                  var mypageFile = page_img_file_name(g["don"], Number(column), g["cover"]);
                  var page_image = '<p class="reader-p"><i>this page</i><br /><img class="enlarge" src="%s" width="70px"/></p>';
                  if (column == 1) {
                      page_image = "";
                  }
                  return sprintf('<small><i>no. %s</i></small><h1>%s <br />by %s <small><a href="http://www.acmssearch.sl.nsw.gov.au/s/search.html?collection=slnsw&form=simple&query=%s&type=1&meta_G_sand=&sort=&submit-search=Search" target="_slnsw">[more]</a></small>\
                  <h1><span class="topicsDia">Topics distribution:<table><tr><td>100-80%</td><td><tc class="c1" /></td></tr><tr><td>80-60%</td><td><tc class="c4" /><tc class="c3" /></td></tr><tr><td>60-40%</td><td><tc class="c5" /><tc class="c4" /><tc class="c1" /><tc class="c1" /><tc class="c5" /><tc class="c4" /></td></tr><tr><td>40-20%</td><td><tc class="c3" /><tc class="c3" /><tc class="c2" /><tc class="c1" /><tc class="c2" /><tc class="c3" /><tc class="c4" /><tc class="c5" /></td></tr><tr><td><20%</td><td><tc class="c2" /><tc class="c1" /><tc class="c1" /><tc class="c2" /><tc class="c1" /><tc class="c4" /><tc class="c3" /><tc class="c2" /><tc class="c2" /><tc class="c4" /><tc class="c5" /><tc class="c5" /><tc class="c4" /></td></tr></table>'+topicsChart(topicMatrix[row][column])+'</span></h1>\
                  <p>Kind: %s. <i>This is page %s from %s</i></p>\
                  <p class="reader-p">Cover<br /><img class="enlarge" src="data/diariesCovers/%s" width="70px"/></p>' + page_image, g["id"], g["title"], g["author"], g["author"].replace(" ", "+"), g["kind"], column, g["page_no"], g["cover"], mypageFile);
              }
              
              function topicsChart(pageInfo) {
                return (pageInfo);
              
              
//              <table><tr><td>100-80%</td><td><tc class="c1" /></td></tr><tr><td>80-60%</td><td><tc class="c4" /><tc class="c3" /></td></tr><tr><td>60-40%</td><td><tc class="c5" /><tc class="c4" /><tc class="c1" /><tc class="c1" /><tc class="c5" /><tc class="c4" /></td></tr><tr><td>40-20%</td><td><tc class="c3" /><tc class="c3" /><tc class="c2" /><tc class="c1" /><tc class="c2" /><tc class="c3" /><tc class="c4" /><tc class="c5" /></td></tr><tr><td><20%</td><td><tc class="c2" /><tc class="c1" /><tc class="c1" /><tc class="c2" /><tc class="c1" /><tc class="c4" /><tc class="c3" /><tc class="c2" /><tc class="c2" /><tc class="c4" /><tc class="c5" /><tc class="c5" /><tc class="c4" /></td></tr></table>
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
                          $(".c").css("background-image", "url('img/white-pill-7x5.png')");
                          $("#topicsView li").attr('class', '');

                          break;
                      case 'showTopics1':
                          $(".c1").css('background-image', '');
                          break;
                      case 'showTopics2':
                          $(".c2").css('background-image', '');
                          break;
                      case 'showTopics3':
                          $(".c3").css('background-image', '');
                          break;
                      case 'showTopics4':
                          $(".c4").css('background-image', '');
                          break;
                      case 'showTopics5':
                          $(".c5").css('background-image', '');
                          break;
                      case "subtopic":
                          //alert(mysubtopic);
                          $(".c").css("background-image", "url('img/white-pill-7x5.png')");
                          $("[t='" + mysubtopic + "']").css('background-image', '');
                          $("#" + mysubtopic).parent().siblings().addClass("bggrey");
                          $("#" + mysubtopic).parent().removeClass("bggrey");
                          break;
                      case 'journey':
                          // Get visited pages from and transform to string for $ selection
                          var myjourney = localStorage.getItem("journey").split(">").splice(1).join();
                          // Hide all pages
                          $(".c").css("background-image", "url('img/white-pill-7x5.png')");
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

              function getCoordinates(diaryId, pageNo) {
                  var row = diaryId * 8;
                  var column = pageNo * 7;
                  return [row, column];
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

              // Storage functions

              function storeme(Storage) {
                  if (typeof(Storage) !== "undefined") {
                      //if (localStorage.diarypages) {
                      localStorage.diarypages = Storage;
                      //} else {
                      //localStorage.diarypages = 1;
                      //}
                      document.getElementById("x").innerHTML = "You have clicked the button " + localStorage.diarypages + " time(s).";
                  } else {
                      document.getElementById("reader-main").innerHTML = "Sorry, your browser does not support web storage...";
                  }
              }

          })
