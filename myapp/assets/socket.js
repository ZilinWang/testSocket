/**
 * Created by wangshibao on 6/29/17.
 */
var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function() {
    // socket.emit('my event', {data: 'I\'m connected!'}); // my event = rest api url
    console.log("dfasdfsadsfd");
});