$(document).ready(function() {
    $("img[id^='del_']").click(function() {
        var book_del = $(this).attr("id");
        var book_id = book_del.substring(4, book_del.length);
        $.ajax({
            url: "/delfrombag/",
            type: "POST",
            data: {"book_id": book_id},
            success: function(data) {
                $('#book_' + book_id).remove();
                $('#total_price').text(data.total_price);
                $('#bagpage_bonus_sum').text(data.bonus);
            }
        });
    });
});