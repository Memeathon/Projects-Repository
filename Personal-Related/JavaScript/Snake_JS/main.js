
const el=document.getElementById('myCanvas');
const ctx=el.getContext('2d');

running = true;

clockTime = 0;
const updateTime = 1;

startBody = [
    {x: 200, y: 240},
    {x: 200, y: 220},
    {x: 200, y: 200},
    {x: 180, y: 200},
];

body = [
    {x: 200, y: 240},
    {x: 200, y: 220},
    {x: 200, y: 200},
    {x: 180, y: 200},
];

possibleDir = [
    {x: 0, y: -20}, // W
    {x: 0, y: 20}, //  S
    {x: 20, y: 0}, //  D
    {x: -20, y: 0}, // A
];

bodytoAdd = false;

food = null;

document.addEventListener("keydown", (e) => {
    if (e.key === 'w') {
        chosenDir = possibleDir[0];
    } else if (e.key === 'a') {
        chosenDir = possibleDir[3];
    } else if (e.key === 's') {
        chosenDir = possibleDir[1];
    } else if (e.key === 'd') {
        chosenDir = possibleDir[2];
    }

});

chosenDir = {x: -0, y: 20};

// Box width
var bw = 380;
// Box height
var bh = 380;
// Padding
var p = 10;

function drawBoard(){
    ctx.beginPath();
    ctx.lineWidth=0.1;
    for (var x = 0; x <= bw; x += 20) {
        ctx.moveTo(0.5 + x + p, p);
        ctx.lineTo(0.5 + x + p, bh + p);
    }

    for (var x = 0; x <= bh; x += 20) {
        ctx.moveTo(p, 0.5 + x + p);
        ctx.lineTo(bw + p, 0.5 + x + p);
    }
    ctx.strokeStyle = "black";
    ctx.stroke();
};

function refresh() {
    ctx.clearRect(0, 0, canvas.width*3, canvas.height*3);
    drawBoard();

    document.getElementById('score').innerText = 'Score: ' + (body.length-1)

    if (food == null) {
        do {
            food = {x: Math.floor(lerp(2, 38, Math.random()))*10, y: Math.floor(lerp(2, 38, Math.random()))*10}
        } while ( (food.x % 20) == 10 || (food.x % 20) == 10 );
        while ( (food.y % 20) == 10 || (food.x % 20) == 10 ) {
            food = {x: Math.floor(lerp(2, 38, Math.random()))*10, y: Math.floor(lerp(2, 38, Math.random()))*10}
        };
        food.x+=10
        food.y+=10
        console.log(food, food.x % 20, food.x % 20)
    }
    
    ctx.beginPath();
    ctx.fillStyle = "black";
    ctx.fillRect(food.x,food.y,20,20);
    ctx.fillStyle = "rgba(73, 55, 39, 1)";
    ctx.fillRect(food.x+2.5,food.y+2.5,15,15);
    ctx.stroke();

    ctx.lineWidth = 20;
    ctx.lineCap = "round";
    ctx.strokeStyle = 'black';
};

function run() {
    if (Math.floor(clockTime) == updateTime) {
        clockTime=0;

        body.push({x: body[body.length-1].x + chosenDir.x, y: body[body.length-1].y + chosenDir.y});

        refresh();
        ctx.beginPath();
        ctx.moveTo(body[0].x, body[0].y);

        for (let i = 0; i < body.length; i++) {
            if (body[i].x-10 < 0 || body[i].x > 380 || body[i].y < 10 || body[i].y > 380 || (body[i].x==body[body.length-1].x && body[i].y==body[body.length-1].y && i != body.length-1)) {
                console.log("PLAYER LOST! GAME END WITH: " + body[i].x, body[i].y, 380, 380, body);
                body=[...startBody];
                chosenDir = {x: -0, y: 20};
                requestAnimationFrame(run);
                return;
            } else if (i==body.length-1 && body[i].x == food.x+10 && body[i].y == food.y+10) {
                bodytoAdd = true
            }
            console.log(food.x, food.y)
            ctx.lineTo(body[i].x, body[i].y);

        }

        ctx.stroke();
        ctx.lineWidth = 15;
        ctx.strokeStyle = "rgba(63, 84, 28, 1)";
        ctx.stroke();
        if (bodytoAdd==false) {
            body.splice(0, 1);
        } else {
            console.log("length increased!");
            food=null;
            bodytoAdd=false;
        };
        console.log(body);
     }
    clockTime+=0.01;
    requestAnimationFrame(run);
}

requestAnimationFrame(run);