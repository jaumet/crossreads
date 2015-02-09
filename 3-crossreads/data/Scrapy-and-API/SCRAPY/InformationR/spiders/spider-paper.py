import re
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from InformationR.items import InformationrPaper

class InformationResearch(BaseSpider):
	'''
	This class gets a paper from IR and scraps several metadata fields from it.
	'''
	name = "paper"
	allowed_domains = ["informationr.net/"]
	start_urls = [
		"http://www.informationr.net/ir/19-3/paper630.html", 
    "http://www.informationr.net/ir/19-3/paper631.html", 
    "http://www.informationr.net/ir/19-3/paper632.html", 
    "http://www.informationr.net/ir/19-3/paper633.html", 
    "http://www.informationr.net/ir/19-3/paper634.html", 
    "http://www.informationr.net/ir/19-3/paper635.html", 
    "http://www.informationr.net/ir/19-3/paper636.html", 
    "http://www.informationr.net/ir/19-3/paper637.html", 
    "http://www.informationr.net/ir/19-3/paper638.html", 
    "http://www.informationr.net/ir/19-3/paper639.html", 
    "http://www.informationr.net/ir/19-3/paper640.html"
	]
	
	# List for the new issues: 18-3, 18-4, 19-1, 19-2
	start_urlsOLD = [
		"http://informationr.net/ir/18-3/paper583.html",
		"http://informationr.net/ir/18-3/paper584.html",
		"http://informationr.net/ir/18-3/paper585.html",
		"http://informationr.net/ir/18-3/paper586.html",
		"http://informationr.net/ir/18-3/paper587.html",
		"http://informationr.net/ir/18-3/paper588.html",
		"http://informationr.net/ir/18-3/paper589.html",
		"http://informationr.net/ir/18-3/paper590.html",
		"http://informationr.net/ir/18-4/paper591.html",
		"http://informationr.net/ir/18-4/paper592.html",
		"http://informationr.net/ir/18-4/paper593.html",
		"http://informationr.net/ir/18-4/paper594.html",
		"http://informationr.net/ir/18-4/paper595.html",
		"http://informationr.net/ir/18-4/paper596.html",
		"http://informationr.net/ir/18-4/paper597.html",
		"http://informationr.net/ir/18-4/paper598.html",
		"http://informationr.net/ir/18-4/paper599.html",
		"http://informationr.net/ir/18-4/paper600.html",
		"http://informationr.net/ir/18-4/paper601.html",
		"http://informationr.net/ir/19-1/paper602.html",
		"http://informationr.net/ir/19-1/paper603.html",
		"http://informationr.net/ir/19-1/paper604.html",
		"http://informationr.net/ir/19-1/paper605.html",
		"http://informationr.net/ir/19-1/paper606.html",
		"http://informationr.net/ir/19-1/paper607.html",
		"http://informationr.net/ir/19-1/paper608.html",
		"http://informationr.net/ir/19-1/paper609.html",
		"http://informationr.net/ir/19-1/paper610.html",
		"http://informationr.net/ir/19-1/paper611.html",
		"http://informationr.net/ir/19-2/paper612.html",
		"http://informationr.net/ir/19-2/paper619.html",
		"http://informationr.net/ir/19-2/paper621.html",
		"http://informationr.net/ir/19-2/paper620.html",
		"http://informationr.net/ir/19-2/paper622.html",
		"http://informationr.net/ir/19-2/paper623.html",
		"http://informationr.net/ir/19-2/paper625.html",
		"http://informationr.net/ir/19-2/paper624.html",
		"http://informationr.net/ir/19-2/paper613.html",
		"http://informationr.net/ir/19-2/paper614.html",
		"http://informationr.net/ir/19-2/paper615.html",
		"http://informationr.net/ir/19-2/paper616.html",
		"http://informationr.net/ir/19-2/paper617.html",
		"http://informationr.net/ir/19-2/paper618.html"
	]

	start_urlsOLD1 = [
		"http://informationr.net/ir/17-1/paper507.html",
		"http://informationr.net/ir/17-1/paper508.html",
		"http://informationr.net/ir/17-1/paper509.html",
		"http://informationr.net/ir/17-1/paper510.html",
		"http://informationr.net/ir/17-1/paper511.html",
		"http://informationr.net/ir/17-1/paper512.html",
		"http://informationr.net/ir/17-1/paper513.html",
		"http://informationr.net/ir/16-1/paper464.html",
		"http://informationr.net/ir/16-1/paper465.html",
		"http://informationr.net/ir/16-1/paper466.html",
		"http://informationr.net/ir/16-1/paper467.html",
		"http://informationr.net/ir/16-1/paper469.html",
		"http://informationr.net/ir/16-2/paper473.html",
		"http://informationr.net/ir/16-2/paper474.html",
		"http://informationr.net/ir/16-2/paper475.html",
		"http://informationr.net/ir/16-2/paper476.html",
		"http://informationr.net/ir/16-2/paper477.html",
		"http://informationr.net/ir/16-2/paper478.html",
		"http://informationr.net/ir/16-2/paper479.html",
		"http://informationr.net/ir/16-2/paper480.html",
		"http://informationr.net/ir/18-2/paper574.html",
		"http://informationr.net/ir/18-2/paper575.html",
		"http://informationr.net/ir/18-2/paper576.html",
		"http://informationr.net/ir/18-2/paper577.html",
		"http://informationr.net/ir/18-2/paper578.html",
		"http://informationr.net/ir/18-2/paper579.html",
		"http://informationr.net/ir/18-2/paper580.html",
		"http://informationr.net/ir/18-2/paper581.html",
		"http://informationr.net/ir/18-2/paper582.html",
		"http://informationr.net/ir/18-1/paper555.html",
		"http://informationr.net/ir/18-1/paper558.html",
		"http://informationr.net/ir/18-1/paper559.html",
		"http://informationr.net/ir/18-1/paper563.html",
		"http://informationr.net/ir/18-1/paper566.html",
		"http://informationr.net/ir/18-1/paper568.html",
		"http://informationr.net/ir/18-1/paper569.html",
		"http://informationr.net/ir/18-1/paper570.html",
		"http://informationr.net/ir/18-1/paper572.html",
		"http://informationr.net/ir/18-1/paper571.html",
		"http://informationr.net/ir/18-1/paper556.html",
		"http://informationr.net/ir/17-2/paper514.html",
		"http://informationr.net/ir/17-2/paper515.html",
		"http://informationr.net/ir/17-2/paper516.html",
		"http://informationr.net/ir/17-2/paper517.html",
		"http://informationr.net/ir/17-2/paper518.html",
		"http://informationr.net/ir/17-2/paper519.html",
		"http://informationr.net/ir/17-2/paper521.html",
		"http://informationr.net/ir/17-2/paper520.html",
		"http://informationr.net/ir/18-1/paper557.html",
		"http://informationr.net/ir/18-1/paper560.html",
		"http://informationr.net/ir/18-1/paper561.html",
		"http://informationr.net/ir/18-1/paper562.html",
		"http://informationr.net/ir/18-1/paper564.html",
		"http://informationr.net/ir/18-1/paper565.html",
		"http://informationr.net/ir/18-1/paper567.html",
		"http://informationr.net/ir/18-1/paper573.html",
		"http://informationr.net/ir/17-4/paper541.html",
		"http://informationr.net/ir/17-4/paper539.html",
		"http://informationr.net/ir/17-4/paper544.html",
		"http://informationr.net/ir/17-4/paper550.html",
		"http://informationr.net/ir/17-4/paper553.html",
		"http://informationr.net/ir/17-4/paper554.html",
		"http://informationr.net/ir/17-4/paper534.html",
		"http://informationr.net/ir/17-4/paper535.html",
		"http://informationr.net/ir/17-4/paper536.html",
		"http://informationr.net/ir/17-3/paper522.html",
		"http://informationr.net/ir/17-3/paper523.html",
		"http://informationr.net/ir/17-3/paper524.html",
		"http://informationr.net/ir/17-3/paper525.html",
		"http://informationr.net/ir/17-3/paper526.html",
		"http://informationr.net/ir/17-3/paper527.html",
		"http://informationr.net/ir/17-3/paper528.html",
		"http://informationr.net/ir/17-3/paper530.html",
		"http://informationr.net/ir/17-4/paper537.html",
		"http://informationr.net/ir/17-4/paper538.html",
		"http://informationr.net/ir/17-4/paper540.html",
		"http://informationr.net/ir/17-4/paper542.html",
		"http://informationr.net/ir/17-4/paper543.html",
		"http://informationr.net/ir/17-4/paper545.html",
		"http://informationr.net/ir/17-4/paper546.html",
		"http://informationr.net/ir/17-4/paper547.html",
		"http://informationr.net/ir/17-4/paper548.html",
		"http://informationr.net/ir/17-4/paper549.html",
		"http://informationr.net/ir/17-4/paper552.html",
		"http://informationr.net/ir/17-3/paper531.html",
		"http://informationr.net/ir/17-3/paper532.html",
		"http://informationr.net/ir/17-3/paper533.html",
		"http://informationr.net/ir/17-3/paper529.html",
		"http://informationr.net/ir/17-4/paper551.html",
		"http://informationr.net/ir/16-3/paper485.html",
		"http://informationr.net/ir/16-3/paper488.html",
		"http://informationr.net/ir/16-3/paper486.html",
		"http://informationr.net/ir/16-3/paper487.html",
		"http://informationr.net/ir/16-3/paper494.html",
		"http://informationr.net/ir/16-3/paper492.html",
		"http://informationr.net/ir/16-3/paper483.html",
		"http://informationr.net/ir/16-3/paper489.html",
		"http://informationr.net/ir/16-3/paper490.html",
		"http://informationr.net/ir/16-3/paper491.html",
		"http://informationr.net/ir/16-3/paper481.html",
		"http://informationr.net/ir/16-3/paper482.html",
		"http://informationr.net/ir/16-3/paper484.html",
		"http://informationr.net/ir/16-3/paper493.html",
		"http://informationr.net/ir/15-1/paper423.html",
		"http://informationr.net/ir/15-1/paper424.html",
		"http://informationr.net/ir/15-1/paper425.html",
		"http://informationr.net/ir/15-1/paper426.html",
		"http://informationr.net/ir/15-1/paper427.html",
		"http://informationr.net/ir/15-2/paper428.html",
		"http://informationr.net/ir/15-2/paper429.html",
		"http://informationr.net/ir/15-2/paper430.html",
		"http://informationr.net/ir/15-2/paper431.html",
		"http://informationr.net/ir/15-2/paper432.html",
		"http://informationr.net/ir/15-3/paper433.html",
		"http://informationr.net/ir/15-3/paper434.html",
		"http://informationr.net/ir/15-3/paper435.html",
		"http://informationr.net/ir/15-3/paper436.html",
		"http://informationr.net/ir/15-3/paper437.html",
		"http://informationr.net/ir/14-2/paper396.html",
		"http://informationr.net/ir/14-2/paper397.html",
		"http://informationr.net/ir/14-2/paper398.html",
		"http://informationr.net/ir/14-2/paper399.html",
		"http://informationr.net/ir/14-2/paper400.html",
		"http://informationr.net/ir/14-2/paper401.html",
		"http://informationr.net/ir/14-2/paper402.html",
		"http://informationr.net/ir/14-2/paper403.html",
		"http://informationr.net/ir/14-2/paper404.html",
		"http://informationr.net/ir/14-1/paper388.html",
		"http://informationr.net/ir/14-1/paper389.html",
		"http://informationr.net/ir/14-1/paper390.html",
		"http://informationr.net/ir/14-1/paper391.html",
		"http://informationr.net/ir/14-1/paper392.html",
		"http://informationr.net/ir/14-1/paper393.html",
		"http://informationr.net/ir/14-1/paper394.html",
		"http://informationr.net/ir/14-1/paper395.html",
		"http://informationr.net/ir/16-4/paper496.html",
		"http://informationr.net/ir/16-4/paper497.html",
		"http://informationr.net/ir/16-4/paper498.html",
		"http://informationr.net/ir/16-4/paper499.html",
		"http://informationr.net/ir/16-4/paper500.html",
		"http://informationr.net/ir/16-4/paper501.html",
		"http://informationr.net/ir/16-4/paper502.html",
		"http://informationr.net/ir/16-4/paper503.html",
		"http://informationr.net/ir/16-4/paper504.html",
		"http://informationr.net/ir/16-4/paper505.html",
		"http://informationr.net/ir/16-4/paper506.html",
		"http://informationr.net/ir/15-4/paper451.html",
		"http://informationr.net/ir/15-4/paper442.html",
		"http://informationr.net/ir/15-4/paper449.html",
		"http://informationr.net/ir/15-4/paper447.html",
		"http://informationr.net/ir/15-4/paper448.html",
		"http://informationr.net/ir/15-4/paper453.html",
		"http://informationr.net/ir/15-4/paper445.html",
		"http://informationr.net/ir/15-4/paper443.html",
		"http://informationr.net/ir/15-4/paper441.html",
		"http://informationr.net/ir/15-4/paper446.html",
		"http://informationr.net/ir/15-4/paper452.html",
		"http://informationr.net/ir/15-4/paper440.html",
		"http://informationr.net/ir/15-4/paper444.html",
		"http://informationr.net/ir/15-4/paper454.html",
		"http://informationr.net/ir/15-4/paper450.html",
		"http://informationr.net/ir/15-4/paper438.html",
		"http://informationr.net/ir/15-4/paper439.html",
		"http://informationr.net/ir/14-3/paper405.html",
		"http://informationr.net/ir/14-3/paper406.html",
		"http://informationr.net/ir/14-3/paper408.html",
		"http://informationr.net/ir/14-3/paper409.html",
		"http://informationr.net/ir/14-3/paper410.html",
		"http://informationr.net/ir/14-3/paper411.html",
		"http://informationr.net/ir/14-3/paper412.html",
		"http://informationr.net/ir/14-3/paper407.html",
		"http://informationr.net/ir/14-4/paper413.html",
		"http://informationr.net/ir/14-4/paper414.html",
		"http://informationr.net/ir/14-4/paper415.html",
		"http://informationr.net/ir/14-4/paper416.html",
		"http://informationr.net/ir/14-4/paper417.html",
		"http://informationr.net/ir/14-4/paper418.html",
		"http://informationr.net/ir/14-4/paper419.html",
		"http://informationr.net/ir/14-4/paper420.html",
		"http://informationr.net/ir/14-4/paper421.html",
		"http://informationr.net/ir/14-4/paper422.html",
		"http://informationr.net/ir/13-1/paper331.html",
		"http://informationr.net/ir/13-1/paper332.html",
		"http://informationr.net/ir/13-1/paper333.html",
		"http://informationr.net/ir/13-1/paper334.html",
		"http://informationr.net/ir/13-1/paper336.html",
		"http://informationr.net/ir/13-1/paper337.html",
		"http://informationr.net/ir/13-1/paper339.html",
		"http://informationr.net/ir/13-1/paper335.html",
		"http://informationr.net/ir/13-1/paper338.html",
		"http://informationr.net/ir/13-2/paper340.html",
		"http://informationr.net/ir/13-2/paper341.html",
		"http://informationr.net/ir/13-2/paper342.html",
		"http://informationr.net/ir/13-2/paper343.html",
		"http://informationr.net/ir/13-2/paper344.html",
		"http://informationr.net/ir/13-2/paper345.html",
		"http://informationr.net/ir/13-2/paper346.html",
		"http://informationr.net/ir/13-4/paper383.html",
		"http://informationr.net/ir/13-4/paper384.html",
		"http://informationr.net/ir/13-4/paper385.html",
		"http://informationr.net/ir/13-4/paper386.html",
		"http://informationr.net/ir/13-4/paper387.html",
		"http://informationr.net/ir/13-3/paper347.html",
		"http://informationr.net/ir/13-3/paper348.html",
		"http://informationr.net/ir/13-3/paper349.html",
		"http://informationr.net/ir/13-3/paper350.html",
		"http://informationr.net/ir/13-3/paper351.html",
		"http://informationr.net/ir/13-3/paper352.html",
		"http://informationr.net/ir/13-3/paper353.html",
		"http://informationr.net/ir/12-1/paper286.html",
		"http://informationr.net/ir/12-1/paper287.html",
		"http://informationr.net/ir/12-1/paper274.html",
		"http://informationr.net/ir/12-1/paper275.html",
		"http://informationr.net/ir/12-1/paper276.html",
		"http://informationr.net/ir/12-1/paper277.html",
		"http://informationr.net/ir/12-1/paper278.html",
		"http://informationr.net/ir/12-1/paper279.html",
		"http://informationr.net/ir/12-1/paper280.html",
		"http://informationr.net/ir/12-1/paper281.html",
		"http://informationr.net/ir/12-1/paper282.html",
		"http://informationr.net/ir/12-1/paper283.html",
		"http://informationr.net/ir/12-1/paper288.html",
		"http://informationr.net/ir/12-1/paper284.html",
		"http://informationr.net/ir/12-1/paper285.html",
		"http://informationr.net/ir/12-2/paper298.html",
		"http://informationr.net/ir/12-2/paper290.html",
		"http://informationr.net/ir/12-2/paper291.html",
		"http://informationr.net/ir/12-2/paper292.html",
		"http://informationr.net/ir/12-2/paper293.html",
		"http://informationr.net/ir/12-2/paper294.html",
		"http://informationr.net/ir/12-2/paper295.html",
		"http://informationr.net/ir/12-2/paper296.html",
		"http://informationr.net/ir/12-2/paper297.html",
		"http://informationr.net/ir/12-2/paper306.html",
		"http://informationr.net/ir/12-2/paper303.html",
		"http://informationr.net/ir/12-2/paper304.html",
		"http://informationr.net/ir/12-2/paper299.html",
		"http://informationr.net/ir/12-2/paper300.html",
		"http://informationr.net/ir/12-2/paper302.html",
		"http://informationr.net/ir/12-2/paper305.html",
		"http://informationr.net/ir/12-2/paper307.html",
		"http://informationr.net/ir/12-2/paper301.html",
		"http://informationr.net/ir/12-3/paper309.html",
		"http://informationr.net/ir/12-3/paper310.html",
		"http://informationr.net/ir/12-3/paper311.html",
		"http://informationr.net/ir/12-3/paper312.html",
		"http://informationr.net/ir/12-3/paper313.html",
		"http://informationr.net/ir/12-3/paper314.html",
		"http://informationr.net/ir/12-3/paper315.html",
		"http://informationr.net/ir/12-3/paper316.html",
		"http://informationr.net/ir/12-3/paper317.html",
		"http://informationr.net/ir/12-3/paper318.html",
		"http://informationr.net/ir/12-3/paper319.html",
		"http://informationr.net/ir/12-3/paper320.html",
		"http://informationr.net/ir/12-3/paper308.html",
		"http://informationr.net/ir/12-4/paper330.html",
		"http://informationr.net/ir/12-4/paper323.html",
		"http://informationr.net/ir/12-4/paper328.html",
		"http://informationr.net/ir/12-4/paper322.html",
		"http://informationr.net/ir/12-4/paper324.html",
		"http://informationr.net/ir/12-4/paper326.html",
		"http://informationr.net/ir/12-4/paper325.html",
		"http://informationr.net/ir/12-4/paper329.html",
		"http://informationr.net/ir/12-4/paper327.html",
		"http://informationr.net/ir/12-4/paper321.html",
		"http://informationr.net/ir/11-1/paper240.html",
		"http://informationr.net/ir/11-1/paper241.html",
		"http://informationr.net/ir/11-1/paper242.html",
		"http://informationr.net/ir/11-1/paper244.html",
		"http://informationr.net/ir/11-1/paper243.html",
		"http://informationr.net/ir/11-1/paper245.html",
		"http://informationr.net/ir/11-4/paper260.html",
		"http://informationr.net/ir/11-4/paper261.html",
		"http://informationr.net/ir/11-4/paper262.html",
		"http://informationr.net/ir/11-4/paper263.html",
		"http://informationr.net/ir/11-4/paper264.html",
		"http://informationr.net/ir/11-4/paper265.html",
		"http://informationr.net/ir/11-4/paper266.html",
		"http://informationr.net/ir/11-4/paper267.html",
		"http://informationr.net/ir/11-4/paper269.html",
		"http://informationr.net/ir/11-4/paper270.html",
		"http://informationr.net/ir/11-4/paper268.html",
		"http://informationr.net/ir/11-4/paper271.html",
		"http://informationr.net/ir/11-4/paper272.html",
		"http://informationr.net/ir/11-4/paper273.html",
		"http://informationr.net/ir/10-1/paper212.html",
		"http://informationr.net/ir/10-1/paper201.html",
		"http://informationr.net/ir/10-1/paper203.html",
		"http://informationr.net/ir/10-1/paper210.html",
		"http://informationr.net/ir/10-1/paper206.html",
		"http://informationr.net/ir/10-1/paper199.html",
		"http://informationr.net/ir/10-1/paper202.html",
		"http://informationr.net/ir/10-1/paper205.html",
		"http://informationr.net/ir/10-1/paper208.html",
		"http://informationr.net/ir/10-1/paper211.html",
		"http://informationr.net/ir/10-1/paper209.html",
		"http://informationr.net/ir/10-1/paper200.html",
		"http://informationr.net/ir/10-1/paper198.html",
		"http://informationr.net/ir/10-1/paper207.html",
		"http://informationr.net/ir/10-1/paper204.html",
		"http://informationr.net/ir/10-2/paper225.html",
		"http://informationr.net/ir/10-2/paper222.html",
		"http://informationr.net/ir/10-2/paper220.html",
		"http://informationr.net/ir/10-2/paper219.html",
		"http://informationr.net/ir/10-2/paper218.html",
		"http://informationr.net/ir/10-2/paper223.html",
		"http://informationr.net/ir/10-2/paper224.html",
		"http://informationr.net/ir/10-2/paper214.html",
		"http://informationr.net/ir/10-2/paper216.html",
		"http://informationr.net/ir/10-2/paper215.html",
		"http://informationr.net/ir/10-2/paper217.html",
		"http://informationr.net/ir/10-2/paper221.html",
		"http://informationr.net/ir/10-2/paper227.html",
		"http://informationr.net/ir/10-2/paper226.html",
		"http://informationr.net/ir/10-2/paper213.html",
		"http://informationr.net/ir/11-2/paper246.html",
		"http://informationr.net/ir/11-2/paper247.html",
		"http://informationr.net/ir/11-2/paper248.html",
		"http://informationr.net/ir/11-2/paper249.html",
		"http://informationr.net/ir/11-2/paper250.html",
		"http://informationr.net/ir/11-3/paper251.html",
		"http://informationr.net/ir/11-3/paper252.html",
		"http://informationr.net/ir/11-3/paper253.html",
		"http://informationr.net/ir/11-3/paper254.html",
		"http://informationr.net/ir/11-3/paper256.html",
		"http://informationr.net/ir/11-3/paper257.html",
		"http://informationr.net/ir/11-3/paper258.html",
		"http://informationr.net/ir/11-3/paper259.html",
		"http://informationr.net/ir/11-3/paper255.html",
		"http://informationr.net/ir/10-3/paper228.html",
		"http://informationr.net/ir/10-3/paper229.html",
		"http://informationr.net/ir/10-3/paper230.html",
		"http://informationr.net/ir/10-3/paper231.html",
		"http://informationr.net/ir/10-3/paper232.html",
		"http://informationr.net/ir/10-4/paper239.html",
		"http://informationr.net/ir/10-4/paper234.html",
		"http://informationr.net/ir/10-4/paper235.html",
		"http://informationr.net/ir/10-4/paper236.html",
		"http://informationr.net/ir/10-4/paper237.html",
		"http://informationr.net/ir/10-4/paper238.html",
		"http://informationr.net/ir/9-1/paper166.html",
		"http://informationr.net/ir/9-1/paper162.html",
		"http://informationr.net/ir/9-1/paper163.html",
		"http://informationr.net/ir/9-1/paper164.html",
		"http://informationr.net/ir/9-1/paper165.html",
		"http://informationr.net/ir/9-2/paper167.html",
		"http://informationr.net/ir/9-2/paper168.html",
		"http://informationr.net/ir/9-2/paper171.html",
		"http://informationr.net/ir/9-2/paper169.html",
		"http://informationr.net/ir/9-2/paper173.html",
		"http://informationr.net/ir/9-2/paper170.html",
		"http://informationr.net/ir/9-2/paper174.html",
		"http://informationr.net/ir/9-2/paper172.html",
		"http://informationr.net/ir/9-3/paper175.html",
		"http://informationr.net/ir/9-3/paper178.html",
		"http://informationr.net/ir/9-3/paper179.html",
		"http://informationr.net/ir/9-3/paper181.html",
		"http://informationr.net/ir/9-3/paper177.html",
		"http://informationr.net/ir/9-3/paper180.html",
		"http://informationr.net/ir/9-3/paper176.html",
		"http://informationr.net/ir/9-4/paper196.html",
		"http://informationr.net/ir/9-4/paper197.html",
		"http://informationr.net/ir/9-4/paper188.html",
		"http://informationr.net/ir/9-4/paper191.html",
		"http://informationr.net/ir/9-4/paper195.html",
		"http://informationr.net/ir/9-4/paper187.html",
		"http://informationr.net/ir/9-4/paper186.html",
		"http://informationr.net/ir/9-4/paper184.html",
		"http://informationr.net/ir/9-4/paper192.html",
		"http://informationr.net/ir/9-4/paper189.html",
		"http://informationr.net/ir/9-4/paper183.html",
		"http://informationr.net/ir/9-4/paper185.html",
		"http://informationr.net/ir/9-4/paper193.html",
		"http://informationr.net/ir/9-4/paper194.html",
		"http://informationr.net/ir/9-4/paper182.html",
		"http://informationr.net/ir/9-4/paper190.html",
		"http://informationr.net/ir/8-1/paper140.html",
		"http://informationr.net/ir/8-1/paper141.html",
		"http://informationr.net/ir/8-1/paper142.html",
		"http://informationr.net/ir/8-1/paper143.html",
		"http://informationr.net/ir/8-1/paper144.html",
		"http://informationr.net/ir/8-1/paper145.html",
		"http://informationr.net/ir/8-2/paper147.html",
		"http://informationr.net/ir/8-2/paper148.html",
		"http://informationr.net/ir/8-2/paper149.html",
		"http://informationr.net/ir/8-2/paper146.html",
		"http://informationr.net/ir/8-2/paper150.html",
		"http://informationr.net/ir/8-3/paper151.html",
		"http://informationr.net/ir/8-3/paper154.html",
		"http://informationr.net/ir/8-3/paper152.html",
		"http://informationr.net/ir/8-3/paper153.html",
		"http://informationr.net/ir/8-4/paper161.html",
		"http://informationr.net/ir/8-4/paper157.html",
		"http://informationr.net/ir/8-4/paper160.html",
		"http://informationr.net/ir/8-4/paper158.html",
		"http://informationr.net/ir/8-4/paper156.html",
		"http://informationr.net/ir/8-4/paper159.html",
		"http://informationr.net/ir/8-4/paper155.html",
		"http://informationr.net/ir/7-1/paper112.html",
		"http://informationr.net/ir/7-1/paper113.html",
		"http://informationr.net/ir/7-1/paper121.html",
		"http://informationr.net/ir/7-1/paper114.html",
		"http://informationr.net/ir/7-1/paper115.html",
		"http://informationr.net/ir/7-1/paper116.html",
		"http://informationr.net/ir/7-1/paper117.html",
		"http://informationr.net/ir/7-1/paper118.html",
		"http://informationr.net/ir/7-1/paper120.html",
		"http://informationr.net/ir/7-1/paper122.html",
		"http://informationr.net/ir/7-1/paper119.html",
		"http://informationr.net/ir/7-4/paper134.html",
		"http://informationr.net/ir/7-4/paper135.html",
		"http://informationr.net/ir/7-4/paper136.html",
		"http://informationr.net/ir/7-4/paper137.html",
		"http://informationr.net/ir/7-4/paper138.html",
		"http://informationr.net/ir/7-4/paper139.html",
		"http://informationr.net/ir/6-1/paper86.html",
		"http://informationr.net/ir/6-1/paper88.html",
		"http://informationr.net/ir/6-1/paper89.html",
		"http://informationr.net/ir/6-1/paper90.html",
		"http://informationr.net/ir/6-1/paper87.html",
		"http://informationr.net/ir/6-1/paper85.html",
		"http://informationr.net/ir/6-1/paper91.html",
		"http://informationr.net/ir/6-2/paper92.html",
		"http://informationr.net/ir/6-2/paper93.html",
		"http://informationr.net/ir/6-2/paper94.html",
		"http://informationr.net/ir/6-2/paper95.html",
		"http://informationr.net/ir/6-2/paper96.html",
		"http://informationr.net/ir/6-2/paper103.html",
		"http://informationr.net/ir/6-2/paper97.html",
		"http://informationr.net/ir/6-2/paper98.html",
		"http://informationr.net/ir/6-2/paper99.html",
		"http://informationr.net/ir/6-2/paper100.html",
		"http://informationr.net/ir/6-2/paper101.html",
		"http://informationr.net/ir/6-2/paper102.html",
		"http://informationr.net/ir/7-2/paper126.html",
		"http://informationr.net/ir/7-2/paper127.html",
		"http://informationr.net/ir/7-2/paper128.html",
		"http://informationr.net/ir/7-2/paper123.html",
		"http://informationr.net/ir/7-2/paper124.html",
		"http://informationr.net/ir/7-2/paper125.html",
		"http://informationr.net/ir/7-3/paper131.html",
		"http://informationr.net/ir/7-3/paper132.html",
		"http://informationr.net/ir/7-3/paper129.html",
		"http://informationr.net/ir/7-3/paper130.html",
		"http://informationr.net/ir/7-3/paper133.html",
		"http://informationr.net/ir/6-3/paper104.html",
		"http://informationr.net/ir/6-3/paper105.html",
		"http://informationr.net/ir/6-3/paper108.html",
		"http://informationr.net/ir/6-3/paper106.html",
		"http://informationr.net/ir/6-3/paper107.html",
		"http://informationr.net/ir/6-4/paper109.html",
		"http://informationr.net/ir/6-4/paper110.html",
		"http://informationr.net/ir/6-4/paper111.html",
		"http://informationr.net/ir/5-1/paper64.html",
		"http://informationr.net/ir/5-1/paper65.html",
		"http://informationr.net/ir/5-1/paper66.html",
		"http://informationr.net/ir/5-1/paper67.html",
		"http://informationr.net/ir/5-1/paper68.html",
		"http://informationr.net/ir/5-2/paper69.html",
		"http://informationr.net/ir/5-2/paper70.html",
		"http://informationr.net/ir/5-2/paper71.html",
		"http://informationr.net/ir/5-2/paper72.html",
		"http://informationr.net/ir/4-1/paper48.html",
		"http://informationr.net/ir/4-1/paper49.html",
		"http://informationr.net/ir/4-1/paper50.html",
		"http://informationr.net/ir/4-1/paper51.html",
		"http://informationr.net/ir/4-2/paper52.html",
		"http://informationr.net/ir/4-2/paper53.html",
		"http://informationr.net/ir/4-2/paper54.html",
		"http://informationr.net/ir/5-3/paper73.html",
		"http://informationr.net/ir/5-3/paper74.html",
		"http://informationr.net/ir/5-3/paper75.html",
		"http://informationr.net/ir/5-3/paper76.html",
		"http://informationr.net/ir/5-3/paper77.html",
		"http://informationr.net/ir/5-3/paper78.html",
		"http://informationr.net/ir/4-3/paper56.html",
		"http://informationr.net/ir/4-3/paper57.html",
		"http://informationr.net/ir/4-3/paper58.html",
		"http://informationr.net/ir/4-3/paper59.html",
		"http://informationr.net/ir/4-3/paper55.html",
		"http://informationr.net/ir/5-4/paper79.html",
		"http://informationr.net/ir/5-4/paper80.html",
		"http://informationr.net/ir/5-4/paper81.html",
		"http://informationr.net/ir/5-4/paper82.html",
		"http://informationr.net/ir/5-4/paper83.html",
		"http://informationr.net/ir/5-4/paper84.html",
		"http://informationr.net/ir/4-4/paper60.html",
		"http://informationr.net/ir/4-4/paper61.html",
		"http://informationr.net/ir/4-4/paper62.html",
		"http://informationr.net/ir/4-4/paper63.html",
		"http://informationr.net/ir/3-1/paper23.html",
		"http://informationr.net/ir/3-1/paper24.html",
		"http://informationr.net/ir/3-1/paper25.html",
		"http://informationr.net/ir/3-1/paper26.html",
		"http://informationr.net/ir/3-1/paper27.html",
		"http://informationr.net/ir/3-1/paper28.html",
		"http://informationr.net/ir/3-1/paper29.html",
		"http://informationr.net/ir/3-1/paper30.html",
		"http://informationr.net/ir/3-1/paper31.html",
		"http://informationr.net/ir/3-1/paper32.html",
		"http://informationr.net/ir/3-1/paper33.html",
		"http://informationr.net/ir/3-1/paper34.html",
		"http://informationr.net/ir/3-1/paper35.html",
		"http://informationr.net/ir/3-2/paper40.html",
		"http://informationr.net/ir/3-2/paper36.html",
		"http://informationr.net/ir/3-2/paper37.html",
		"http://informationr.net/ir/3-2/paper38.html",
		"http://informationr.net/ir/3-2/paper39.html",
		"http://informationr.net/ir/3-3/paper41.html",
		"http://informationr.net/ir/3-3/paper42.html",
		"http://informationr.net/ir/3-3/paper43.html",
		"http://informationr.net/ir/3-4/paper44.html",
		"http://informationr.net/ir/3-4/paper47.html",
		"http://informationr.net/ir/3-4/paper45.html",
		"http://informationr.net/ir/3-4/paper46.html",
		"http://informationr.net/ir/2-1/paper9a.html",
		"http://informationr.net/ir/2-1/paper10.html",
		"http://informationr.net/ir/2-1/paper11.html",
		"http://informationr.net/ir/2-1/paper12.html",
		"http://informationr.net/ir/2-2/paper13.html",
		"http://informationr.net/ir/2-2/paper14.html",
		"http://informationr.net/ir/2-2/paper15.html",
		"http://informationr.net/ir/2-3/paper16.html",
		"http://informationr.net/ir/2-3/paper17.html",
		"http://informationr.net/ir/2-3/paper18.html",
		"http://informationr.net/ir/2-3/paper19.html",
		"http://informationr.net/ir/2-4/paper20.html",
		"http://informationr.net/ir/2-4/paper21.html",
		"http://informationr.net/ir/2-4/paper22.html",
		"http://informationr.net/ir/1-1/paper1.html",
		"http://informationr.net/ir/1-1/paper2.html",
		"http://informationr.net/ir/1-1/paper3.html",
		"http://informationr.net/ir/1-2/paper4.html",
		"http://informationr.net/ir/1-2/paper5.html",
		"http://informationr.net/ir/1-2/paper6.html",
		"http://informationr.net/ir/1-3/paper7.html",
		"http://informationr.net/ir/1-3/paper8.html",
		"http://informationr.net/ir/1-3/paper9.html"
	]

	def parseXXX(self, response):
		hxs = HtmlXPathSelector(response)

		items = []
		
		item = InformationrPaper()
		p = re.compile('^(http\:\/\/informationr\.net\/ir\/(.*)\-(.*))\/paper(.*)\.html$')
		pp = p.findall(response.url)
		issuebaseurl = pp[0][0]
		volume = pp[0][1]
		issue = pp[0][2]
		paperid = pp[0][3]
		#item['volume'] = volume
		#item['issue'] = issue
		item['paperid'] = paperid
		items.append(item)
		return items
		
######################################		
	def parse(self, response):
		hxs = HtmlXPathSelector(response)

		items = []
		
		item = InformationrPaper()

		## WARNING: for  the last issues: 18-3, 18-4, 19-1, 19-2 . "WWW" IS NEEDED!!
		#p = re.compile('^(http\:\/\/informationr\.net\/ir\/(.*)\-(.*))\/paper(.*)\.html$')
		p = re.compile('^(http\:\/\/www\.informationr\.net\/ir\/(.*)\-(.*))\/paper(.*)\.html$')
		pp = p.findall(response.url)
		print "@@@@@@@@@@@@@@@@@@@@@@"
		print response.url
		issuebaseurl = pp[0][0]
		volume = pp[0][1]
		issue = pp[0][2]
		paperid = pp[0][3]
		item['volume'] = volume
		item['issue'] = issue
		item['paperid'] = paperid
		
		if (int(volume)==1): # Exception for URL of the editorial in Volume 1
			if (int(issue)==1):
				i1 = ""
			else:
				i1 = volume 
			item['issueurl'] = issuebaseurl+"/infres"+i1+".html"
		else:
			item['issueurl'] = issuebaseurl+"/infres"+volume+issue+".html"
		
		# IR versions of HTML: version Volume >11 or Volume =<11
		
		vi = volume+"-"+issue
		if (int(volume)>16 and vi != "17-1"):
			mytitle = '//article/h1/text()'
			myauthors = '//article/div/h4/text()'
		elif ((int(volume)>=13 and int(volume)<=16) or vi=="17-1"):
			mytitle = '//body/h1/text()'
			myauthors = '//div/h4/text()'
		else:
			myauthors = '//body/h4/text()'
			mytitle = '//body/h1/text()'
		myau = hxs.select(myauthors).extract()
		if (len(str(myau)) < 5):
			myau = hxs.select('//div/h4/text()').extract()
		if (len(str(myau)) < 5):
			myau = hxs.select('//h4[contains(@align,"center")]/text()').extract()
		if (len(str(myau)) < 5):
			myau = hxs.select('//body/h4[a]/text()').extract()
			
		# Citation and year:
		# =>12-4: hxs.select('//form/fieldset/div').extract() -> delete in the beginning "<div><br>" and at the end "</div>"
		# 11-4 a 7-4: hxs.select('//body/div[h4]').extract() -> (<h4>.*</h4>) needs to be deleted
		# =<6-4: hxs.select('//body/p[@style="text-align : left; color : black;"]').extract() -> needs to delete "<p ...>" and "</p>"
		#
		if (int(volume)>11):
			mycitation = '//form/fieldset/div/text()'
		elif (int(volume) <=11 and int(volume) >=7):
			mycitation = '//body/div[h4]/text()'
		else:
			mycitation = '//body/p[@style="text-align : left; color : black;"]/text()'
		mycit = hxs.select(mycitation).extract()

		if (len(str(mycit)) < 5):
			mycit = hxs.select('//p[strong]/text()').extract()
		if (len(str(mycit)) < 5):
			mycit = hxs.select('//div[@style="text-align: center;"]/text()').extract()
		if (len(str(mycit)) < 5):
			mycit = hxs.select('//div[@align="center"][b][i]/text()').extract()
		item['citation'] = str(mycit)
		
		# NUMBER OF CITATIONS:
		# http://scholar.google.co.uk/scholar?hl=en&q=http://informationr.net/ir/9-3/paper177.html&btnG=Search&as_sdt=2000
		# hxs.select('//div[@class="gs_fl"]/a/text()').extract()[0]
		
		# Year:
		y = re.compile('^.*\((\d\d\d\d)\).*')
		yy = y.findall(str(item['citation']))
		if (len(yy)>=1):
			item['year'] = yy[0]
		else:
			item['year'] = "XXXX"
		# Number of references:
		# 1-3: len(hxs.select('//menu/li').extract())
		# 3-3, 7-4, 8-4, 11-4, 5-4,6-3,6-4: hxs.select('//body/ul[li]').re(re.compile('.*\<i\>.*'))
		#12-4: len(hxs.select('//form/fieldset/ul/li').extract())
		#13-4, 18-2: len(hxs.select('//ul[@class="refs"]/li').extract())
		
		if (int(volume)>13):
			myref = hxs.select('//ul[@class="refs"]/li').extract()
		elif (int(volume)==12):
			myref = hxs.select('//form/fieldset/ul/li').extract()
		elif (int(volume) <=11 and int(volume) >=3):
			myref = hxs.select('//body/ul/li').re(re.compile('\<i\>'))
		else:
			myref = hxs.select('//menu/li').extract()
		if (len(myref) < 2):
			myref = hxs.select('//form/fieldset/ul/li').extract()
		elif (len(myref) < 2):
			myref = hxs.select('//body/ul/li').extract()
			
		item['numref'] = len(myref)
		
		item['title'] = str(hxs.select(mytitle).extract())
		item['authors'] = str(myau)
	
		item['link'] = response.url
	
		items.append(item)
		return items

