$(document).ready(function() {
    $('#addtobag').click(function() {
        var current_button = $(this);
        var book_url = document.location.href.split('/');
        var book_name = $('#bookpage_bookname').text();
        $.ajax({
            url: "/addtobag/",
            type: "POST",
            data: {"book_name": book_name},
            success: function(data) {
                current_button.attr('value', data);
            }
        });
    });

    $('.star').hover(
    function() {
        $(this).css('cursor', 'pointer');
        var current_star_id = $(this).attr('id')[4];
        $(".star").each(function(i, elem) {
            if (current_star_id >= i) {
                $(this).attr('src', '/static/pictures/star_blue.png');
            } else {
                $(this).attr('src', '/static/pictures/star.png');
            }
        });
    },
    function() {
        $('#stars').hover(
        function() {

        },
        function() {
            $(".star").each(function(i, elem) {
                $(this).attr('src', '/static/pictures/star.png');
            });
        });
    });
});