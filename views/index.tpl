% rebase("layout.tpl", title="WikiBeat")

<div class="container" id="content">
  <div class="row">
    <div class="twelve column" style="margin-top: 10%">
      <h4 style="text-align: center; color: white; font-size: 70px">🔥 WikiBeat v1.1 🔥</h4>
      <h5 style="text-align: center; color: white; font-size: 20px">What's good, fam? Introducing HackGT's only bot that writes factual raps about any topic</h5>
    </div>
  </div>
  

  <div class="row" style="text-align: center; margin-top: 4%">
    <form action="/submit_topic" method="POST" >
      <div class="row">
        <div class="twelve columns">
          <input class="u-full-width" type="text" style="height:60px; font-size: 25px; text-align: center; background-color: black; color:white; border-color: grey" placeholder="Type any topic..." name="inp">
        </div>
      </div>
      
      <input class="button-primary" type="submit" style="margin-top: 2%; color:white; background-color:black; border-color:white" value="🔥 Leggo 🔥" onclick="loading();">
    </form>
    
  </div>
  
</div>

<div id="loading" style="display: none">
    <h4 style="text-align: center; color: white; font-size: 60px; margin-top: 10%">Building rap...</h4>
    <img src="static/images/loading2.gif" style="margin-left: auto; margin-right: auto; display: block;" width="300px">

  </div>
<script type="text/javascript">
  function loading(){
      var x = document.getElementById("content");
      x.style.display = "none";
      var y =  document.getElementById("loading");
      y.style.display = "block";     
  }
</script>