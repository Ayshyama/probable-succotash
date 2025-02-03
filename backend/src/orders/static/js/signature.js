document.addEventListener("DOMContentLoaded", function () {
    let canvas = document.getElementById("signature-pad");
    let ctx = canvas.getContext("2d");
    let drawing = false;

    canvas.addEventListener("mousedown", function () {
        drawing = true;
    });

    canvas.addEventListener("mouseup", function () {
        drawing = false;
        ctx.beginPath();
    });

    canvas.addEventListener("mousemove", function (event) {
        if (!drawing) return;
        ctx.lineWidth = 2;
        ctx.lineCap = "round";
        ctx.strokeStyle = "#000";
        ctx.lineTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
        ctx.stroke();
    });

    document.getElementById("clear-signature").addEventListener("click", function () {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    });
});
