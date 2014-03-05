/////////////////////////////////
//		     AREA
//	  CONFIGURATION FILE
//////////////////////// [Canberra, 2013-14 by Jaume@Nualart.cat]
//
// Three variable need to be defined:
// FIELDS -> This variable is only used by AREA. 
//	It defines the machine name the human name and whether each paramater 
//	is eligible for filtering.
// ROLE DEFINITIONS:
// 		"area" -> only as AREA field
// 
///////////////////////////////////////////////////////////////////
// AREA CONFIGURATION
//
	var MAX_DISTINC = 500;
	var AREAX = 800;
	var AREAY = 600;
	var COLORS_APPROACH = "gradient"; // fix, random, gradient
	var PARAM1 = "year";
	var PARAM2 = "format";
	var AREA_TITLE = "";

///////////////////////////////////////////////////////////////////
// FIELDS CONFIGURATION:
//
// -> the index are the machine-names for each field (only alphanumeric characters)/ Also used in var DATA
// -> human : human name for the field
// -> areafilter: 0 = no eligible for filtering | 1 = eligible for filtering
// -> role: "hide" or "show" ====> NOT IMPLEMENTED

var FIELDS = [
	{
		"id": 
			{ human: "My ID", areafilter: "0", role:"table"},
		"title": 
			{ human: "My Title", areafilter: "1", role:"table-area"},
		"year": 
			{ human: "Year", areafilter: "1", role:"table-area"},
		"lang": 
			{ human: "Language", areafilter: "1", role:"table-area"},
		"format":
			{ human: "Format", areafilter: "1", role:"hide"},
		"topic":
			{ human: "Topic", areafilter: "1", role:"table-area"},
		"publication": 
			{ human: "Publication", areafilter: "1", role:"table-area"},
		"numImg": 
			{ human: "number of images", areafilter: "1", role:"table-area"}
	}
];

