document.addEventListener(
    "DOMContentLoaded",
    function(){



const tickets =
document.getElementById(
    "ticketsChart"
);



if(tickets){


new Chart(
tickets,
{


type:"line",


data:{


labels:[
"Lun",
"Mar",
"Mié",
"Jue",
"Vie",
"Sáb",
"Dom"
],


datasets:[{

label:
"Tickets creados",


data:[
5,
8,
12,
9,
15,
20,
25
],


borderWidth:2


}]


}


});



}







const robux =
document.getElementById(
"robuxChart"
);



if(robux){


new Chart(
robux,
{


type:"bar",


data:{


labels:[
"Lun",
"Mar",
"Mié",
"Jue",
"Vie"
],


datasets:[{


label:
"Robux entregados",


data:[
50,
120,
80,
200,
320
],


borderWidth:1


}]


}


});


}






const users =
document.getElementById(
"usersChart"
);



if(users){


new Chart(
users,
{


type:"doughnut",


data:{


labels:[
"Usuarios verificados",
"No verificados"
],


datasets:[{


data:[
2,
0
]


}]


}


});


}







const risk =
document.getElementById(
"riskChart"
);



if(risk){


new Chart(
risk,
{


type:"pie",


data:{


labels:[

"Bajo",
"Medio",
"Alto"

],


datasets:[{


data:[

80,
15,
5

]


}]


}


});


}



});