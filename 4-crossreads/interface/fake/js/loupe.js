/**
 * loupe.js 2.01 (21-Oct-2010) (c) by Christian Effenberger 
 * All Rights Reserved. Source: loupe.netzgesta.de
 * Distributed under Netzgestade Software License Agreement.
 * This license permits free of charge use on non-commercial 
 * and private web sites only under special conditions. 
 * Read more at... http://www.netzgesta.de/cvi/LICENSE.txt
 *
 * syntax: 
 **/

var loupe = {version : 2.01, released : '2010-10-21 12:07:00', _s: null,
	defaultVisible : false, defaultResopath : "images/loupe/", defaultCrosshair : false, defaultOpacity : 25, defaultRadius : 100, defaultColor : '#0000ff', defaultXview : 0, defaultYview : 0, defaultXoff : 8, defaultYoff : 6, defaultName : null, 
	gif : "data:image/gif;base64,R0lGODlhAQABAJH/AP///wAAAP///wAAACH/C0FET0JFOklSMS4wAt7tACH5BAEAAAIALAAAAAABAAEAAAICVAEAOw==",				
	add : function(image, options) {
		function uniqueID() {var v=Date.parse(new Date())+Math.floor(Math.random()*100000000000); return v.toString(16);}
		function getArg(a,t) {return (typeof options[a.toLowerCase()]===t?options[a.toLowerCase()]:loupe["default"+a]);};
		function getNum(a,n,m) {return Math.max(n,Math.min(m,(typeof options[a.toLowerCase()]==='number'?options[a.toLowerCase()]:loupe["default"+a])));};
		var defopts={"visible":loupe.defaultVisible,"crosshair":loupe.defaultCrosshair,"resopath":loupe.defaultResopath,"opacity":loupe.defaultOpacity,"radius":loupe.defaultRadius,"color":loupe.defaultColor,"xview":loupe.defaultXview,"yview":loupe.defaultYview,"xoff":loupe.defaultXoff,"yoff":loupe.defaultYoff,"name":loupe.defaultName};
		if(options) {for(i in defopts) {if(!options[i]) {options[i]=defopts[i];}}}else {options=defopts;} 
		var img,ctx,tmp,id,name,canvas,object=image.parentNode,vml=document.all&&!window.opera&&(!document.documentMode||document.documentMode<9)?1:0,chakra=document.all&&!window.opera&&document.documentMode&&document.documentMode>=9?1:0,nop=document.all&&!window.opera&&document.documentMode&&document.documentMode===8?1:0,w3c=vml?false:loupe.E('canvas').getContext("2d")?1:0;
		name=getArg('Name','string');image.id=(image.id!='undefined'?image.id:uniqueID());id=(name==''||name==null||loupe.G(name)?image.id:name);
		if(!loupe.G(name==''||name==null?id+"_Loupe":name)) {if(vml) {canvas=loupe.E("div");}else if(w3c) {canvas=loupe.E("canvas");}
			if(canvas) {canvas.id=(name==''||name==null?id+"_Loupe":name); canvas.vml=vml; canvas.w3c=w3c; canvas.path=getArg('Resopath','string')||''; 
				canvas.visible=getArg('Visible','boolean'); canvas.crosshair=getArg('Crosshair','boolean'); canvas.color=loupe.C(getArg('Color','string'))||'#0000ff';
				canvas.radius=parseInt(getNum('Radius',1,100),10)||100; canvas.opacity=parseInt(getNum('Opacity',1,100),10)||25; 
				var xfac=0,yfac=0,x=0,y=0,xoff=0,yoff=0,xpos=0,ypos=0,halfw=0,halfh=0; xoff=parseInt(getNum('Xoff',0,image.width),10); yoff=parseInt(getNum('Yoff',0,image.height),10);
				if(image.naturalWidth&&image.naturalHeight) {xfac=(image.naturalWidth/image.width); yfac=(image.naturalHeight/image.height); canvas.cWidth=image.naturalWidth; canvas.cHeight=image.naturalHeight;}
				else {tmp=new Image(); tmp.src=image.src; xfac=(tmp.width/image.width); yfac=(tmp.height/image.height); canvas.cWidth=tmp.width; canvas.cHeight=tmp.height; delete tmp;}
				xpos=parseInt(getNum('Xview',0,canvas.cWidth),10); ypos=parseInt(getNum('Yview',0,canvas.cHeight),10); canvas.xMulti=xfac; canvas.yMulti=yfac;
				canvas.loupe=new Image(); canvas.loupe.onload=function() {			
					if(canvas.loupe.width&&canvas.loupe.height&&canvas.loupe.width>0&&canvas.loupe.height>0) {canvas.width=canvas.loupe.width; canvas.height=canvas.loupe.height; canvas.left=0; canvas.top=0;
						canvas.lense=new Image(); canvas.lense.onload=function() {		
							if(canvas.lense.width&&canvas.lense.height&&canvas.lense.width>0&&canvas.lense.height>0) {halfw=(canvas.lense.width/2); halfh=(canvas.lense.height/2);
								canvas.icon=new Image(); canvas.icon.onload=function() {	
									if(canvas.icon.width&&canvas.icon.height&&canvas.icon.width>0&&canvas.icon.height>0) {
										if(image.width>=canvas.lense.width&&image.height>=canvas.lense.height) {
											if(!loupe.G(id+"_Switch")) {if(xpos>0||ypos>0) {
												x=Math.round(xpos>0?Math.max(1,Math.min(xpos,canvas.cWidth)):1); y=Math.round(ypos>0?Math.max(1,Math.min(ypos,canvas.cHeight)):1); 
												canvas.xPos=((canvas.width/2)-halfw-xoff)+(x/xfac); canvas.yPos=((canvas.height/2)-halfh-yoff)+(y/yfac);}else{canvas.xPos=canvas.width/2; canvas.yPos=canvas.height/2;}
												image.style.cursor='default'; image.style.cursor='default'; image.style.MozUserSelect="none"; image.style.KhtmlUserSelect="none"; 
												image.style.MozUserDrag="none"; image.style.KhtmlUserDrag="none"; image.unselectable="on"; object.style.position='relative';
												object.style.MozUserSelect="none"; object.style.KhtmlUserSelect="none"; object.unselectable="on"; if(w3c) {tmp=loupe.E("canvas");}else if(vml) {tmp=loupe.E("div");}	
												tmp.id=id+"_Switch"; tmp.height=canvas.icon.height; tmp.width=canvas.icon.width; tmp.left=0; tmp.top=0; tmp.title="switch Loupe on/off"; 
												tmp.style.position='absolute'; tmp.style.height=tmp.height+'px'; tmp.style.width=tmp.width+'px'; tmp.style.left=(image.width-tmp.width)+'px'; 
												tmp.style.top=(image.height-tmp.height)+'px'; tmp.style.cursor='pointer'; tmp.style.zIndex=9990; tmp.style.WebkitTouchCallout="none";
												tmp.style.WebkitTapHighlightColor="rgba(0,0,0,0)"; if(chakra) {tmp.style.background="url("+loupe.gif+") transparent";}
												canvas.style.cursor='move'; canvas.style.MozUserSelect="none"; canvas.style.KhtmlUserSelect="none"; canvas.style.MozUserDrag="none"; 
												canvas.style.KhtmlUserDrag="none"; canvas.unselectable="on"; loupe.A(object,tmp);
												if(w3c) {ctx=tmp.getContext("2d"); ctx.clearRect(0,0,tmp.width,tmp.height); ctx.drawImage(canvas.icon,0,0,tmp.width,tmp.height);}else 
												if(vml) {tmp.style.filter="progid:DXImageTransform.Microsoft.AlphaImageLoader(src='"+canvas.path+"icon.png')";}
												tmp.onclick=function() {loupe.toggle(canvas.id);};
											} canvas.name=id; canvas.iName=image.id; canvas.iWidth=image.width; canvas.iHeight=image.height; canvas.halfh=halfh; canvas.halfw=halfw;
											canvas.xOff=xoff; canvas.yOff=yoff; canvas.xMin=-(halfw+xoff)+(halfw/xfac); canvas.yMin=-(halfh+yoff)+(halfh/yfac); 
											canvas.xMax=image.width-(halfw+xoff)-(halfw/xfac); canvas.yMax=image.height-(halfh+yoff)-(halfh/yfac); canvas.style.width=canvas.width+'px';
											canvas.style.height=canvas.height+'px'; canvas.style.left=0+'px'; canvas.style.top=0+'px'; canvas.style.position='absolute';
											if(nop) {canvas.style.visibility="visible";}else{canvas.style.visibility=(canvas.visible?"visible":"hidden");}
											if(w3c) {canvas.style.opacity=(canvas.visible?1:0);} canvas.style.cursor='move'; canvas.style.MozUserSelect="none";
											canvas.style.KhtmlUserSelect="none"; canvas.unselectable="on"; if(chakra) {canvas.style.background="url("+loupe.gif+") transparent";}
											canvas.onclick=function() {return false;}; canvas.ondblclick=function() {return false;}; canvas.onmousedown=loupe._begin;
											if(typeof(document.ontouchstart)!="undefined"){canvas.hastouchgesture=true; canvas.ontouchstart=loupe._begin;}
											if(w3c) {canvas.style.zIndex=9999; ctx=canvas.getContext("2d"); loupe.A(object,canvas);
												ctx.clearRect(0,0,canvas.width,canvas.height); ctx.drawImage(canvas.loupe,0,0,canvas.width,canvas.height);
												if(canvas.radius==100&&(halfw==halfh)) {ctx.arc(xoff+halfw,yoff+halfh,halfw,0,Math.PI*2, false);}else{
													ctx.beginPath(); tmp=parseFloat((Math.min(canvas.lense.width,canvas.lense.height)/200)*canvas.radius);
													ctx.arc(xoff+tmp,yoff+tmp,tmp,Math.PI,Math.PI*(3/2),false);
													ctx.arc(xoff+canvas.lense.width-tmp,yoff+tmp,tmp,Math.PI*(3/2),0,false);
													ctx.arc(xoff+canvas.lense.width-tmp,yoff+canvas.lense.height-tmp,tmp,0,Math.PI*(1/2),false);
													ctx.arc(xoff+tmp,yoff+canvas.lense.height-tmp,tmp,Math.PI*(1/2),Math.PI,false); ctx.closePath();											
												} ctx.clip(); ctx.clearRect(0,0,canvas.width,canvas.height);
												ctx.drawImage(canvas.lense,canvas.xOff,canvas.yOff,canvas.lense.width,canvas.lense.height);
											}else if(vml) {canvas.style.filter="progid:DXImageTransform.Microsoft.AlphaImageLoader(src='"+canvas.path+"loupe.png',sizingMethod='scale')"; 
												canvas.style.zIndex=9997; loupe.A(object,canvas); 
												if(typeof document.namespaces==="object") {
													var e=["shape","shapetype","group","background","path","formulas","handles","fill","stroke","shadow","textbox","textpath","imagedata","line","polyline","curve","roundrect","oval","rect","arc","image"],s=document.createStyleSheet(); 
													for(var i=0; i<e.length; i++) {s.addRule("v\\:"+e[i],"behavior: url(#default#VML);");} document.namespaces.add("v","urn:schemas-microsoft-com:vml");
													if(!loupe.G(id+"_Grab")) {
														if(canvas.radius==100&&(halfw==halfh)) {vml=loupe.E('v:oval');}else {vml=loupe.E('v:roundrect'); vml.setAttribute('arcsize',(canvas.radius*0.5)+'%');}
														vml.id=id+"_Grab"; vml.setAttribute('filled','true'); vml.setAttribute('fillcolor','#ffffff'); vml.setAttribute('stroked','false');
														vml.setAttribute('strokeweight','0'); vml.style.position='absolute'; vml.style.left=xoff-1; vml.style.top=yoff-1; vml.style.zoom=1;
														vml.style.width=canvas.lense.width+1; vml.style.height=canvas.lense.height+1; vml.style.zIndex=9998; tmp=loupe.E('v:fill'); tmp.id=id+"_Pos";
														tmp.setAttribute('alignshape','false'); tmp.setAttribute('position','0,0'); tmp.setAttribute('type','tile'); tmp.setAttribute('src',image.src);
														loupe.A(vml,tmp); loupe.A(canvas,vml); 
													}  
												}else{
													if(!loupe.G(id+"_Dummy")) { tmp=loupe.E("div"); tmp.id=id+"_Dummy";
														tmp.width=canvas.width; tmp.height=canvas.height; tmp.left=0; tmp.top=0; tmp.unselectable="on"; tmp.style.position='absolute';
														tmp.style.width=canvas.width+'px'; tmp.style.height=canvas.height+'px'; tmp.style.left=0+'px'; tmp.style.top=0+'px'; tmp.style.zIndex=9998;
														loupe.A(canvas,tmp);
														var head,foot;
														if(canvas.radius==100&&(halfw==halfh)) {head='<v:shape '; foot='</v:shape>';}else{head='<v:roundrect id="'+id+'_Grab" arcsize="'+(canvas.radius*0.5)+'%" '; foot='</v:roundrect>';}
														tmp.innerHTML=head+' strokeweight="0" filled="t" stroked="f" fillcolor="#ffffff" style="zoom:1;margin:0;padding:0;position:absolute;top:'+(yoff-1)+'px;left:'+(xoff-1)+'px;width:'+(canvas.lense.width+1)+'px;height:'+(canvas.lense.height+1)+'px;"><v:fill position="0,0" id="'+id+'_Pos" src="'+image.src+'" alignshape="false" type="tile" />'+foot;
													}
												}
												if(!loupe.G(id+"_Lens")) { tmp=loupe.E("div"); tmp.id=id+"_Lens";
													tmp.width=canvas.lense.width; tmp.height=canvas.lense.height; tmp.left=xoff; tmp.top=yoff; tmp.unselectable="on"; tmp.style.position='absolute';
													tmp.style.width=canvas.lense.width+'px'; tmp.style.height=canvas.lense.height+'px'; tmp.style.left=xoff+'px'; tmp.style.top=yoff+'px'; tmp.style.zIndex=9999;
													tmp.style.filter="progid:DXImageTransform.Microsoft.AlphaImageLoader(src='"+canvas.path+"lense.png',sizingMethod='scale')"; loupe.A(canvas,tmp);
												}
											} if(nop) {canvas.style.visibility=canvas.visible?"visible":"hidden";} loupe._s=canvas; loupe._position();
										}}
								}; canvas.icon.src=canvas.path+'icon.png';}
						}; canvas.lense.src=canvas.path+'lense.png';}
				}; canvas.loupe.src=canvas.path+'loupe.png';}
		}return false;
	},
	remove : function(self) {
		if(self) {var ele=loupe.G(self.id+"_Switch");
			if(ele) {	
				if(self.inDrag&&self.w3c) {document.removeEventListener("mousemove",loupe._move,false); document.removeEventListener("mouseup",loupe._end,false);}else 
				if(self.inDrag&&self.vml) {document.detachEvent("onmousemove",loupe._move); document.detachEvent("onmouseup",loupe._end);}
				self.parentNode.removeChild(ele); self.parentNode.removeChild(self);
			}
		}return false;
	},
	toggle : function(id) {var self=loupe.G(id);
		if(self) {
			if(self.w3c) {
				if(self.style.visibility=="visible") {if(self.timer) {window.clearInterval(self.timer);} 
					var o=0,c=0,p=10,s=100/p; self.style.opacity=1;	
					self.timer=window.setInterval(function(){o=100-(p*c); self.style.opacity=o*0.01; c++; 
					if(c>s) {window.clearInterval(self.timer); self.style.opacity=0; self.style.visibility="hidden"}}, 30);
				}else if(self.style.visibility=="hidden") {if(self.timer) {window.clearInterval(self.timer);}
					var o=0,c=0,p=10,s=100/p; self.style.opacity=0; self.style.visibility="visible"
					self.timer=window.setInterval(function(){o=p*c; self.style.opacity=o*0.01;c++; 
					if(c>s) {window.clearInterval(self.timer); self.style.opacity=1;}},30);
				}
			}else {self.style.visibility=self.style.visibility!="visible"?"visible":"hidden";}
		}return false;
	},
	_position : function() {var self=loupe._s;
		if(self) {var left,top,xf,yf,xSrc,ySrc,fill,style,image=loupe.G(self.iName);
			if(image) {
				if(self.w3c) {
					var ctx=self.getContext("2d"),lensew=(self.halfw*2),lenseh=(self.halfh*2);
					left=Math.max(self.xMin,Math.min(self.xMax,Math.round(self.xPos-self.width/2)));
					top=Math.max(self.yMin,Math.min(self.yMax,Math.round(self.yPos-self.height/2)));
					xSrc=Math.round(Math.min((left-self.xMin)*self.xMulti,self.cWidth-lensew));
					ySrc=Math.round(Math.min((top-self.yMin)*self.yMulti,self.cHeight-lenseh));
					self.style.left=left+"px"; self.style.top=top+"px";
					ctx.drawImage(image,xSrc,ySrc,self.lense.width,self.lense.height,self.xOff,self.yOff,self.lense.width,self.lense.height);
					if(self.crosshair) {var style='rgba('+loupe.R(self.color)+','+(self.opacity/100)+')';
						ctx.strokeStyle=style; ctx.lineWidth=1;
						ctx.beginPath(); ctx.moveTo(parseInt(self.xOff+self.halfw,10)+.5,self.yOff);
						ctx.lineTo(parseInt(self.xOff+self.halfw,10)+.5,self.yOff+parseInt(lenseh,10)); ctx.closePath(); ctx.stroke();
						ctx.beginPath(); ctx.moveTo(self.xOff,self.yOff+self.halfh);
						ctx.lineTo(self.xOff+lensew,self.yOff+self.halfh); ctx.closePath(); ctx.stroke();
					}ctx.drawImage(self.lense,self.xOff,self.yOff,self.lense.width,self.lense.height);
				}else {fill=document.getElementById(self.name+"_Pos");
					if(fill) {			
						left=Math.max(self.xMin,Math.min(self.xMax,Math.round(self.xPos-self.width/2)));
						top=Math.max(self.yMin,Math.min(self.yMax,Math.round(self.yPos-self.height/2)));
						xSrc=Math.round(Math.min((left-self.xMin)*self.xMulti,self.cWidth-(self.halfw*2)));
						ySrc=Math.round(Math.min((top-self.yMin)*self.yMulti,self.cHeight-(self.halfh*2)));
						xf=-(xSrc/((self.halfw*2)+1)); yf=-(ySrc/((self.halfh*2)+1));
						if(document.documentMode&&document.documentMode===8) {fill.position=xf+','+yf;}else {fill.setAttribute('position',xf+','+yf);}
						self.style.left=left+"px"; self.style.top=top+"px";
					}
				}
			}
		}
		return false;
	},
	_begin: function(e) {e=e?e:window.event; e.cancelBubble=true;
		if(e.stopPropagation) {e.stopPropagation();} var self=loupe._s=this;
		if(self&&!self.inDrag) {self.inDrag=true;
			if(self.hastouchgesture&&e.touches.length==1) {e.preventDefault(); e=e.touches[0];}
			if(e.pageX) {self.startX=e.pageX; self.startY=e.pageY;}else 
			if(e.clientX) {self.startX=e.clientX; self.startY=e.clientY;}
			if(self.w3c) {
				document.addEventListener("mousemove",loupe._move,false);
				document.addEventListener("mouseup",loupe._end,false);
				self.ontouchmove=loupe._move; self.ontouchend=loupe._end;
			}else if(self.vml) {
				document.attachEvent("onmousemove",loupe._move);
				document.attachEvent("onmouseup",loupe._end);
			}
		}return false;
	},
	_move: function(e) {e=e?e:window.event; var eX=0,eY=0,self=loupe._s;
		if(self&&self.inDrag) {
			if(self.hastouchgesture&&e.touches.length==1) {e.preventDefault(); e=e.touches[0];}
			if(e.pageX) {eX=e.pageX; eY=e.pageY;}else if(e.clientX) {eX=e.clientX; eY=e.clientY;}
			self.xPos+=eX-self.startX; self.yPos+=eY-self.startY;
			self.startX=eX; self.startY=eY; loupe._position();
		}return false;
	},
	_end: function() {var self=loupe._s;
		if(self) {			
			if(self.w3c) {
				document.removeEventListener("mousemove",loupe._move,false);
				document.removeEventListener("mouseup",loupe._end,false);
				self.ontouchmove=null; self.ontouchend=null;
			}else if(self.vml) {
				document.detachEvent("onmousemove",loupe._move);
				document.detachEvent("onmouseup",loupe._end);
			}self.inDrag=false; loupe._s=null;
		}return false;
	},
	_init: function() {
		if(typeof document.namespaces==="object"&&typeof document.namespaces["v"]!=="object") {
			var e=["shape","shapetype","group","background","path","formulas","handles","fill","stroke","shadow","textbox","textpath","imagedata","line","polyline","curve","roundrect","oval","rect","arc","image"],s=document.createStyleSheet(); 
			for(var i=0; i<e.length; i++) {s.addRule("v\\:"+e[i],"behavior: url(#default#VML);");} document.namespaces.add("v","urn:schemas-microsoft-com:vml");
		}return false;
	},
	C : function(v) {if(v.toLowerCase().match(/^#[0-9a-f]{6}$/i)){return v;}else if(v.toLowerCase().match(/^#[0-9a-f]{3}$/i)){return '#'+v.substr(1,1)+v.substr(1,1)+v.substr(2,1)+v.substr(2,1)+v.substr(3,1)+v.substr(3,1);}else{return '#000000';}},
	R : function(v) {function h2d(h){return(Math.max(0,Math.min(parseInt(h,16),254)));};return h2d(v.substr(1,2))+','+h2d(v.substr(3,2))+','+h2d(v.substr(5,2));}, 
	G : function(v) {return(document.getElementById(v));}, E : function(v) {return(document.createElement(v));}, A : function(o,v) {o.appendChild(v); return false;}
}; if(window.attachEvent) {window.attachEvent("onload",loupe._init);}
