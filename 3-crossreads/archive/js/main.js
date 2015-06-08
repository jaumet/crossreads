
var  svg = d3.select("body")
    .append("circle")
         .attr("class", "logo")
         .attr("cx", 225)
         .attr("cy", 225)
         .attr("r", 20)
         .style("fill", "transparent")       
         .style("stroke", "black")     
         .style("stroke-width", 0.25)
         .on("mouseover", function(){ 
               d3.select(this)
                   .style("fill", "url('http://localhost/crossreads/3-crossreads/interface/img/th/a4746001h.jpg')");
         })
          .on("mouseout", function(){ 
               d3.select(this)
                   .style("fill", "transparent");
         });
