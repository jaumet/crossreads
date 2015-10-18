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
				label = "Top topic in this diary: "+el.label;
			}
		});
		return label;
	}

	//$scope.orderFields = ["start_date[0].start_year","author"]

	$scope.setDiaryFocus = function(diary){
		$scope.focusDiary = diary;
		$http.get("data/diaryDetail/"+diary.nid+".json").success(function(data){
			$scope.focusDiary.pages = data;
		})
	}

	$scope.addOnClick = function(event, totalpages, diaryID) {
		// Configuration paramenters for each layout (needs to be in  the top)
		sq = 10; // n; n x n in pixels
		ImgXLine = 120;

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
   		//console.log(x, y, xmax, ymax, my_page, sq, ImgXLine, totalpages);

		return checkCoord(x, y, xmax, ymax, my_page, diaryID)
	}

    function checkCoord(x, y, xmax, ymax, my_page, diaryID) {
		//console.log("x: "+x+" - xmax: "+xmax+" | y: "+y+" - ymax: "+ymax);
        x_norm = ((x/sq) - parseInt(x/sq))*sq;
        y_norm = ((y/sq) - parseInt(y/sq))*sq;
        if ((x_norm < 1 || x_norm  > 9) || ((y_norm < 1 || y_norm  > 9)) || (x > xmax && y > ymax )) {
          output =   "("+parseInt(x/sq)+","+parseInt(y/sq)+") Not square clicked"

        } else  {
          output = "("+parseInt(x/sq)+","+parseInt(y/sq)+") Page clicked -> "+my_page+" | DiaryID: "+diaryID;
          // Show div on top
          //$("#square").css("left",parseInt(3*((x/6)+1))).css("top",parseInt(3*((y/6)+1)));
          // FIXME Mitchell? How we do this the best way? (ng-bind?)
          window.location.href = '/pages.html?d=122345';
        }
        console.log(output);
        return output;
	}

	$scope.pageClick = function(diaryID, pageID) {
		// get text:
    $http.get("data/3-Transcriptions/"+diaryID+"/"+pageID+".json").success(function(data){
      mytext = data;
    })
		// return html
    return mytext;

	}

}
