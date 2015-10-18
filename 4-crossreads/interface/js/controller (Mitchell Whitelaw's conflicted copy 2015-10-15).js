function listControl($scope,$http){
	//console.log("hello world");

	$http.get("data/diaries.json").success(function(data){
		$scope.diaries = data;
	});

	//$scope.orderFields = ["start_date[0].start_year","author"]

	$scope.setDiaryFocus = function(diary){
		$scope.focusDiary = diary;

		$http.get("data/diaryDetail/"+diary.id+".json").success(function(data){

			$scope.focusDiary.pages = data;

		})


	}
	


}



