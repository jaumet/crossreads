
(function(){
	var app = angular.module('library', []);

	app.controller('DiariesController', function(){
		this.diary = DATA;
  });

  function randomTopic() {
    mytopics = ["A", "B", "C"];
    return mytopics[Math.floor(Math.random()*mytopics.length)];
  }

}());
