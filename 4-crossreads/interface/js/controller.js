function listControl($scope,$http, $location, $rootScope){

	$http.get("data/diaries.json").success(function(data){
		$scope.diaries = data;
    $rootScope.diaries = data; // on root scope

	});

	$http.get("data/topics.json").success(function(data){
		$scope.topics = data;
	});

	$http.get("data/vars.json").success(function(data){
		$scope.vars = data;
	});

	$scope.getTopic = function (mallet_id, what) {
	    label = "unknown";
	    color = "red";
	    $scope.topics.forEach(function(el){
		    if (el.mallet_ids_inluded.indexOf(mallet_id) != -1) {
			    label = el.label;
			    color = $scope.vars["topic_groups"][parseInt(el.tid.toString().slice(0,1))-1]["color"];
          mallet_ids_inluded = el.mallet_ids_inluded;
          tid = el.tid;
		    }
	    });
      switch (what) {
	      case 0: //label
      		return label;
      		break;
		    case 1: //color
      		return color;
      		break;
        case 2: //tid
          return tid;
        case 3: //tid
          return mallet_ids_inluded;
          break;
        case 4: //TGif
          return "c2"; //("c"+toString(parseInt(el.tid.toString().slice(0,1))-1));
          break;
      }
	}

	$scope.setDiaryFocus = function(diary, pagenumber){

    $scope.focusDiary = diary;
    diary.path = "topicGroup-0.02-all"; // default;				
		diary.expand = true;

		if (diary.pages) {
			$scope.setFocusPage(diary, pagenumber-1); // already loaded, just set the page
		} else {
  		//otherwise, load the data from file, thengetTop() set the page
			$http.get("data/diaryDetail/"+diary.nid+".json").success(function(data){
				console.log("loaded diary " + diary.nid + " looking for page " + pagenumber);
				diary.pages = data[0].pages; // store the page data on the diary data object
				diary.page_no = data[0].page_no;
				$scope.setFocusPage(diary, pagenumber-1);
				
			})
		}
	}


  $scope.clickDiaryTile = function(d){

    d.expand = !d.expand; 
    $scope.pageExpand = false; 
    d.chart = getFilteredTopics(d.chart);
    $scope.focusDiary = d; 
//    d.pages[2].topics = getFilteredTopics(d.pages[2].topics);    
console.log($scope.focusDiary);

    $scope.mypath=$scope.getPath();

  }

  function getFilteredTopics(topics){

    filteredTopics = []; presentID = [];
      topics.forEach(function(el, i) {
        if (filteredTopics.length < 5 ) {
          if (presentID.indexOf($scope.getTopic(el[0],2)) == -1) {
            presentID.push($scope.getTopic(el[0],2));
            filteredTopics.push(el);
          } else {
            //console.log("Repeated , not added yet: "+el);  
            filteredTopics.forEach(function(val, key) {
              if ($scope.getTopic(el[0],2) == $scope.getTopic(val[0],2)) {
                filteredTopics[key][1] = parseFloat(filteredTopics[key][1])+ parseFloat(el[1]);
              }
            });
          }
        }
      });
    return filteredTopics;  
  }



	$scope.setFocusPage = function(diary, pageIndex){
		//console.log("setting page number " + pageIndex);

		if (diary.pages.length <= pageIndex || pageIndex < 0) return;

		diary.focusPageIndex = pageIndex;
		diary.focusPageIndex_norm = parseInt(pageIndex) + 1;
						
		// set the focused page for this diary 
		// to the value pageIndex - after checking the page 
    diary.filteredTopics = getFilteredTopics(diary.pages[pageIndex].topics);
	}


	$scope.imageGridClick = function(event, totalpages, diary, what) {
		// Configuration paramenters for each layout
		sq = 10; // square dimansions: n -> n x n in pixels
		ImgXLine = 120; // images (squares) per line

		// Mouse coordinates
		x = event.offsetX;
		y = event.offsetY;
		if (totalpages == ImgXLine) {
			xmax = totalpages;
			ymax = sq;
		} else {
			xmax = (totalpages%ImgXLine)*sq;
			ymax = (Math.ceil(totalpages/ImgXLine) - 1)*sq;
		}
 		my_page = (Math.ceil((y/sq)-1)*ImgXLine) + (Math.ceil((x/sq)%ImgXLine));
    my_flydiv = [];
 		my_flydiv["top"] = (Math.ceil((y/sq)-1)*ImgXLine);
 		my_flydiv["left"] = (Math.ceil((x/sq)%ImgXLine)) - 1;
    x_norm = ((x/sq) - parseInt(x/sq))*sq;
    y_norm = ((y/sq) - parseInt(y/sq))*sq;
    if ((x_norm < 1 || x_norm  > 9) || ((y_norm < 1 || y_norm  > 9)) || (x > xmax && y > ymax )) {
      output =   "(x_norm: "+x_norm+" | y_norm: "+y_norm+" | xmax: "+xmax+"| ymax:"+ymax+parseInt(x/sq)+","+parseInt(y/sq)+") Not square clicked"
    } else  {
      output = "(x_norm: "+x_norm+" | y_norm: "+y_norm+" | xmax: "+xmax+"| ymax:"+ymax+" | "+parseInt(x/sq)+","+parseInt(y/sq)+") Page clicked -> "+my_page+" | DiaryID: "+diary.nid;
    
      $scope.setDiaryFocus(diary, my_page);
      $scope.focusDiary.left = (parseInt(x/sq)*sq);
      $scope.focusDiary.top = (parseInt(y/sq)*sq);
    }
    console.log(output);
  }

  $scope.getPath = function() {
	    mypath = $location.path();
	        if (mypath == '') {
		        mypath = "topicGroup-0.02-all"; 
	        }
      return mypath;
  }

  $scope.dateDiff = function (y0,m0,d0,y1,m1,d1) {

    if (!y1 && !m1 && !d1) return 0; // = diay duration is 1 day (letter)
    
    if (!y1) y1 = y0
    if (!m1) m1 = "January"
    if (!d1) d1 = 1
    if (!m0) m0 = "January"
    if (!d0) d0 = 1
    var months = [ "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December" ];
    // month of difference:
    return Math.ceil((y1-y0)*12) + months.indexOf(m1)-months.indexOf(m0);
  }

  function toggleExpand() {
      var expanded = true;
      $('img').each(function() {
          if (!$(this).hasClass('expanded')) {
              expanded = false;
              return false;
          }
      });
      $('a[href$=".png"], a[href$=".jpg"], a[href$=".gif"], a[href$=".bmp"]').children('img').each(function() {
          if (expanded)
              $(this).removeClass('expanded');
          else
              $(this).addClass('expanded');
      });
  }
 
  /////////// READER
  $scope.getReaderContentsFromURL = function(path){
    readerContents = {};
    //console.log("path: "+path);
    pieces = path.split("/");
    readerContents.page_index = parseInt(pieces[2]);
    
    // CHECK if path is empty and do...

    //load diary metadata from diaries.json
    $scope.diaries.forEach(function(el) {
      if (parseInt(el.nid) == parseInt(pieces[1])) {
        readerContents.meta = el;
      }
    });

		//load diaryDetail
		$http.get("data/diaryDetail/"+pieces[1]+".json").success(function(data){
			//console.log("loaded diary " + pieces[1] + " looking for page number " + pieces[2]);
			readerContents.pages = data[0].pages; // store the page data on the diary data object
			readerContents.page_no = data[0].page_no;  				
		})
    return readerContents;
	}
   

  $scope.getTop = function(which_topic, how_choose) {
    toplist = [];
    // get the top json file
    $http.get("data/tops/"+which_topic).success(function(data){
      // choose a page conditions: randon, max score possible, next best scored
      // default  
      if (!how_choose) how_choose="random";
      if (which_topic.indexOf("TG") != -1) {item = 2;} else {item = 1;}
      // Randon
      switch (how_choose) {
        case "random":
          the_page_path = data[Math.floor(Math.random() * data.length) + 0 ][item]
          //window.location.assign("http://"+window.location.hostname+":8000/reader.html#"+the_page_path);
          window.location.assign("reader.html#"+the_page_path);
          break;
      }
		})
  }
  
}

////////////////////////////////////////////////////////////////////////////


function readerControl($scope, $http, $location){

  // LocalStoage
  // Using localStorage for the list of visited pages
  if (localStorage.getItem("journey") === null) {
    localStorage.setItem('journey', "");
  }
  $http.get("data/carousel.json").success(function(data){
    $scope.carousel = data;
    //console.log($scope.carousel["featured"]);
  });
      
  $http.get("data/diaries.json").success(function(data){
    $scope.diaries = data;
    // after diaries have loaded, we can get the reader contents
    
    // don't need this function -  now in setDiary and setPage
    //$scope.d = $scope.getReaderContentsFromURL($location.path());

    // once diaries.json is loaded, look at the path and load the diary detail & page


    if ($location.path()){ // if the path is set
      //console.log("init - getting page path: "+$location.path)
      newDiaryId = $location.path().split("/")[1];
      newPageIndex = $location.path().split("/")[2]; 
    } else {
      newDiaryId = "0"; //$scope.carousel["featured"][0]["diaryID"];
      newPageIndex = "0"; //$scope.carousel["featured"][0]["pageIndex"];    
    }
    // init
    $scope.setDiary(newDiaryId, newPageIndex);
    // getDivPosFromIndex(newPageIndex);
  });

  $http.get("data/topics.json").success(function(data){
    $scope.topics = data;
  });

  $http.get("data/vars.json").success(function(data){
    $scope.vars = data;
  });

  $scope.checkPath = function() {
    if ($location.path().length>2){ return true; }
    else { return false; }
  }

  $scope.getTop = function(which_topic, how_choose) {
    toplist = [];
    // get the top json file
    $http.get("data/tops/"+which_topic).success(function(data){
      // choose page conditions: randon, max score possible, next best scored
      // default  
      if (!how_choose) how_choose="random";
      if (which_topic.indexOf("TG") !=-1) {item = 2;} else {item = 1;}
      // Randon
      switch (how_choose) {
        case "random":
          the_page_path = data[Math.floor(Math.random() * data.length) + 0 ][item]
          // set the ID of the new diary
          newDiaryId = the_page_path.split("/")[1];
          newPageIndex = parseInt(the_page_path.split("/")[2]) - 1; // This "-1" corrects the getTop !
          // then call the new diary load          
          $scope.setDiary(newDiaryId, newPageIndex);
          break;
      }     
    })
  }

  $scope.nextPage = function(){
    if ($scope.d.page_index  < $scope.d.pages.length-1) {
      $scope.d.page_index++;
      $scope.setPage($scope.d.page_index);
      //$scope.getDivPosFromIndex($scope.d.page_index);
    }
  }

   $scope.prevPage = function(){
    if ($scope.d.page_index  > 0) {
      $scope.d.page_index--;
      $scope.setPage($scope.d.page_index);
      //$scope.getDivPosFromIndex($scope.d.page_index);
    }
  }

  $scope.setDiary = function(diaryID, pageIndex){

    $http.get("data/diaryDetail/"+diaryID+".json").success(function(data){
      console.log("setDiary - loaded diary " + diaryID + " looking for page number " + pageIndex);

      // loaded, store data on the scope
      $scope.d = data[0]; 

      // now find matching metadata
      $scope.diaries.forEach(function(el) {
        if (parseInt(el.nid) == diaryID) {
          $scope.d.meta = el;
          console.log(" found metadata for diary " + diaryID);
        }
      });

      // $scope.d.top = top;
      // $scope.d.left = left;
      $scope.d.default = false;
      console.log($scope.d);

      // once loaded the diary data, set the current page index
      $scope.setPage(pageIndex);  
      // set the path to match the current model
    })

  }

  $scope.setPage = function(idx){
    // check for index in range
    console.log("page number " + idx);
    $scope.d.page_index = idx;
    $scope.d.page_index_norm = parseInt(idx) + 1;
    $scope.currentPage = $scope.d.pages[idx]; // set current page on scope
    console.log("current page: "+$scope.currentPage.id);

    var divpos = $scope.getDivPosFromIndex(idx); // get the div pos object
    $scope.d.top = divpos.top; // set on the scope
    $scope.d.left = divpos.left;

    // now set the path
    $location.path("/"+$scope.d.meta.nid+"/"+idx); 

    // now process the topics data for this page for display - eg merge topics, assign labels?
    filteredTopics = []; presentID = [];
    $scope.currentPage.topics.forEach(function(el, i) {
      if (filteredTopics.length < 5 ) {
        if (presentID.indexOf($scope.getTopic(el[0],2)) == -1) {
          presentID.push($scope.getTopic(el[0],2));
          filteredTopics.push(el);
        } else {
          console.log("Repeated , not added yet: "+el);  
          filteredTopics.forEach(function(val, key) {
            if ($scope.getTopic(el[0],2) == $scope.getTopic(val[0],2)) {
              filteredTopics[key][1] = parseFloat(filteredTopics[key][1])+ parseFloat(el[1]);
            }
          });
        }
      }
    });
    $scope.currentPage.filteredTopics = filteredTopics;
  //$scope.storage("/"+$scope.d.meta.nid+"/"+idx+" ["+filteredTopics+"]","set");
  
  // Set flydiv left and top
  		//x = (totalpages%ImgXLine)*sq;
			//y = (Math.ceil(totalpages/ImgXLine) - 1)*sq;
  

}

  $scope.storage = function(action) {
    //! Initially action is not set

    //switch (action): 
      //...
      // storing a visit
      var journey = localStorage.getItem('journey') + " >> " + "/"+$scope.d.meta.nid+"/"+$scope.d.page_index;
      localStorage.setItem('journey', journey);

    console.log("localscore: "+localStorage.getItem("journey"));
  }

  $scope.getTopic = function (mallet_id, what) {
    label = "unknown";color = "red";
    $scope.topics.forEach(function(el){
      if (el.mallet_ids_inluded.indexOf(mallet_id) != -1) {
        label = el.label;
        color = $scope.vars["topic_groups"][parseInt(el.tid.toString().slice(0,1))-1]["color"];
        mallet_ids_inluded = el.mallet_ids_inluded;
        tid = el.tid;
      }
    });
    switch (what) {
      case 0: //label
        return label;
        break;
      case 1: //color
        return color;
        break;
      case 2: //tid
        return tid;
        break;
      case 3: //tid
        return mallet_ids_inluded;
        break;
      case 4: //TGif
        return "c2"; //("c"+toString(parseInt(el.tid.toString().slice(0,1))-1));
        break;
    }
  }

	$scope.imageGridClick = function(event, totalpages, diary, what) {

    // this function takes click event and calculates page index
  // then call getDivPosFromIndex

		// Configuration paramenters for each layout
		sq = 10; // square dimansions: n -> n x n in pixels
		ImgXLine = 120; // images (squares) per line

		// Mouse coordinates
		x = event.offsetX;
		y = event.offsetY;
		if (totalpages == ImgXLine) {
			xmax = totalpages;
			ymax = sq;
		} else {
			xmax = (totalpages%ImgXLine)*sq;
			ymax = (Math.ceil(totalpages/ImgXLine) - 1)*sq;
		}

 		my_page = (Math.ceil((y/sq)-1)*ImgXLine) + (Math.ceil((x/sq)%ImgXLine)) - 1;
    $scope.setPage(my_page);
  }

  $scope.getDivPosFromIndex = function(idx){
    // calculates top and left of the page 

    sq = 10; // square dimansions: n -> n x n in pixels
    ImgXLine = 120; // images (squares) per line

    myleft = (idx*sq)%(ImgXLine*sq);
    mytop = Math.floor(idx/ImgXLine)*sq;

    console.log('left ' + myleft);
    return {'left':myleft, 'top':mytop};

  }

}


