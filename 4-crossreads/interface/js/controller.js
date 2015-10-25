function listControl($scope,$http){
	//console.log("hello world");

	$http.get("data/diaries.json").success(function(data){
		$scope.diaries = data;
	});

	$http.get("data/topics.json").success(function(data){
		$scope.topics = data;
	});

	$scope.getTopicLabel = function (mallet_id) {
		label = "unknown";
		$scope.topics.forEach(function(el){
			if (el.mallet_ids_inluded.indexOf(mallet_id) != -1) {
				label = el.label;
			}
		});
		return label;
	}

	//$scope.orderFields = ["start_date[0].start_year","author"]

	$scope.setDiaryFocus = function(diary, pagenumber){
		$scope.focusDiary = diary;

		diary.expand = true;

		if (diary.pages) {
			$scope.setFocusPage(diary, pagenumber-1); // already loaded, just set the page
		 } 
		 else 
		 {

		//otherwise, load the data from file, then set the page

			$http.get("data/diaryDetail/"+diary.nid+".json").success(function(data){
				console.log("loaded diary " + diary.nid + " looking for page " + pagenumber);

				diary.pages = data[0].pages; // store the page data on the diary data object
				diary.page_no = data[0].page_no;
				
				$scope.setFocusPage(diary, pagenumber-1);

				//console.log(data); // NB diary json is a one element array!!!!
				
				//diary.focusPage = data[0].pages[pagenumber-1];

				//console.log($scope.focusDiary.nid);
				//console.log($scope.focusPage.id);

				
			})
		}
	}


	$scope.setFocusPage = function(diary, pageIndex){
		console.log("setting page number " + pageIndex);

		if (diary.pages.length <= pageIndex || pageIndex < 0) return;

		diary.focusPageIndex = pageIndex;
		
		// set the focused page for this diary 
		// to the value pageIndex - after checking the page 

	}

	$scope.addOnClick = function(event, totalpages, diary) {
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
 		my_page = (Math.ceil((y/sq)-1)*ImgXLine) + (Math.ceil((x/sq)%ImgXLine))
 		console.log(x, y, xmax, ymax, my_page, sq, ImgXLine, totalpages);
 		
    x_norm = ((x/sq) - parseInt(x/sq))*sq;
    y_norm = ((y/sq) - parseInt(y/sq))*sq;
    if ((x_norm < 1 || x_norm  > 9) || ((y_norm < 1 || y_norm  > 9)) || (x > xmax && y > ymax )) {
      output =   "("+parseInt(x/sq)+","+parseInt(y/sq)+") Not square clicked"

    } else  {
      output = "("+parseInt(x/sq)+","+parseInt(y/sq)+") Page clicked -> "+my_page+" | DiaryID: "+diary.nid;
      // Show div on top
      //$("#square").css("left",parseInt(3*((x/6)+1))).css("top",parseInt(3*((y/6)+1)));

    }
    console.log(output);

    $scope.setDiaryFocus(diary, my_page);

	}



	$scope.pageClick = function(diaryID, pageID) {
		// get text:
    $http.get("data/3-Transcriptions/"+diaryID+"/"+pageID+".json").success(function(data){
      mytext = data;
    })
    return mytext;

	}

}
