var TOPICNAMES = ["Personal", "War", "Military life", "Traveling", "The accidental tourist"];

var TOPICS = [
	{
	"code":"0-0",
	"topic":"-",
	"topicNo":100,
	"words":""
	},
	{
	"code":"1-1",
	"topic":"Weather",
	"topicNo":1,
	"words":"cold day night weather rain morning snow heavy wind wet fine sunday warm afternoon today quiet early raining days mud"
	},
	{
	"code":"1-2",
	"topic":"Colors of life",
	"topicNo":15,
	"words":"white sun great red blue long sea beautiful black high sight sky hills grey dark clouds bright green dust huge"
	},
	{
	"code":"1-3",
	"topic":"Food",
	"topicNo":10,
	"words":"tea bread dinner biscuits breakfast good coffee butter eggs food rations jam beef plenty issued meal bully canteen tin beer"
	},
/*
	{
	"code":"1-3",
	"topic":"Food",
	"topicNo":28,
	"words":"tea bread dinner biscuits breakfast good coffee butter eggs food rations jam beef plenty issued meal bully canteen tin beer"
	},
*/
	{
	"code":"1-4",
	"topic":"Personal care & clothes",
	"topicNo":18,
	"words":"clothes boots clean pair men issue issued bath wear clothing socks wearing water hot kit baths put change blankets returned"
	},
	{
	"code":"1-5",
	"topic":"Letters, family",
	"topicNo":17,
	"words":"letter letters dear received love home time write dont news france good mother send ago hope days heard long back"
	},
	{
	"code":"1-6",
	"topic":"Poetry & spirit",
	"topicNo":11,
	"words":"land world god man thy love hearts past face mother deep glory children tears gate procession beneath sacred dear loved"
	},
	{
	"code":"1-7",
	"topic":"Family & Oz",
	"topicNo":3,
	"words":"pte mrs anzac father c/e mother sydney laborer pres n.s.w r.c miss australia batt wife coy kin sgt smith c/o"
	},
	{
	"code":"1-8",
	"topic":"In French",
	"topicNo":22,
	"words":"les pour vous sans qui dans madelon nous une c?est des ils pas tout moi tous son ceux sur votre"
	},
	{
	"code":"2-1",
	"topic": "Combat",
	"topicNo":4,
	"words":"shells shell trenches guns fire fritz night line trench gun men big close bombardment firing quiet machine artillery front heavy"
	},
	{
	"code":"2-2",
	"topic":"Front line",
	"topicNo":6,
	"words":"line morning night front enemy attack guns back trenches artillery left casualties wounded trench position heavy prisoners moved german boys"
	},
	{
	"code":"2-3",
	"topic":"Health",
	"topicNo":26,
	"words":"feet water day head feeling poor hospital bad eyes men sore doctor face feel bed sick body felt long awful"
	},
	{
	"code":"2-4",
	"topic":"Health",
	"topicNo":24,
	"words":"wounded killed stretcher man hospital back poor chap left men dead bearers died leg head post station dressing hit brought"
	},
	{
	"code":"2-5",
	"topic":"Air",
	"topicNo":9,
	"words":"planes air aeroplanes bombs machine dropped guns fritz plane night aeroplane great enemy flying shells lines machines bomb brought flew"
	},
	{
	"code":"2-6",
	"topic":"Front line",
	"topicNo":2,
	"words":"men fire guns gun light enemy front position forward firing machine smoke dark minutes immediately rear sound yards signal roar"
	},
	{
	"code":"2-7",
	"topic":"Context",
	"topicNo":14,
	"words":"german prisoners oct germans english news turkish work food germany officers french british war told england september commandant armistice sept"
	},
	{
	"code":"3-1",
	"topic":"Politics & context",
	"topicNo":16,
	"words":"men war australian great made british army life troops france general australians soldiers military years australia officers fighting battle death"
	},
	{
	"code":"3-2",
	"topic":"Parades & Marches",
	"topicNo":12,
	"words":"parade men general afternoon battalion good morning work marched today day officers band ground march drill company order inspected lunch"
	},
	{
	"code":"3-3",
	"topic":"Turkey?",
	"topicNo":19,
	"words":"turks trenches beach water turkish men good hill sea enemy turk post anzac stand round abdul artillery gully lying dead"
	},
	{
	"code":"3-4",
	"topic":"General",
	"topicNo":5,
	"words":"para pte officer orders part coy charge field order battalion col battn a.i.f hours duty sentence absent capt div lieut"
	},
	{
	"code":"3-5",
	"topic":"Sports",
	"topicNo":8,
	"words":"played won football match sports game afternoon team cricket beat playing great officers race coy boxing day prize competition nil"
	},
	{
	"code":"4-1",
	"topic":"Roads & railways",
	"topicNo":27,
	"words":"train left arrived station camp marched town leave miles motor night march p.m passed amiens a.m railway hours morning city"
	},
	{
	"code":"4-2",
	"topic":"Over the sea",
	"topicNo":7,
	"words":"ship boat sea port board harbour left ships passed boats aboard ashore troops wharf island bay sydney morning water arrived"
	},
	{
	"code":"4-3",
	"topic":"by Land",
	"topicNo":29,
	"words":"train arrived large engine trucks boys number line back station made depot run left camp railway time hut started siding"
	},
	{
	"code":"4-4",
	"topic":"Sea life",
	"topicNo":25,
	"words":"sea day deck ship boat hot morning weather passed mess night calm rough good board land sight afternoon drill water"
	},
	{
	"code":"4-5",
	"topic":"Middle East",
	"topicNo":20	,
	"words":"horses miles jerusalem road wadi turks valley hills water jordan left hill great camped turkish village camp moved made brigade"
	},
	{
	"code":"5-1",
	"topic":"City life",
	"topicNo":13,
	"words":"church place fine inside beautiful town round stone cathedral built walls building side places large houses high city small ancient"
	},
	{
	"code":"5-2", 
	"topic":"Egypt",
	"topicNo":21,
	"words":"cairo native natives women city egypt streets round people pyramids egyptian white children street tram soldiers left interesting man large"
	},
	{
	"code":"5-3",
	"topic":"UK",
	"topicNo":23,
	"words":"london back tea train met park left breakfast cross hotel arrived victoria home dinner place caught lunch walked office bed"
	},
	{
	"code":"5-4",
	"topic":"France",
	"topicNo":0,
	"words":"hotel paris walked round place french streets girls good people opera returned dinner english shops full lunch back officers fine"
	}
];
