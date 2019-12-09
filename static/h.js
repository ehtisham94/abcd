// status delete id || status update id
var sdi = 0;
var sui = 0;
var name ;
var pass ;
function forDelete(x) {
    if(sdi != 0) document.getElementById(sdi+"d").innerHTML = "<button onclick='forDelete(" + sdi + ")'>forDelete</button>"
    sdi = x;
    console.log(x);
    document.getElementById(x+"d").innerHTML = "<button onclick='cD(1)'>Yes</button> <button onclick='cD(0)'>No</button>";

}

function cD(o) {
    console.log(o);

    if (o) {
        del.id.value = sdi;
        document.getElementById('dele').submit();
    }
    else{
        document.getElementById(sdi+"d").innerHTML = "<button onclick='forDelete(" + sdi + ")'>forDelete</button>"
        sdi = 0;
    }
}


function forUpdate(x) {
    if(sui != 0) {
        document.getElementById(sui+"n").innerHTML = name;
        document.getElementById(sui+"p").innerHTML = pass;
        document.getElementById(sui+"u").innerHTML = "<button onclick='forUpdate(" + sui + ")'>forUpdate</button>";

    }
    sui = x;
    name = document.getElementById(x+"n").lastChild.nodeValue.trim();
    pass = document.getElementById(x+"p").lastChild.nodeValue.trim();

    console.log(x)
    document.getElementById(x+"n").innerHTML = "<input type='text' id='un' value='"+ name +"' >";
    document.getElementById(x+"p").innerHTML = "<input type='text' id='up' value='"+ pass +"' >";
    document.getElementById(x+"u").innerHTML = "<button onclick='cU(1)'>Yes</button> <button onclick='cU(0)'>No</button>";

}

function cU(o,un,up) {
    console.log(o);
    console.log(un);
    console.log(up);
    if (o) {
        upd.id.value = sui;
        upd.name.value = document.getElementById("un").value;
        upd.password.value = document.getElementById("up").value;
        document.getElementById('upda').submit();
    }
    else{
        document.getElementById(sui+"n").innerHTML = name;
        document.getElementById(sui+"p").innerHTML = pass;
        document.getElementById(sui+"u").innerHTML = "<button onclick='forUpdate(" + sui + ")'>forUpdate</button>"
        sui = 0;
    }

}
