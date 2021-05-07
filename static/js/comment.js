var socket = new WebSocket('ws://localhost:8000/ws/comment');

socket.onmessage = async function(e) {
    var djangoData = JSON.parse(e.data);
    alert(djangoData);
}
$('#input2-group2').focus(() => {
    $('#input2-group2').keyup((e) => {
        code = e.keyCode;
        input = document.querySelector('#input2-group2').value;
        if (input !== "") {
            if (code === 13) {
                $('#comment-submit').click();

            }
        }
    });
});


document.querySelector('#comment-submit').onclick = function(e) {
    document.querySelector('#input2-group2').value = "";

};