$(document).ready(function() {
    var width = document.documentElement.clientWidth;
    $(".divbook").each(function(i, elem) {
        var top = 330 * Math.floor(i / Math.floor((width - 260) / 200)) + 20;
        var left = 200 * (i % Math.floor((width - 260) / 200)) + 20;
        $(this).css("top", top);
        $(this).css("left", left);
    });
});