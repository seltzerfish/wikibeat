% rebase("layout.tpl", title="WikiBeat")
<!-- <h4 id="timer" style="margin-top: 4%; text-align: left; position: fixed; color: white; font-size: 50px;">timer</h4> -->
<style>
    h4::last-word {
        color: #00f;
}
</style>
<a id="startBut" class="button button-primary" onclick="play_song();" style="margin-left:auto; margin-top:20%; margin-right:auto; display: block; width:50%; background-color: black; border-color: white; height:50px; font-size: 20px"
    href="#">🔥 Done! Smash this button when u ready 🔥</a>
<h4 id="header" style="margin-top: 4%; text-align: center; color: white; font-size: 50px; display: none">{{title}}
    Rap</h4>
<div class="container" id="content">

    <h4 id="line1" style="margin-top: 4%; text-align: center; color: white; font-size: 30px; display: none"></h4>
    <h4 id="line2" style="margin-top: 4%; text-align: center; color: white; font-size: 30px; display: none"></h4>
</div>

<button id="again" class="button button-primary" onclick="play_song();" style="display: none; margin-left:auto; margin-top:20%; margin-right:auto; width:50%; background-color: black; border-color: white; height:50px; font-size: 20px">🔥
    Damn, son. Play dat again 🔥</button>
<a id="leave" href="/" class="button button-primary" onclick="play_song();" style="display: none; margin-left:auto; margin-top:2%; margin-right:auto; width:50%; background-color: black; border-color: white; height:50px; font-size: 20px">Take
    me back to da home page</a>
<script type="text/javascript" src="http://code.jquery.com/jquery-1.7.1.min.js"></script>
<script>
    function play_song() {
        var positions = eval({{ timings }})
    // console.log({{timings}})

    var audio = new Audio('../productions/{{title}}.mp3');
    audio.play();
    e = document.getElementById("startBut");
    e.style.display = "none";
    ag = document.getElementById("again");
    ag.style.display = "none";
    le = document.getElementById("leave");
    le.style.display = "none";
    e1 = document.getElementById("line1");
    e2 = document.getElementById("line2");
    e1.style.display = "block"
    e2.style.display = "block"

    title = document.getElementById("header");
    title.style.display = "block";
    var startTime = Date.now();
    var should_switch = false;


    var interval = setInterval(function () {
        var elapsedTime = Date.now() - startTime;
        // document.getElementById("timer").innerHTML = (elapsedTime / 1000).toFixed(3);
    }, 100);
    // console.log(string({{couplets}}))
    var coup = []
        % for i in range(len(couplets)):
            coup.push("{{couplets[i]}}")
                % end
    console.log(coup)
    for (i = 0; i < positions.length; i += 1) {

        if (i % 2 == 0) {
            setTimeout(setLine1.bind(null, coup[i]), positions[i][0] - interval)
        }

        else {
            setTimeout(setLine2.bind(null, coup[i]), positions[i][0] - interval)
            setTimeout(setLine1.bind(null, ""), positions[i][1] - interval)
            setTimeout(setLine2.bind(null, ""), positions[i][1] - interval)
            if (i == positions.length - 1) {
                setTimeout(make_visible.bind(null, "again"), positions[i][1] - interval + 2000)
                setTimeout(make_visible.bind(null, "leave"), positions[i][1] - interval + 2000)

            }
        }
    }
}
    function make_visible(ele_id) {
        e = document.getElementById(ele_id);
        e.style.display = "block";
    }
    function setLine1(content) {
        e = document.getElementById("line1");
        e.innerHTML = content;
    }

    function setLine2(content) {
        e = document.getElementById("line2");
        e.innerHTML = content;
    }
    $(document).ready(function () {
        $(".fancy_title").lettering();
    });
</script>