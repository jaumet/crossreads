
(function(){
	var app = angular.module('diaries', []);

	app.controller('DiariesController', function(){
		this.diary = mydiary;

	
	});

	var mydiary = 	
	{
		"id":2,
		"diary_id":"2",
		"page_no":"2",
		"title":"title",
		"date":"1914/1/18",
		"location":"Gallipolly",
		"topics":"peace",
		"transcript":"transcript",
		"cover":"a3368001h.jpg"
	};


}());
